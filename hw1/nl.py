if __name__ == "__main__":
    import fileinput

    line_count = 0
    with fileinput.input() as f:
        for line in f:
            line_count += 1
            print(f"{line_count} {line.rstrip()}")
