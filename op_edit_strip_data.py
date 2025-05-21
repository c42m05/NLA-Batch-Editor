import bpy

class op(bpy.types.Operator):
    """Edit strips"""
    bl_idname = "nla.edit_strip_data"
    bl_label = "Edit Strips"
    bl_options = {"REGISTER", "INTERNAL", "UNDO"}

    clone_active: bpy.props.BoolProperty(
        name="Copy from active",
        default=False,
        description="Copy from active",
    ) # type:ignore

    @classmethod
    def poll(self, context):
        return context.area.type == "NLA_EDITOR"
    
    def execute(self, context):
        strip_props = context.scene.NBE_properties.strip_props
        toggle_props = context.scene.NBE_properties.strip_toggles

        for strip in context.selected_nla_strips:
            for item in toggle_props.__annotations__.keys():
                is_editable = getattr(toggle_props, item)

                if self.clone_active:
                    if context.active_nla_strip:
                        if is_editable:
                                setattr(strip, item, user_input)
                    else:
                        self.report({"INFO"}, f"Give some info")
                else:
                    if hasattr(strip_props, item):
                        user_input = getattr(strip_props, item)

                        if is_editable:
                            setattr(strip, item, user_input)

        return {"FINISHED"}