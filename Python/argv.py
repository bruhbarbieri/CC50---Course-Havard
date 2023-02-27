from sys import argv

if len(argv) >= 2:
    print("Hello,", end="")
    for i in range(1, len(argv)):
        print("", argv[i], end="")
    print()
else:
    print("Hello, world")