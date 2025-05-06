def copy_attr(source, target, props = [], ignore_props = True):
    # Get attributes
    all_attributes = dir(source)
    properties = [
        attr 
        for attr in all_attributes 
        if (
            not callable(getattr(source, attr)) and 
            not attr.startswith("_") and 
            not 'bl_rna' in attr and
            (not attr in props if ignore_props else attr in props)
        )
    ]
    
    properties.reverse() # To fix a stupid bug
    
    for i in properties:
        if not target == source and not source.is_property_readonly(i):
            newattr = getattr(source, i)
            setattr(target, i, newattr)