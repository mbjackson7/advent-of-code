def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    lines = file_contents.split("\n")
    lines[0] = lines[0].replace("S", "|")
    lines = [list(line) for line in lines]
    for i in range(1, len(lines)):
        for j in range(len(lines[i - 1])):
            if lines[i - 1][j] == "|":
                if lines[i][j] == ".":
                    lines[i][j] = "|"
                elif lines[i][j] == "^":
                    answer += 1
                    if j > 0:
                        lines[i][j - 1] = "|"
                    if j < len(lines[i]) - 1:
                        lines[i][j + 1] = "|"
        for line in lines:
            print("".join(line))
        print()
    for line in lines:
        print("".join(line))
    print(answer)


if __name__ == "__main__":
    main()
