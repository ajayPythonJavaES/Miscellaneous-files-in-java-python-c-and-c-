def mulMatrices():
    print "Please enter the dimensions for matrix A:"
    row_a = int(input("Please enter the total number of rows for matrix A: "))
    col_a = int(input("Please enter the total number of columns for matrix A: "))
    
    print "Please enter the dimesions for matrix B:"
    row_b = int(input("Please enter the total number of rows for matrix B: "))
    col_b = int(input("Please enter the total number of column for matrix B: "))

    try:
        if(row_a != row_b or col_a != col_b):
            print "Error: Matrices should be of same dimensions"
        else:
            #matA = [[1,2],[2,3]]
            matA = []
            for i in range(0, row_a):
                t_list = []
                for j in range(0, col_a):            
                    x = int(input("enter the value"))
                    t_list.append(x)
                matA.append(t_list)

            matB = []
            for i in range(0, row_b):
                t_list = []
                for j in range(0, col_b):            
                    x = int(input("enter the value"))
                    t_list.append(x)
                matB.append(t_list)

            #print matB            
            """result_matrix = matA+matB
            print result_matrix"""
            result_matrix = []
            """for i in range(0, row_a):
                t_list = []
                #x = 0
                for j in range(0, col_a):
                    x = x + (matA[i][j]*matB[j][i])
                    #t_list.append(matA[i][j] + matB[i][j])
                    t_list.append(x)
                result_matrix.append(t_list)
            """
            for i in range(0, row_a):
                t_list = []
                x = 0                
                for j in range(0, col_a):
                    for k in range(0, col_a):
                        x = x + matA[i][k]*matB[k][j]
                    t_list.append(x)
                    x = 0
                result_matrix.append(t_list)
            print result_matrix
    except(ArithmeticError):
        print "Error: Arithmetic Exception"



def addMatrices():
    print "Please enter the dimensions for matrix A:"
    row_a = int(input("Please enter the total number of rows for matrix A: "))
    col_a = int(input("Please enter the total number of columns for matrix A: "))
    
    print "Please enter the dimesions for matrix B:"
    row_b = int(input("Please enter the total number of rows for matrix B: "))
    col_b = int(input("Please enter the total number of column for matrix B: "))

    try:
        if(row_a != row_b or col_a != col_b):
            print "Error: Matrices should be of same dimensions"
        else:
            #matA = [[1,2],[2,3]]
            matA = []
            for i in range(0, row_a):
                t_list = []
                for j in range(0, col_a):            
                    x = int(input("enter the value"))
                    t_list.append(x)
                matA.append(t_list)

            matB = []
            for i in range(0, row_b):
                t_list = []
                for j in range(0, col_b):            
                    x = int(input("enter the value"))
                    t_list.append(x)
                matB.append(t_list)

            #print matB            
            """result_matrix = matA+matB
            print result_matrix"""
            result_matrix = []
            for i in range(0, row_a):
                t_list = []
                #x = 0
                for j in range(0, col_a):
                    #x = x + (matA[i][j]*matB[j][i])
                    t_list.append(matA[i][j] + matB[i][j])
                    #t_list.append(x)
                result_matrix.append(t_list)
            print result_matrix
    except(ArithmeticError):
        print "Error: Arithmetic Exception"


def transpose():
    print "Please enter the dimensions for matrix A:"
    row_a = int(input("Please enter the total number of rows for matrix A: "))
    col_a = int(input("Please enter the total number of columns for matrix A: "))
    
    try:
        #matA = [[1,2],[2,3]]
        matA = []
        for i in range(0, row_a):
            t_list = []
            for j in range(0, col_a):            
                x = int(input("enter the value"))
                t_list.append(x)
                matA.append(t_list)

                result_matrix  = []
                for i in range(0, col_a):
                    t_list = []
                    #x = 0
                    for j in range(0, row_a):
                        #x = x + (matA[i][j]*matB[j][i])
                        t_list.append(matA[j][i])
                        #t_list.append(x)
                    result_matrix.append(t_list)
        print result_matrix
    except(Exception):
        print "Super error"


def isIdentical():
    print "Please enter the dimensions for matrix A:"
    row_a = int(input("Please enter the total number of rows for matrix A: "))
    col_a = int(input("Please enter the total number of columns for matrix A: "))

    try:
        for i in range(0,row_a):
            for j in range(0, col_a):
                x = int(input("enter the value"))
                t_list.append(x)
                matA.
