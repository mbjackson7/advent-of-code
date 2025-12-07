def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    lines = file_contents.split("\n")

    lengths = []
    digits = []
    spacing = 0
    for char in lines[-1]:
        if char == " ":
            spacing += 1
        elif spacing != 0:
            lengths.append(spacing)
            digits.append([""] * spacing)
            spacing = 0
    lengths.append(spacing + 1)
    digits.append([""] * (spacing + 1))

    # print(lengths)
    # print(digits)
    for i in range(len(lines) - 1):
        line = lines[i]
        print(line)
        pos = 0
        for j in range(len(lengths)):
            length = lengths[j]
            for mod in range(length):
                digit = line[pos + mod]
                if digit != " ":
                    digits[j][mod] += digit
            pos += length + 1

    print(digits)

    ops = [s for s in lines[-1].split(" ") if s]
    for i in range(len(ops)):
        op = ops[i]
        solution = 1
        if op == "+":
            solution = 0
        for num in digits[i]:
            if op == "+":
                solution += int(num)
            else:
                solution *= int(num)
        answer += solution

    print(answer)


if __name__ == "__main__":
    main()
