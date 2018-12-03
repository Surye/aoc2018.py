import re
from collections import Counter
day = 3

SHEET_SIZE = 1100

def fill_sheet1(sheet, claim, x, y, w, h):
    for row in range(1, w+1):
        for col in range(1, h+1):
            xrow = row+x-1
            xcol = col+y-1
            if not sheet[xcol][xrow]:
                sheet[xcol][xrow] = claim
            else:
                # Overlap
                #print(f"#{claim} overlapping on #{sheet[xcol][xrow]}")
                sheet[xcol][xrow] = 'X'

def algo1(data):
    sheet = [[None] * SHEET_SIZE for _ in range(SHEET_SIZE)]   # 1000x1000 array
    for claim in data:
        #print(claim)
        match = re.match(r'^#(?P<claim>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', claim)
        fill_sheet1(sheet, int(match['claim']), int(match['x']), int(match['y']), int(match['w']), int(match['h']))

    c = Counter(x for xs in sheet for x in xs)

    return c['X']


def fill_sheet2(sheet, claims, claim, x, y, w, h):
    for row in range(1, w+1):
        for col in range(1, h+1):
            xrow = row+x-1
            xcol = col+y-1
            if not sheet[xcol][xrow]:
                sheet[xcol][xrow] = [claim]
            else:
                sheet[xcol][xrow].append(claim)
                for c in sheet[xcol][xrow]:
                    try:
                        claims.remove(c)
                    except KeyError:
                        pass # Don't care if we remove one that's gone.


def algo2(data):
    sheet = [[None] * SHEET_SIZE for _ in range(SHEET_SIZE)]   # 1000x1000 array
    claims = set()
    for claim in data:
        match = re.match(r'^#(?P<claim>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', claim)
        claims.add(int(match['claim']))
        fill_sheet2(sheet, claims, int(match['claim']), int(match['x']), int(match['y']), int(match['w']), int(match['h']))
    return claims.pop()


if __name__ == "__main__":
    test1_input = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    test1_answer = 4
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    test2_answer = 3
    if algo2(test2_input) == test2_answer:
        print("Second Question Test Passed")
    else:
        print("Second Question Test FAILED")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    print("Answer 1: ", algo1(input_data))
    print("Answer 2: ", algo2(input_data))
