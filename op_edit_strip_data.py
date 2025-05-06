bl_info = {
    "name": "NLA Edit Strip Data",
    "author": "c4205M <ylmzcanmstf@gmail.com>",
    "version": (1, 0),
    "blender": (4, 1, 1),
    "location": "Operator Search",
    "description": "Edit strip data.",
    "category": "Animation"
}

import bpy
from bpy.props import (BoolProperty)

class StripPropertyBoolGroup(bpy.types.PropertyGroup):
    action : BoolProperty(
        name='Action',
        default=False,
        description='Include action to edit'
    )  # type: ignore

    action_frame_end : BoolProperty(
        name='Action Frame End',
        default=False,
        description='Include action frame end to edit'
    )  # type: ignore

    action_frame_start : BoolProperty(
        name='Action Frame Start',
        default=False,
        description='Include action frame start to edit'
    )  # type: ignore

    blend_in : BoolProperty(
        name='Blend In',
        default=False,
        description='Include blend in amount to edit'
    )  # type: ignore

    blend_out : BoolProperty(
        name='Blend Out',
        default=False,
        description='Include blend out amount to edit'
    )  # type: ignore

    blend_type : BoolProperty(
        name='Blend Type',
        default=False,
        description='Include blend type to edit'
    )  # type: ignore

    extrapolation : BoolProperty(
        name='Extrapolation',
        default=False,
        description='Include extrapolation type to edit'
    )  # type: ignore

    fcurves : BoolProperty(
        name='Fcurves',
        default=False,
        description='Include fcurves to edit'
    )  # type: ignore

    frame_end : BoolProperty(
        name='End Frame',
        default=False,
        description='Include end frame value to edit'
    )  # type: ignore

    frame_start : BoolProperty(
        name='Start Frame',
        default=False,
        description='Include start frame value to edit'
    )  # type: ignore

    influence : BoolProperty(
        name='Influence',
        default=False,
        description='Include influence amount to edit'
    )  # type: ignore

    modifiers : BoolProperty(
        name='Modifiers',
        default=False,
        description='Include modifiers to edit'
    )  # type: ignore

    mute : BoolProperty(
        name='Mute',
        default=False,
        description='Include mute attribute to edit'
    )  # type: ignore

    name : BoolProperty(
        name='Name',
        default=False,
        description='Include name attribute to edit'
    )  # type: ignore

    repeat : BoolProperty(
        name='Repeat',
        default=False,
        description='Include repeat amount to edit'
    )  # type: ignore

    scale : BoolProperty(
        name='Scale',
        default=False,
        description='Include scale amount to edit'
    )  # type: ignore

    strip_time : BoolProperty(
        name='strip_time',
        default=False,
        description='Include strip time attribute to edit'
    )  # type: ignore

    strips : BoolProperty(
        name='Strips',
        default=False,
        description='Include strips attribute to edit'
    )  # type: ignore

    type : BoolProperty(
        name='Type',
        default=False,
        description='Include type attribute to edit'
    )  # type: ignore

    use_animated_influence : BoolProperty(
        name='Animated Influence',
        default=False,
        description='Include animated influence to edit'
    )  # type: ignore

    use_animated_time : BoolProperty(
        name='Animated Time',
        default=False,
        description='Include animated time to edit'
    )  # type: ignore

    use_animated_time_cyclic : BoolProperty(
        name='Animated Time Cyclic',
        default=False,
        description='Include animated time cyclic to edit'
    )  # type: ignore

    use_auto_blend : BoolProperty(
        name='Auto Blend In/Out',
        default=False,
        description='Include auto blend attribute to edit'
    )  # type: ignore

    use_reverse : BoolProperty(
        name='Reverse',
        default=False,
        description='Include reverse attribute to edit'
    )  # type: ignore

    use_sync_length : BoolProperty(
        name='Sync Length',
        default=False,
        description='Include sync length to edit'
    )  # type: ignore

