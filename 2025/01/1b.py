def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    position = 50
    answer = 0

    for line in file_contents.split("\n"):
        direction_str = line[0]
        amount = int(line[1:])
        step = -1 if direction_str == "L" else 1
        for _ in range(amount):
            position += step
            if position == -1:
                position = 99
            elif position == 100:
                position = 0
            if position == 0:
                answer += 1
        print(line, position, answer)

    print(answer)


if __name__ == "__main__":
    main()
