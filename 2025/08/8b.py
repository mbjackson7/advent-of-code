import math


def get_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def main():
    in_file = open("input.txt", "r")
    file_contents = in_file.read()
    answer = 1

    boxes = [[int(i) for i in j.split(",")] for j in file_contents.split("\n")]

    connections = []
    circuits: list[set] = []

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = get_distance(boxes[i], boxes[j])
            connections.append((i, j, dist))
    connections.sort(key=lambda x: x[2])

    # print(connections)
    # print(len(connections))
    # print()

    for i in range(len(boxes)):
        circuits.append(set([i]))

    for connection in connections:
        nodes = connection[:2]
        part_of: list[int] = []
        for i in range(len(circuits)):
            for box in nodes:
                if box in circuits[i]:
                    part_of.append(i)
                    break

        if len(part_of):
            # print(f"Connection {nodes} added to {part_of[0]}")
            circuits[part_of[0]].update(set(nodes))
            # print(circuits)
            for i in reversed(range(1, len(part_of))):
                circuits[part_of[0]].update(circuits[part_of[i]])
                circuits.pop(part_of[i])
                # print(f"Circuit {part_of[i]} merged into {part_of[0]}")
                # print(circuits)
        else:
            # print(f"New circuit with {nodes}")
            circuits.append(set(nodes))
            # print(circuits)

        if len(circuits) == 1:
            answer = boxes[nodes[0]][0] * boxes[nodes[1]][0]
            break

    print(answer)


if __name__ == "__main__":
    main()
