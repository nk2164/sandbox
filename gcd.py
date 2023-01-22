def gcd(m,n):
    # Make sure m and n are positive integers.
    if (m < 0 or n < 0):
        return -1

    # set remainder to some non zero value, say -1. This is to make it
    # go into the while loop.
    r = -1
    while r != 0:
        # Find remainder of m divided by n.
        r = m % n
        # [Is it zero ? - If yes, the Algo terminates]
        if r == 0 :
            break
        else:
            m = n
            n = r
    
    return n

def replace(a,b,c,d):
    # replace this to (b,c,d,a)
    # i.e - a <- b, b <- c, c <- d & d <- a
    rearranged_list = []
    t = int(a)
    a, b, c, d = b, c, d, t
    rearranged_list.extend((a,b,c,d))
    return rearranged_list

# Find the gcd of 2 numbers.
print(gcd(2166,6099))
print(replace(1,2,3,4))

# Can you find the GCD of multiple numbers ? - Yes, Because GCD is associative ...so GCD(a,b,c) --> GCD(a,GCD(b,c))
# So, i can easily call the above proc multiple times with 2 inputs.
