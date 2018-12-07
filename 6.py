from collections import Counter

day = 6


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def algo1(data):
    coords = [tuple(map(int, x.split(","))) for x in data]

    bounding_x = [max([coord[0] for coord in coords]), min([coord[0] for coord in coords])]
    bounding_y = [max([coord[1] for coord in coords]), min([coord[1] for coord in coords])]

    dim_x = (bounding_x[0] - bounding_x[1])
    dim_y = (bounding_y[0] - bounding_y[1])

    bound_area = dim_x * dim_y

    grid = [[None] * (dim_x+1) for _ in range(dim_y+1)]

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            this_coord = (x + bounding_x[1], y + bounding_y[1])
            dists = [dist(this_coord, coord) for coord in coords]
            min_dist = min(dists)
            if dists.count(min_dist) > 1:
                grid[y][x] = -1  # overlap
            else:
                grid[y][x] = dists.index(min_dist)

    areas = Counter(x for xs in grid for x in xs)

    del areas[-1]

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if y in [0, len(grid)-1] or x in [0, len(row)-1]:  # If on the edge, probably infinite?
                try:
                    del areas[value]
                except:
                    pass

    return max(areas.values())


def algo2(data, min_dist):
    coords = [tuple(map(int, x.split(","))) for x in data]

    bounding_x = [max([coord[0] for coord in coords]), min([coord[0] for coord in coords])]
    bounding_y = [max([coord[1] for coord in coords]), min([coord[1] for coord in coords])]

    dim_x = (bounding_x[0] - bounding_x[1])
    dim_y = (bounding_y[0] - bounding_y[1])

    bound_area = dim_x * dim_y

    grid = [[None] * (dim_x+1) for _ in range(dim_y+1)]

    found = 0

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            this_coord = (x + bounding_x[1], y + bounding_y[1])
            dists = [dist(this_coord, coord) for coord in coords]
            sum_dist = sum(dists)
            if sum_dist < min_dist:
                found += 1
                grid[y][x] = "#"
            else:
                grid[y][x] = "."

    # for y, row in enumerate(grid):
    #     for x, value in enumerate(row):
    #         print(value, end=" ")
    #     print()

    return found


if __name__ == "__main__":
    test1_input = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]
    test1_answer = 17
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]
    test2_answer = 16
    if algo2(test2_input, 32) == test2_answer:
        print("Second Question Test Passed")
    else:
        print("Second Question Test FAILED")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    print("Answer 1: ", algo1(input_data))
    print("Answer 2: ", algo2(input_data, 10000))
