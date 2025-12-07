def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    ranges, ingredients = file_contents.split("\n\n")

    ranges = [[int(j) for j in i.split("-")] for i in ranges.split("\n")]
    # ingredients = [int(i) for i in ingredients.split("\n")]

    ranges = sorted(ranges, key=lambda x: x[0])

    max_top = 0
    for r in ranges:
        if max_top >= r[1]:
            continue
        bottom = max_top + 1 if max_top >= r[0] else r[0]
        num = (r[1] - bottom) + 1
        answer += num
        max_top = r[1]

    print(answer)


if __name__ == "__main__":
    main()
