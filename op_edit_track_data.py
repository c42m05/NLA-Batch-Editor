bl_info = {
    "name": "NLA Edit Track Data",
    "author": "c4205M <ylmzcanmstf@gmail.com>",
    "version": (1, 0),
    "blender": (4, 1, 1),
    "location": "Operator Search",
    "description": "Edit track data.",
    "category": "Animation"
}

import bpy

class op(bpy.types.Operator):
    """Edit tracks"""
    bl_idname = "nla.edit_track_data"
    bl_label = "Nla Edit Track Data"
    bl_options = {'REGISTER', 'UNDO'}

    name_input : bpy.props.StringProperty(
        name='Name',
        default='',
        description='Edit track name'
    ) # type: ignore

    edit_mode : bpy.props.EnumProperty(
        items=[('TOGGLE', 'Toggle', 'Toggle mute or lock properties'),
               ('SET', 'Set', 'Set mute or lock properties'),
               ],
        name="Edit Mode"
    ) # type: ignore

    mute_input : bpy.props.BoolProperty(
        name='Mute',
        default=False,
        description='Mute'
    ) # type: ignore

    lock_input : bpy.props.BoolProperty(
        name='Lock',
        default=False,
        description='Lock'
    ) # type: ignore

    @classmethod
    def poll(self, context):
        return context.area.type == 'NLA_EDITOR'
    
    def execute(self, context):
        print('\n\n\n\n################################\n###### EDIT TRACK DATA #########\n################################\n')

        for obj in context.selected_objects:
            for track in obj.animation_data.nla_tracks:
                if track.select:
                    track.name = self.name_input if self.name_input else track.name
                    
                    if self.edit_mode == 'SET':
                        track.mute = not self.mute_input
                        track.lock = self.lock_input
                    else:
                        track.mute = not track.mute if self.mute_input else track.mute
                        track.lock = not track.lock if self.lock_input else track.lock

        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()

        col.prop(self, 'name_input')
        col.prop(self, 'edit_mode')
        col.prop(self, 'mute_input')
        col.prop(self, 'lock_input')

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
classes = (
    op,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)