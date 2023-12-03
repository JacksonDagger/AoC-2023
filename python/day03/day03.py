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
    numbers = []

    for i, l in enumerate(lines):
        lastmatch = False
        start = 0
        for j, c in enumerate(list(l)):
            if (re.match(r'\d', c)):
                if not lastmatch:
                    start = j
                lastmatch = True
            elif lastmatch:
                numbers.append((start, j - 1, i))
                lastmatch = False
        if lastmatch:
            numbers.append((start, len(l) - 1, i))

    sum = 0
    for coll, colr, row in numbers:
        found = False
        maxcol = len(lines[0])
        for i in range(bound(0, len(lines), row-1), bound(0, len(lines), row+2)):
            for c in lines[i][bound(0, maxcol, coll-1):bound(0, maxcol+1, colr+2)]:
                if not (re.match(r"\d", c) or c=="."):
                    x = parsenumber(coll, colr, row, lines)
                    sum += x

                    found = True
                    break
            if found:
                next
    print(sum)

    newlines = []
    for l in lines:
        newlines.append(list(l))
    lines = newlines
    sum = 0
    for coll, colr, row in numbers:
        x = parsenumber(coll, colr, row, lines)
        maxcol = len(lines[0])
        for i in range(bound(0, len(lines), row-1), bound(0, len(lines), row+2)):
            for j in range(bound(0, maxcol, coll-1), bound(0, maxcol, colr+2)):
                c = lines[i][j]
                if c == "*":
                    lines[i][j] = (1, x)
                elif isinstance(c, tuple):
                    n, g = c
                    if n == 1:
                        lines[i][j] = (2, g*x)
                    else:
                        lines[i][j] = "."
    for l in lines:
        for c in l:
            if isinstance(c, tuple):
                n, g = c
                if n == 2:
                    sum +=g       
    print(sum)
            
                    
def bound(min, max, x):
    if x > max:
        return max
    if x < min:
        return min
    return x
                
def parsenumber(coll, colr, row, lines):
    
    num = 0
    for i in range(coll, colr+1):
        num *= 10
        num += int(lines[row][i])
    return(num)


if __name__ == '__main__':
    main()