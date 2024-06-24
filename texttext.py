import sys

def cat(file_name):
    f = open(file_name, "r")
    for l in f:
        print(l)
    f.close()
    return "Done"


if __name__ == "__main__":
    cat(sys.argv[1])

