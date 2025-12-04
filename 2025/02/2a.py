def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    for id_range in file_contents.split(","):
        s_str, e_str = id_range.split("-")
        slen = len(s_str)
        elen = len(e_str)
        if slen == elen and slen % 2 == 1:
            continue
        start = int(s_str)
        end = int(e_str)
        for num in range(start, end + 1):
            num_str = str(num)
            digits = len(num_str)
            if digits % 2 == 0:
                half = digits // 2
                if num_str[:half] == num_str[half:]:
                    answer += num

    print(answer)


if __name__ == "__main__":
    main()
