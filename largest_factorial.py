def largestFact():
    num = input("Please enter a number")
    mul = 1
    while(num > 1):
        if(num is not 1):
            mul = mul * num
        num -= 1
    print mul
    print len(str(mul))
