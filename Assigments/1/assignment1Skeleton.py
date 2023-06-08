"""
Assignment 1: Algorithms and python programming
Recursions
Dictionaries
Author: Hadas Lapid
"""
#Q1.A.
def countCInList(): # ADD INPUT
    pass
# Q1.B.
def isCNInList(): # ADD INPUT
    pass
#Q2
def countNumsDict(): # ADD INPUT
    pass

#Q3
def int2bin(): # ADD INPUT
    pass

# Q4
def recDiag(): # ADD INPUT
    pass

def main():
    # Q1 test
    l = [1, 4, 7, 1, 2, 1]
    # Q1.A.
    #print(countCInList(l, 1))
    #print(countCInList(l, 7))
    #print(countCInList(l, 8))
    #print(countCInList(l, 2))
    # Q1.B.
    #print(isCNInList(l, 1, 3))
    #print(isCNInList(l, 1, 2))
    #print(isCNInList(l, 7, 1))
    #print(isCNInList(l, 8, 3))
    #print(isCNInList(l, 8, 0))

    # Q2 test
    #print(countNumsDict(l,{}))
    ls = "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world"
    #print(countNumsDict(ls.lower().split(),{}))

    # Q3 test
    #print(int2bin(175),bin(175))
    #print(int2bin(17),bin(17))
    #print(int2bin(7),bin(7))
    #print(int2bin(235),bin(235))

    # Q4 test
    l1 =[['a','g','d','y','b'],
       ['n','b','u','k','t'],
       ['l','t','c','p','i'],
       ['y','f','v','d','e'],
       ['e','r','b','r','e']]
    #print(recDiag(l1))
    l2 = [['d', 'g', 'w', 'y', 'a'],
        ['n', 'c', 'u', 'k', 'j'],
        ['l', 's', 'b', 'p', 'l'],
        ['k', 'f', 'r', 'm', 'e'],
        ['q', 'r', 'b', 'r', 'n']]
    #print(recDiag(l2))

if __name__=="__main__":
    main()
