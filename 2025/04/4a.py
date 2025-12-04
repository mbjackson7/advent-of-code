def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    lines = file_contents.split("\n")
    visual = []
    for line in lines:
        visual.append(list(line))

    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == "@":
                adj = 0
                for row_mod in [-1, 0, 1]:
                    for col_mod in [-1, 0, 1]:
                        try:
                            if (
                                ((row + row_mod) != -1)
                                and ((col + col_mod) != -1)
                                and not (row_mod == 0 and col_mod == 0)
                            ):
                                if lines[row + row_mod][col + col_mod] == "@":
                                    adj += 1
                        except:
                            pass
                # visual[row][col] = str(adj)
                if adj < 4:
                    answer += 1
                    # print(row, col)
                    # visual[row][col] = "x"

    print(answer)

    # for line in visual:
    #   print("".join(line))


if __name__ == "__main__":
    main()
