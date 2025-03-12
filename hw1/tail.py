from collections import deque


def tail(source, limit):
    q = deque(maxlen=limit)
    for line in source:
        q.append(line)

    for line in q:
        print(line, end="")


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    STD_LIMIT = 17
    FILE_LIMIT = 10

    if len(args) == 0:
        tail(sys.stdin, STD_LIMIT)
    elif len(args) == 1:
        with open(args[0]) as f:
            tail(f, FILE_LIMIT)
    else:
        for filename in args:
            with open(filename) as f:
                print(f"==> {filename} <==")
                tail(f, FILE_LIMIT)
