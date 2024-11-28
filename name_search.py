import string

import numpy as np
import argparse

class NameSearch:

    def __init__(self, Name_List, Name_Algorithm, Name_Length):
        # Matrix of the word search puzzle 
        self.matrix = np.load("./data/matrix.npy")
        # Name of the algorithm
        self.Name_Algorithm = Name_Algorithm
        # Length of the name
        self.Name_Length = Name_Length
        # List of all potential names 
        with open("./data/names/"+Name_List+".txt", 'r') as f:
            self.names = f.read().splitlines()
        self.names = [n.upper().strip() for n in self.names]

    def match_BruteForce(self, pattern, text):
        for i in range(len(text)): #modified solution from my submission for leetcode problem 28
            matched = 0
            key = list(pattern)
            while key:
                if i+matched >= len(text) or text[i+matched] != key.pop(0):
                    break
                else:
                    #print("found", c, "at index", i)
                    matched += 1
                if not key:
                    print('Using', self.Name_Algorithm, 'the length of the name is', len(pattern), 'and the name is', pattern)


    def match_Horspool(self, pattern, text):
        table = dict.fromkeys(string.ascii_uppercase, len(pattern))

        pattern_size = len(pattern)

        for i in range(pattern_size-1):
            table[pattern[i]] = pattern_size - 1 - i

        i = pattern_size - 1

        while i < len(text):
            matched = 0
            key = list(pattern)
            while key:
                if i-matched < 0 or text[i-matched] != key.pop():
                    break
                matched += 1
            if not key:
                print(f'Using {self.Name_Algorithm}, the length of the name is {pattern_size} and the name is {pattern}')
                #return i - (pattern_size - 1)
            i += table.get(text[i], pattern_size)
        return -1

    #extra credit no numpy diagonal
    def get_diagonals(self, matrix, size):
        left = []
        right = []

        #left
        for c in range(-(size + 1), size):
            i = max(0, -c)
            j = max(0, c)

            while i < size and j < size:
                left.append(matrix[i][j])
                i += 1
                j += 1

        #right
        for c in range(size, size-1):
            if c < size:
                i = 0
                j = c
            else:
                j = size-1
                i = c - j

            while i < size and j >= 0:
                right.append(matrix[i][j])
                i += 1
                j += 1

        return left, right

        
    def search(self):
        # pattern is each name in self.names
        for name in self.names:
            if len(name) == self.Name_Length:
                pattern = name.upper()

                # text is each horizontal, vertical, and diagonal strings in self.matrix
                size = self.matrix.shape[0]
                text_r = self.matrix.flatten().tolist()
                #print(text_r)
                text_c = self.matrix.flatten(order='F').tolist()
                #print(text_c)

                text_dl, text_dr = self.get_diagonals(self.matrix, size)

                if self.Name_Algorithm == "BruteForce":
                    self.match_BruteForce(pattern, text_r)
                    self.match_BruteForce(pattern, text_c)

                    self.match_BruteForce(pattern, text_dl)
                    self.match_BruteForce(pattern, text_dr)
                elif self.Name_Algorithm == "Horspool":
                    self.match_Horspool(pattern, text_r)
                    self.match_Horspool(pattern, text_c)

                    self.match_Horspool(pattern, text_dl)
                    self.match_Horspool(pattern, text_dr)

if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Word Searching')
    parser.add_argument('-name', dest='Name_List', required = True, type = str, help='Name of name list')
    parser.add_argument('-algorithm', dest='Name_Algorithm', required = True, type = str, help='Name of algorithm')
    parser.add_argument('-length', dest='Name_Length', required = True, type = int, help='Length of the name')
    args = parser.parse_args()

    # Example:
    # python name_search.py -algorithm BruteForce -name Mexican -length 5

    obj = NameSearch(args.Name_List, args.Name_Algorithm, args.Name_Length)
    obj.search()


