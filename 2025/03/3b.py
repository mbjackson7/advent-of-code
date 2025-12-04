def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0
    DIGITS = 12

    for bank in file_contents.split("\n"):
        bank = list(bank)
        tmp = []
        for item in bank:
            tmp.append(int(item))
        bank = tmp
        joltage = ""

        lastPos = -1

        for index in range(DIGITS):
            max_val = 0
            for batt_i in range(lastPos + 1, len(bank) - (DIGITS - index - 1)):
                if max_val < bank[batt_i]:
                    max_val = bank[batt_i]
                    lastPos = batt_i
            joltage += str(max_val)
        answer += int(joltage)
        # print(joltage)

    print(answer)


if __name__ == "__main__":
    main()
