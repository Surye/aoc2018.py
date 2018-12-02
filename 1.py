day = 1


def algo1(data):
    return sum([int(x) for x in data])


def algo2(data):
    sums = [0]
    current_sum = 0
    i = 0
    while True:
        i += 1
        for freq in data:
            freq = int(freq)
            current_sum += freq
            if current_sum in sums:
                return current_sum
            else:
                sums.append(current_sum)


if __name__ == "__main__":
    test1_input = [1, -2, 3, 1]
    test1_answer = 3
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = [1, -2, 3, 1]
    test2_answer = 2
    if algo2(test2_input) == test2_answer:
        print("Second Question Test 1 Passed")
    else:
        print("Second Question Test 1 FAILED")

    test2_input = [1, -1]
    test2_answer = 0
    if algo2(test2_input) == test2_answer:
        print("Second Question Test 2 Passed")
    else:
        print("Second Question Test 2 FAILED")

    test2_input = [3, 3, 4, -2, -4]
    test2_answer = 10
    if algo2(test2_input) == test2_answer:
        print("Second Question Test 3 Passed")
    else:
        print("Second Question Test 3 FAILED")

    test2_input = [-6, 3, 8, 5, -6]
    test2_answer = 5
    if algo2(test2_input) == test2_answer:
        print("Second Question Test 4 Passed")
    else:
        print("Second Question Test 4 FAILED")

    test2_input = [7, 7, -2, -7, -4]
    test2_answer = 14
    if algo2(test2_input) == test2_answer:
        print("Second Question Test 5 Passed")
    else:
        print("Second Question Test 5 FAILED")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    print("Answer 1: ", algo1(input_data))
    print("Answer 2: ", algo2(input_data))
