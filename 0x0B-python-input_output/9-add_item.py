#!/usr/bin/python3
if __name__ == "__main__":
    to_jsonf = __import__('7-save_to_json_file').save_to_json_file
    from_jsonf = __import__('8-load_from_json_file').load_from_json_file
    import sys
    ac, av = len(sys.argv), sys.argv
    acl = list()
    filename = "add_item.json"
    clist = list()
    try:
        clist = from_jsonf(filename)
    except FileNotFoundError:
        with open(filename, mode="x", encoding="utf8"):
            pass
        clist = []
    if ac > 1:
        clist += av[1:]
    to_jsonf(clist, filename)
