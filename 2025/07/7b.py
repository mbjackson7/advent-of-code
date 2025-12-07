def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    lines = file_contents.split("\n")
    lines[0] = lines[0].replace("S", "1")
    lines = [list(line) for line in lines]
    for i in range(1, len(lines)):
        splits = 0
        for j in range(len(lines[i - 1])):
            if lines[i - 1][j] not in [".", "^"]:
                if lines[i][j] == ".":
                    lines[i][j] = lines[i - 1][j]
                elif lines[i][j] == "^":
                    if lines[i][j - 1] == ".":
                        lines[i][j - 1] = lines[i - 1][j]
                    else:
                        lines[i][j - 1] = str(
                            int(lines[i - 1][j]) + int(lines[i][j - 1])
                        )
                    if lines[i][j + 1] == ".":
                        lines[i][j + 1] = lines[i - 1][j]
                    else:
                        lines[i][j + 1] = str(
                            int(lines[i - 1][j]) + int(lines[i][j + 1])
                        )
                else:
                    lines[i][j] = str(int(lines[i - 1][j]) + int(lines[i][j]))
    # for line in lines:
    #     print("".join(line))

    for end in lines[-1]:
        if end != ".":
            answer += int(end)
    print(answer)


if __name__ == "__main__":
    main()
