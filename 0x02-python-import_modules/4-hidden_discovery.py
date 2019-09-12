#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    for func in list:
        if func in list:
            if func[0] != '_':
                print("{:s}".format(func))
