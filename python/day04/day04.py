import statistics
import re

def main():
    test = False
    # test = True
    if test:
        with open('test', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]
    vals = []
    counts = []

    totscore = 0
    for l in lines:
        score = 0
        val = 0
        name, nums = l.split(":")
        lw, lp = nums.split(" | ")
        wins = lw.split(" ")
        wins = list(filter(lambda x: re.match(r'\d', x), wins))
        wins = list(map(lambda x: int(x), wins))

        plays = lp.split(" ")
        plays = list(filter(lambda x: re.match(r'\d', x), plays))
        plays = list(map(lambda x: int(x), plays))

        for p in plays:
            if p in wins:
                val += 1
                if score == 0:
                    score = 1
                else:
                    score *= 2

        totscore += score
        vals.append(val)
        counts.append(1)

    for i in range(len(vals)):
        v = vals[i]
        for j in range(i + 1, i + v + 1):
            counts[j] += counts[i]

    ncards = 0
    for i in range(len(vals)):
        ncards += counts[i]

    print(totscore)
    print(ncards)

if __name__ == '__main__':
    main()