folder_hierarchy = {
    "name": "level 1 directory",
    "children": [
        {
            "name": "level 2 directory A",
            "children": [
                {"name": "level 3 directory A1", "children": []},
                {"name": "level 3 directory A2", "children": []},
            ],
        },
        {
            "name": "level 2 directory B",
            "children": [{"name": "level 3 directory B1", "children": []}],
        },
        {
            "name": "level 2 directory C",
            "children": [
                {"name": "level 3 directory C1", "children": []},
                {"name": "level 3 directory C2", "children": []},
                {"name": "level 3 directory C3", "children": []},
            ],
        },
    ],
}


def pretty_print(node, indent=""):
    print(indent + node["name"])
    for child in node["children"]:
        pretty_print(child, indent + "  ")


pretty_print(folder_hierarchy)
