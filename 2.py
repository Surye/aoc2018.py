from collections import defaultdict

day = 2


def algo1(data):
    twos = 0
    threes = 0
    for word in data:
        freq = defaultdict(int)
        for letter in word:
            freq[letter] += 1
        if 2 in freq.values():
            twos += 1
        if 3 in freq.values():
            threes += 1
    return twos * threes


def algo2(data):
    for i, id1 in enumerate(data):
        for id2 in data[i+1:]:
            same_chars = []
            for letter1, letter2 in zip(id1, id2):
                if letter1 == letter2:
                    same_chars.append(letter1)
            if len(id2)-len(same_chars) == 1:
                return ''.join(same_chars)


if __name__ == "__main__":
    test1_input = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]
    test1_answer = 12
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]
    test2_answer = "fgij"
    if algo2(test2_input) == test2_answer:
        print("Second Question Test Passed")
    else:
        print("Second Question Test FAILED")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    print("Answer 1: ", algo1(input_data))
    print("Answer 2: ", algo2(input_data))
