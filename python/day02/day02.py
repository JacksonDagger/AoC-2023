import statistics

def main():
    test = False
    if test:
        with open('test', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]
    gsum = 0
    psum = 0
    for l in lines:
        id = int(l.split(": ")[0].split(" ")[1])
        l = l.split(": ")[1]
        valid = True
        draws = l.split("; ")
        rmax = 0
        gmax = 0
        bmax = 0
        for d in draws:
            r, g, b = drawmin(d)
            rmax =max(r, rmax)
            gmax = max(g, gmax)
            bmax = max(b, bmax)
            if not possible_draw(d, 12, 13, 14):
                valid = False

        psum += rmax*gmax*bmax
        if valid:
            gsum += id
    print(gsum)
    print(psum)

def possible_draw(draw, r, g, b):
    nums = draw.split(", ")

    for x in nums:
        n, col = x.split(" ")
        n = int(n)
        if col == "blue" and n > b:
            return False
        if col == "red" and n > r:
            return False
        if col == "green" and n > g:
            return False
    return True

def drawmin(draw):
    rmax = 0
    gmax = 0
    bmax = 0

    nums = draw.split(", ")

    for x in nums:
        n, col = x.split(" ")
        n = int(n)
        if col == "blue":
            bmax = max(n, bmax)
        if col == "red":
            rmax = max(n, rmax)
        if col == "green":
            gmax = max(n, gmax)
    return rmax, gmax, bmax

if __name__ == '__main__':
    main()