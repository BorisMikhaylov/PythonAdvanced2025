def wc(source):
    lines, words, _bytes = 0, 0, 0
    for line in source:
        lines += 1
        words += len(line.split())
        for c in line:
            _bytes += 1 if c.isascii() else 2
    return lines, words, _bytes


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if len(args) == 0:
        l, w, b = wc(sys.stdin)
        print(f"{l} {w} {b}")
    elif len(args) == 1:
        with open(args[0]) as f:
            l, w, b = wc(f)
            print(f"{l} {w} {b} {args[0]}")
    else:
        total_lines, total_words, total_bytes = 0, 0, 0
        for filename in args:
            with open(filename) as f:
                l, w, b = wc(f)
                total_lines += l
                total_words += w
                total_bytes += b
                print(f"{l} {w} {b} {filename}")
        print(f"{total_lines} {total_words} {total_bytes} total")
