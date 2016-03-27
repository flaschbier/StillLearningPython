t = int(raw_input().strip())

def isSorted(array):
    return all(array[i] < array[i+1] for i in xrange(len(array) - 1))

def rotateIt(array):
    array[0], array[1] = array[1], array[0]
    array[1], array[2] = array[2], array[1]

for i in xrange(t):
    N = int(raw_input().strip())
    A = raw_input().split()
    A = map(int, A)
    three_array = []

    for j in xrange(N-2):
        print "inside xrange and j is %d" % j
        three_array = A[j:j+3:]
        print "three_array is"
        print three_array
        if isSorted(three_array):
            print "inside first if"
            if isSorted(A):
                print "inside second if"
                print "YES"
            else:
                print "inside first if's else"
                continue
        else:
            print "inside first else"
            rotateIt(three_array)
            print "three_array is"
            print three_array
            if isSorted(three_array):
                print "inside else's first if"
                if isSorted(A):
                    print "inside else's first if's if"
                    print "YES"
                else:
                    print "inside else's first if's else"
                    continue
            else:
                print "inside second else"
                rotateIt(three_array)
                print "three_array is"
                print three_array
                if isSorted(three_array):
                    print "inside second else"
                    if isSorted(A):
                        print "inside second else's if"
                        print "YES"
                    else:
                        print "inside second else's else"
                        continue
