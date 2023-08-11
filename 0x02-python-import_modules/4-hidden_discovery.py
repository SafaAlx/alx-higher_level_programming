#!/usr/bin/python3
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4
    # Print sorted name from directory
    for name in sorted(dir(hidden_4)):
        #print only names thet do not start with __
        if name[:2] != "__":
            print("{}".format(name))
