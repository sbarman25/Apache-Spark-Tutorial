#!/Users/snehasishbarman/anaconda/bin/python

import sys

def squareNums(itemsInPartition):
    for item in itemsInPartition:
        val = int(item)**2
        sys.stdout.write(str(val) + " ")
        
if __name__ == "__main__":
    squareNums(sys.stdin)