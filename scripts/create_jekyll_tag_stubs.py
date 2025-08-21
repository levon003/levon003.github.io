import sys

if __name__ == "__main__":
    
    with open("tmp.txt", "w") as outfile:
        outfile.write("test\n")
        sys.exit(1)