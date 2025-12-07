def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 0

    ranges, ingredients = file_contents.split("\n\n")

    ranges = [[int(j) for j in i.split("-")] for i in ranges.split("\n")]
    ingredients = [int(i) for i in ingredients.split("\n")]

    # print(ranges)
    # print(ingredients)

    for i in ingredients:
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                answer += 1
                break

    print(answer)


if __name__ == "__main__":
    main()
