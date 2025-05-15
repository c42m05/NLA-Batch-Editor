import bpy

class op(bpy.types.Operator):
    """Edit strips"""
    bl_idname = "nla.edit_strip_data"
    bl_label = "Nla Edit Strip Data"
    bl_options = {'REGISTER', 'UNDO'}

    clone_active: bpy.props.BoolProperty(
        name='Copy from active',
        default=False,
        description='Copy from active',
    ) # type:ignore

    @classmethod
    def poll(self, context):
        return context.area.type == 'NLA_EDITOR'
    
    def execute(self, context):
        strip_props = context.scene.NBE_strip_properties
        toggle_props = context.scene.NBE_strip_property_toggles

        # WARNING: Hard coded list
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

        for strip in context.selected_nla_strips:
            for item in attributes_list:
                if hasattr(toggle_props, item):
                    has_edit = getattr(toggle_props, item)

                    if self.clone_active:
                        if context.active_nla_strip:
                            if has_edit:
                                    setattr(strip, item, user_input)
                        else:
                            self.report({"INFO"}, f"Give some info")
                    else:
                        if hasattr(strip_props, item):
                            user_input = getattr(strip_props, item)

                            if has_edit:
                                setattr(strip, item, user_input)

        return {'FINISHED'}