class StripUserPropertyGroup(bpy.types.PropertyGroup):
    u_blend_in: bpy.props.FloatProperty(
        name='Blend In',
        default=0.0,
        description='Include blend in amount to edit'
    )  # type: ignore

    u_blend_out: bpy.props.FloatProperty(
        name='Blend Out',
        default=0.0,
        description='Include blend out amount to edit'
    )  # type: ignore

    u_blend_type: bpy.props.StringProperty(
        name='Blend Type',
        default='',
        description='Include blend type to edit'
    )  # type: ignore

    u_extrapolation: bpy.props.StringProperty(
        name='Extrapolation',
        default='',
        description='Include extrapolation type to edit'
    )  # type: ignore

    u_frame_end: bpy.props.IntProperty(
        name='End Frame',
        default=0,
        description='Include end frame value to edit'
    )  # type: ignore

    u_frame_start: bpy.props.IntProperty(
        name='Start Frame',
        default=0,
        description='Include start frame value to edit'
    )  # type: ignore

    u_influence: bpy.props.FloatProperty(
        name='Influence',
        default=0.0,
        description='Include influence amount to edit'
    )  # type: ignore

    u_mute: bpy.props.BoolProperty(
        name='Mute',
        default=False,
        description='Include mute attribute to edit'
    )  # type: ignore

    u_name: bpy.props.StringProperty(
        name='Name',
        default='',
        description='Include name attribute to edit'
    )  # type: ignore

    u_repeat: bpy.props.IntProperty(
        name='Repeat',
        default=0,
        description='Include repeat amount to edit'
    )  # type: ignore

    u_scale: bpy.props.FloatProperty(
        name='Scale',
        default=0.0,
        description='Include scale amount to edit'
    )  # type: ignore

    u_strip_time: bpy.props.FloatProperty(
        name='Strip Time',
        default=0.0,
        description='Include strip time attribute to edit'
    )  # type: ignore

    u_type: bpy.props.StringProperty(
        name='Type',
        default='',
        description='Include type attribute to edit'
    )  # type: ignore

    u_use_animated_influence: bpy.props.BoolProperty(
        name='Animated Influence',
        default=False,
        description='Include animated influence to edit'
    )  # type: ignore

    u_use_animated_time: bpy.props.BoolProperty(
        name='Animated Time',
        default=False,
        description='Include animated time to edit'
    )  # type: ignore

    u_use_animated_time_cyclic: bpy.props.BoolProperty(
        name='Animated Time Cyclic',
        default=False,
        description='Include animated time cyclic to edit'
    )  # type: ignore

    u_use_auto_blend: bpy.props.BoolProperty(
        name='Auto Blend In/Out',
        default=False,
        description='Include auto blend attribute to edit'
    )  # type: ignore

    u_use_reverse: bpy.props.BoolProperty(
        name='Reverse',
        default=False,
        description='Include reverse attribute to edit'
    )  # type: ignore

    u_use_sync_length: bpy.props.BoolProperty(
        name='Sync Length',
        default=False,
        description='Include sync length to edit'
    )  # type: ignore

class op(bpy.types.Operator):
    """Edit strips"""
    bl_idname = "nla.edit_strip_data"
    bl_label = "Nla Edit Strip Data"
    bl_options = {'REGISTER', 'UNDO'}

    clone_active: BoolProperty(
        name='Copy from active',
        default=False,
        description='Copy from active',
    ) # type:ignore

    strip_prop_include: bpy.props.PointerProperty(type=StripPropertyBoolGroup) # type: ignore
    strip_prop_user: bpy.props.PointerProperty(type=StripUserPropertyGroup) # type: ignore

    attributes_list = [
        'action',
        'action_frame_end',
        'action_frame_start',
        'blend_in',
        'blend_out',
        'blend_type',
        'extrapolation',
        'fcurves',
        'frame_end',
        'frame_start',
        'influence',
        'modifiers',
        'mute',
        'name',
        'repeat',
        'scale',
        'select',
        'strip_time',
        'strips',
        'type',
        'use_animated_influence',
        'use_animated_time',
        'use_animated_time_cyclic',
        'use_auto_blend',
        'use_reverse',
        'use_sync_length',
    ]

    @classmethod
    def poll(self, context):
        return context.area.type == 'NLA_EDITOR'
    
    def execute(self, context):
        print('\n\n\n\n################################\n###### EDIT STRIP DATA #########\n################################\n')

        for obj in context.selected_objects:
            for track in obj.animation_data.nla_tracks:
                for strip in track.strips:
                    if self.clone_active:
                        if strip.active:
                            active_strip = strip
                            break
                        else:
                            active_strip = None # ERROR NO ACTIVE STRIP
                
        for obj in context.selected_objects:
            for track in obj.animation_data.nla_tracks:
                for strip in track.strips:
                    if strip.select:
                        if self.clone_active:
                            for i in self.attributes_list:
                                if hasattr(self.strip_prop_include, i):
                                    if getattr(self.strip_prop_include, i):
                                        setattr(strip, i, getattr(active_strip, i))
                        else:
                            for i in self.attributes_list:
                                if hasattr(self.strip_prop_user, 'u_' + i):
                                    if getattr(self.strip_prop_include, i):
                                        setattr(strip, i, getattr(self.strip_prop_user, 'u_' + i))
                            if getattr(self.strip_prop_include, 'action'):
                                setattr(strip, 'action', context.scene.action)

        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()

        col.prop(self, 'clone_active')
        
        if self.clone_active:
            for i in self.attributes_list:
                if hasattr(self.strip_prop_include, i):
                    col.prop(self.strip_prop_include, i)
        else:
            col.use_property_split = False
            col.prop(self.strip_prop_include, 'action')
            if self.strip_prop_include.action:
                col.use_property_split = True
                col.prop(context.scene, 'action')
            for i in self.attributes_list:
                if hasattr(self.strip_prop_user, 'u_' + i):
                    col.use_property_split = False
                    col.prop(self.strip_prop_include, i)
                    if getattr(self.strip_prop_include, i):
                        col.use_property_split = True
                        col.prop(self.strip_prop_user, 'u_' + i)
                    

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
classes = (
    StripPropertyBoolGroup,
    StripUserPropertyGroup,
    op,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.strip_prop_include = bpy.props.PointerProperty(type=StripPropertyBoolGroup)
    bpy.types.Scene.strip_prop_user = bpy.props.PointerProperty(type=StripUserPropertyGroup)
    bpy.types.Scene.action = bpy.props.PointerProperty(type=bpy.types.Action, name='Action')

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.strip_prop_include
    del bpy.types.Scene.strip_prop_user
    del bpy.types.Scene.action