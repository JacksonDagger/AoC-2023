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

    for l in lines:
        continue

if __name__ == '__main__':
    main()