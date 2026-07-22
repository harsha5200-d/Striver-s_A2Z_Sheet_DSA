def rot(mat):

    n  = len(mat)
    m = len(mat[0])


    for i in range(n):

        for j in range(m):

            mat[i][j] = mat[j][i]

    res = []
    for i in mat:
       res.append(i[::-1])

    return res



mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = rot(mat)
print(res)