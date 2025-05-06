import bpy

class op(bpy.types.Operator):
    """Switches selection between NLA tracks and their strips depending on existing selection."""
    bl_idname = "nla.transfer_selection"
    bl_label = "Transfer Selection"
    bl_options = {"REGISTER", "UNDO"} # WARNING: This may be external to the search

    transfer_type: bpy.props.EnumProperty(
        items=[
            ("STOT", "Strips to tracks", "Transfer strip selection to tracks"),
            ("TTOS", "Tracks to strips", "Transfer track selection to strips",)
        ],
        default="STOT",
        name="Transfer Type",
        options=set()
    ) #type: ignore

    @classmethod
    def poll(self, context):
        return context.area.type == "NLA_EDITOR"
    
    def execute(self, context):
        selected = 0

        if self.transfer_type == "STOT":
            for obj in context.view_layer.objects: # WARNING: Blender has no selected tracks context
                if not obj.animation_data or not obj.animation_data.nla_tracks:
                    continue
                for track in obj.animation_data.nla_tracks:
                    track.select = False
                    for strip in track.strips:
                        if strip.select:
                            track.select = True
                            selected += 1
                            
            for i in context.selected_nla_strips:
                i.select = False
        
            if selected > 0:
                self.report({"INFO"}, f"{selected} track(s) selected")
            else:
                self.report({"WARNING"}, "No tracks were selected")
        else:
            for i in context.selected_nla_strips:
                i.select = False
            
            for obj in context.view_layer.objects: # WARNING: Blender has no selected tracks context
                if not obj.animation_data or not obj.animation_data.nla_tracks:
                    continue
                for track in obj.animation_data.nla_tracks:
                    if track.select:
                        track.select = False
                        for strip in track.strips:
                            strip.select = True
                            selected += 1

            if selected > 0:
                self.report({"INFO"}, f"{selected} strip(s) selected")
            else:
                self.report({"WARNING"}, "No strips were selected")

        return {"FINISHED"}