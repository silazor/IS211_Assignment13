'''
Write a function in recursion.py, called
fibonnaci, which will accept one integer parameter (lets call it n) and returns the n
th element of the Fibonnaci
sequence.
'''

def fibonnaci(n):
    if n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
print(fibonnaci(10))

'''
Write a recursive function called
gcd that takes parameters a and b and returns their greatest common divisor. Think about what the base
case is for this algorithm.
'''
def gcd(a, b):
    if a < b:
        # we want b>=a
        print('returned ourself')
        return gcd(b, a)
    # keep
    while b !=0:
        (a, b) = (b, a % b)

    return a

print(gcd(98, 108))

def compareTo(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 'ERROR: string len needs to be at least 1'
    for char in s1:
        if char == s2[0]:
            ns1 = s1[1:]
            ns2 = s2[1:]
            if len(ns1) == 0 and len(ns2) == 0:
                return 0
            if len(ns1) == 0 and len(ns2) != 0:
                return -1
            if len(ns1) != 0 and len(ns2) == 0:
                return 1
            return compareTo(ns1, ns2)
        else:
            s1v = ord(char)
            s2v = ord(s2[0])
            if s1v > s2v:
                return 1
            if s2v > s1v:
                return -1

print(compareTo('abc', 'abd'))
