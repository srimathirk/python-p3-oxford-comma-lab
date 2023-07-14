def oxford_comma(items):
    if len(items) > 3:
        str_items = ", ".join(items[:-1]) + ", and "+ items[-1]
    elif len(items) == 3:
        str_items = f"{items[0]}, {items[1]}, and {items[2]}"  
    elif len(items) == 2:
        str_items = " and ".join(items)    
    else:
        str_items = " ".join(items)
    print(str_items)
    return str_items