"""
Implementation of Google Code Jam's Store Credit problem in Python

https://code.google.com/codejam/contest/dashboard?c=351101#s=p0
"""

from sys import argv

""" Solve each individual case"""
def solve(c):
    credit = c[0]
    nitems = c[1]
    prices = c[2]

    # Create a dictionary: key = |x-u|, value is index of first occurence
    diffs = {}
    mid = float(credit)/2
    for i in range(0, nitems):
        diff = abs(prices[i]-mid)
        if diff in diffs and prices[diffs[diff]] + prices[i] == credit:
            return (diffs[diff], i)
        diffs[diff] = i

""" Getting input from a file """
def prompt(file):
    f = open(file)
    ntest_case = int(f.readline())
    cases = []
    for i in range(0, ntest_case):
        credit= int(f.readline())
        nitems = int(f.readline())
        prices = f.readline().split()
        assert len(prices) == nitems
        prices = map(int, prices)
        cases.append((credit, nitems, prices))
    return cases
    

if __name__ == "__main__":
    # usage: store_credit.py in_file out_file
    script, in_file, out_file = argv
    cases = prompt(in_file)

    # Solve for each cases
    out = open(out_file, 'w')
    for i in range(0, len(cases)):
        a, b = solve(cases[i])
        out.write("Case #%i: %i %i\n" % (i+1, a+1, b+1))
