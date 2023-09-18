def NULL_not_found(object: any) -> int:
    name = ""

    if object is None:
        name = "Nothing"
    elif object is False:
        name = "Fake"
    elif object != object:
        name = "Cheese"
    elif object == 0:
        name = "Zero"
    elif object == "":
        name = "Empty"
    else:
        print("Type not found")
        return 1

    print(f"{name}: {object} {type(object)}")
    return 0
