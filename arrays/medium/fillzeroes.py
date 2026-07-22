def fillzeroes(matrix):

    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):

        for j in range(m):

            if(matrix[i][j]==0):

                for row in range(m):

                    if(matrix[i][row]!=0):
                        matrix[i][row]=-1

                for col in range(n):

                    if(matrix[col][i] != 0):
                        matrix[col][i] = -1


    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==-1):
                matrix[i][j]=0


    return matrix

matrix=[[1,1,1],[1,0,1],[1,1,1]]

res = fillzeroes(matrix)

print(res)
                
                


    
