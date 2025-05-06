import bpy
from . import utilities_helpers

class op(bpy.types.Operator):
    """Dub tracks"""
    bl_idname = "nla.dub_track_data"
    bl_label = "Nla Dub Track Data"
    bl_options = {"REGISTER", "INTERNAL", "UNDO"}

    dublicate_name: bpy.props.StringProperty(
        name='name',
        default='Dublicate',
    ) #type: ignore

    naming_type: bpy.props.EnumProperty(
        items=[('SET', 'Set', 'Modify track selection'),
                ('PREFIX', 'Prefix', 'Modify strip selection'),
                ('SUFFIX', 'Suffix', 'Modify strip selection'),
                ],
        name="Naming by",
        default='PREFIX',
    ) #type: ignore

    @classmethod
    def poll(self, context):
        return context.area.type == 'NLA_EDITOR'
    
    def execute(self, context):
        result_selection = []

        for obj in context.selected_objects:
            for track in obj.animation_data.nla_tracks:
                if track.select:
                    for strip in track.strips:
                        new_track = obj.animation_data.nla_tracks.new(prev=None)
                        new_track.name = set_name(self.dublicate_name, self.naming_type, track.name)
                        new_track.mute = False
                        track.select = False
                        break          

                for strip in track.strips:
                    if strip.select:
                        new_strip = new_track.strips.new(strip.action.name, int(strip.frame_start), strip.action)
                        utilities_helpers.copy_attr(strip, new_strip)
                        strip.select = False
                        new_strip.select = False
                        result_selection.append(new_strip)

        for i in result_selection:
            i.select = True

        del result_selection

        return {'FINISHED'}
    
def set_name(input, method, original):
    if method == 'SET':
        return input
    elif method == 'PREFIX':
        input = 'copy_' if not input else input
        return '_'.join((input, original))
    else:
        input = '_copy' if not input else input
        return '_'.join((original, input))