day = 5

def react_phase(poly):
    i = 0
    reacted = False

    while True:
        if i >= len(poly)-1:
            break
        if poly[i] != poly[i+1] and poly[i].lower() == poly[i+1].lower():  # Same letter, not same case.
            poly = poly[:i] + poly[i+2:]
            i -= 1
            reacted = True

        i += 1

    return poly, reacted

def algo1(data):
    poly = data[0]
    reacting = True
    while reacting:
        poly, reacting = react_phase(poly)

    return len(poly)

def algo2(data):
    results = []
    data = data[0]

    # Pre-reduce
    reacting = True
    while reacting:
        data, reacting = react_phase(data)

    for unit in list(map(chr, range(97, 123))):
        poly = data.replace(unit, '').replace(unit.upper(), '')
        results.append(algo1([poly]))
    return min(results)

if __name__ == "__main__":
    test1_input = ["dabAcCaCBAcCcaDA"]
    test1_answer = 10
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = ["dabAcCaCBAcCcaDA"]
    test2_answer = 4
    if algo2(test2_input) == test2_answer:
        print("Second Question Test Passed")
    else:
        print("Second Question Test FAILED")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    print("Answer 1: ", algo1(input_data))
    print("Answer 2: ", algo2(input_data))
