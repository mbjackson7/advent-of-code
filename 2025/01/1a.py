def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    position = 50
    answer = 0

    for line in file_contents.split("\n"):
        direction = line[0]
        amount = int(line[1:])
        if direction == "L":
            position -= amount
        else:
            position += amount
        while position < 0:
            position += 100
        while position >= 100:
            position -= 100
        if position == 0:
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()
