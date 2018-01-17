def lambda_functionality():
    x = lambda n:n*2
    y = lambda x:x*3
    num = 2
    num = x(num)
    num = x(num)
    x = y(num)
    print x
