def fibo(range_n):
    a = 0
    b = 1
    for i in range(0, range_n):
        c = a + b
        print "Printing line no:",i
        print c
        a = b
        b = c
    print("Executed well")
