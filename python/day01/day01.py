import statistics
import re

def main():
    test = False
    if test:
        with open('test', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]

    x=0
    for l in lines:
        ints = list(map(int, re.findall(r'\d', l)))
        x += 10*ints[0] + ints[-1]
    print(x)

    y=0
    for l in lines:
        l=l.replace("one", "one1one")
        l=l.replace("two", "two2two")
        l=l.replace("three", "three3three")
        l=l.replace("four", "four4four")
        l=l.replace("five", "five5five")
        l=l.replace("six", "six6six")
        l=l.replace("seven", "seven7seven")
        l=l.replace("eight", "eight8eight")
        l=l.replace("nine", "nine9nine")
        ints = list(map(int, re.findall(r'\d', l)))
        y += 10*ints[0] + ints[-1]
    print(y)

if __name__ == '__main__':
    main()
