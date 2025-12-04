def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    for id_range in file_contents.split(","):
        s_str, e_str = id_range.split("-")
        start = int(s_str)
        end = int(e_str)
        for num in range(start, end + 1):
            num_str = str(num)
            digits = len(num_str)
            for divisor in range(2, digits + 1):
                if digits % divisor == 0:
                    step = digits // divisor
                    pattern = num_str[0:step]
                    broken = False
                    for i in range(step, digits, step):
                        if num_str[i : i + step] != pattern:
                            broken = True
                            break
                    if not broken:
                        answer += num
                        break

    print(answer)


if __name__ == "__main__":
    main()
