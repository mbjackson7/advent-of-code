def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    for bank in file_contents.split("\n"):
        bank = list(bank)
        tmp = []
        for item in bank:
            tmp.append(int(item))
        bank = tmp
        first = 0
        second = 0
        for i in range(len(bank)):
            if i != len(bank) - 1:
                if first < bank[i]:
                    first = bank[i]
                    second = 0
                    continue
            if second < bank[i]:
                second = bank[i]
        joltage = int(str(first) + str(second))
        # print(joltage)
        answer += joltage

    print(answer)


if __name__ == "__main__":
    main()
