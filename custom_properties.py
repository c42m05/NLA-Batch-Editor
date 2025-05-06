import bpy
class StripProperties(bpy.types.PropertyGroup): 
    name : bpy.props.StringProperty(
        name="Name",
        default="",
        description="Search name",
        options=set()
    ) # type: ignore
    
    is_search_includes : bpy.props.BoolProperty(
        name="Name Contains Keyword",
        default=True,
        description="When enabled, the search key will inclusively match any part of the target names. Disable for exact matching only.",
        options=set()
    ) # type: ignore

    frame_start : bpy.props.FloatProperty(
        name="Start Frame",
        default=0,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore

    frame_end : bpy.props.FloatProperty(
        name="End Frame",
        default=0,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore

    extrapolation : bpy.props.EnumProperty(
        items=[("HOLD", "Hold", "Add to selection when extrapolation is hold"),
               ("HOLD_FORWARD", "Hold Forward", "Add to selection when extrapolation is hold forward"),
               ("NOTHING", "Nothing", "Add to selection when extrapolation is nothing")],
        name="Extrapolation",
        options=set()
    ) # type: ignore
    
    blend_type : bpy.props.EnumProperty(
        items=[("REPLACE", "Replace", "Add to selection when blend type is replace"),
               ("COMBINE", "Combine", "Add to selection when blend type is combine"),
               ("ADD", "Add", "Add to selection when blend type is add"),
               ("SUBTRACT", "Subtract", "Add to selection when blend type is subtract"),
               ("MULTIPLY", "Multiply", "Add to selection when blend type is multiply")],
        name="Blend Type",
        options=set()
    ) # type: ignore
    
    use_auto_blend : bpy.props.BoolProperty(
        name="Auto Blend In/Out",
        default=False,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore
    
    blend_in : bpy.props.FloatProperty(
        name="Blend In",
        default=10,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore
    
    blend_out : bpy.props.FloatProperty(
        name="Blend Out",
        default=0,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore
    
    use_reverse : bpy.props.BoolProperty(
        name="Reversed",
        default=False,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore
    
    use_animated_influence : bpy.props.BoolProperty(
        name="Animated Influence",
        default=False,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore
    
    influence : bpy.props.FloatProperty(
        name="Influence",
        default=1,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore
    
    scale : bpy.props.FloatProperty(
        name="Scale",
        default=1,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore
    
    repeat : bpy.props.IntProperty(
        name="Repeat",
        default=1,
        description="Add to selection when value is",
        options=set()
    ) # type: ignore

class PushdownProperties(bpy.types.PropertyGroup):
    frame_start : bpy.props.IntProperty(
    name="Frame Start",
    default=1,
    description="Frame starts at",
    options=set()
    ) # type: ignore

    start_min : bpy.props.IntProperty(
        name="Start Min",
        default=2,
        description="Random frame starts do not go below",
        options=set()
    ) # type: ignore

    start_max : bpy.props.IntProperty(
        name="Start Max",
        default=5,
        description="Random frame starts do not go above",
        options=set()
    ) # type: ignore

    random_start : bpy.props.BoolProperty(
        name="Randomize",
        default=False,
        description="Assign random starts for each strip",
        options=set()
    ) # type: ignore

    track_name : bpy.props.StringProperty(
        name="New Track Name",
        default="Animation_**OBJECT**",
        description="Set name for new tracks. Tip: **OBJECT** will be substituted with the name of the associated object."
    ) # type: ignore

    strip_name : bpy.props.StringProperty(
        name="New Strip Name",
        default="AnimationStrip_**OBJECT**",
        description="Set name for new strips. Tip, **object** will be replaced by its object name."
    ) # type: ignore

    distinct_strip_name : bpy.props.BoolProperty(
        name="Distinct Strip Names",
        default=False,
        description="Set strip names different than tracks",
        options=set()
    ) # type: ignore

    set_mute_new_track : bpy.props.BoolProperty(
        name="Mute New Tracks",
        default=False,
        description="Set mute new tracks",
        options=set()
    ) # type: ignore

    keep_actions : bpy.props.BoolProperty(
        name="Keep actions",
        default=False,
        description="Keeps actions in Action Editor",
        options=set()
    ) # type: ignore

    change_action_name : bpy.props.BoolProperty(
        name="Change Action Name",
        default=False,
        description="Change action names (Number prefixes will be added as blender default)",
        options=set()
    ) # type: ignore

class DublicateOpsProperties(bpy.types.PropertyGroup):
    dublicate_name: bpy.props.StringProperty(
        name="Track Name",
        default="Dublicate_**TRACK_NAME**",
        description="Set name for copy tracks. Tip: **TRACK_NAME** will be substituted with the name of the original track",
        options=set()
    ) #type: ignore

    is_copy_linked : bpy.props.BoolProperty(
        name="Linked Copy",
        default=True,
        description="When disabled, actions of strips will also be dublicated", # TODO: Description needed
        options=set()
    ) # type: ignore

    # is_strip_name : bpy.props.BoolProperty(
    #     name="Rename Strips",
    #     default=True,
    #     description="Add to selection when value is", # TODO: Description needed
    #     options=set()
    # ) # type: ignore

class ModifySelectionProperties(bpy.types.PropertyGroup):
    selection_option : bpy.props.EnumProperty(
        items=[("ADD", "Add", "Add to current selection"),
               ("SUBTRACT", "Subtract", "Subtract from current selection"),
               ("INTERSECT", "Intersect", "Intersect with current selection"),
               ],
        name="Selection Option",
        options=set()
    ) # type: ignore
    
    selection_type : bpy.props.EnumProperty(
        items=[("TRACK", "Track", "Modify track selection"),
               ("STRIP", "Strip", "Modify strip selection")],
        name="Selection by",
        options=set()
    ) # type: ignore
    
    include_tracks : bpy.props.EnumProperty(
        items=[("BOTH", "Both", "Include both muted and locked tracks"),
               ("MUTE", "Mute", "Include only muted tracks"),
               ("LOCK", "Lock", "Include only locked tracks"),
               ("NONE", "None", "Muted and locked tracks are excluded"),],
        name="Include Tracks",
        options=set()
    ) # type: ignore
    
    filter_method : bpy.props.EnumProperty(
        items=[("name", "Name", "Filter by name"),
               ("frame_start", "Start Frame", "Filter by start frame value"),
               ("frame_end", "End Frame", "Filter by end frame value"),
               ("extrapolation", "Extrapolation Type", "Filter by extrapolation type"),
               ("blend_type", "Blend Type", "Filter by blend type"),
               ("use_auto_blend", "Auto Blend State", "Filter by auto blend state"),
               ("blend_in", "Blend In Amount", "Filter by blend in amount"),
               ("blend_out", "Blend Out Amount", "Filter by blend out amount"),
               ("use_reverse", "Reverse State", "Filter by reverse state"),
               ("use_animated_influence", "Animated Influence State", "Filter by animated influence state"),
               ("influence", "Influence Amount", "Filter by influence amount"),
               ("scale", "Scale", "Filter by scale"),
               ("repeat", "Repeat", "Filter by repeat")],
        name="Filter by",
        options=set()
    ) # type: ignore

classes = (
    ModifySelectionProperties,
    StripProperties,
    PushdownProperties,
    DublicateOpsProperties,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.NBE_modify_selection_properties = bpy.props.PointerProperty(type=ModifySelectionProperties)
    bpy.types.Scene.NBE_strip_properties = bpy.props.PointerProperty(type=StripProperties)
    bpy.types.Scene.NBE_pushdown_properties = bpy.props.PointerProperty(type=PushdownProperties)
    bpy.types.Scene.NBE_dublicate_op_properties = bpy.props.PointerProperty(type=DublicateOpsProperties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.NBE_modify_selection_properties
    del bpy.types.Scene.NBE_strip_properties
    del bpy.types.Scene.NBE_pushdown_properties
    del bpy.types.Scene.NBE_dublicate_op_properties