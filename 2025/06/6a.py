def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    answers = []

    lines = [[s for s in i.split(" ") if s] for i in file_contents.split("\n")]

    for op in lines[-1]:
        if op == "+":
            answers.append(0)
        else:
            answers.append(1)

    for i in range(len(lines) - 1):
        for j in range(len(lines[i])):
            num = int(lines[i][j])
            if lines[-1][j] == "+":
                answers[j] += num
            else:
                answers[j] *= num

    for num in answers:
        answer += num

    print(answer)


if __name__ == "__main__":
    main()
