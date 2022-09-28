import math


def find_sobels(matrix, pivot):
    ans = []
    for i in range(1,3):
        temp = []
        for j in range(1,3):
            res = (matrix[i-1][j-1]*pivot[0][0])+(matrix[i-1][j]*pivot[0][1])+(matrix[i-1][j+1]*pivot[0][2])+(pivot[1][0]*matrix[i][j-1])+(pivot[1][1]*matrix[i][j])+(pivot[1][2]*matrix[i][j+1])+(pivot[2][0]*matrix[i+1][j-1])+(pivot[2][1]*matrix[i+1][j])+(pivot[2][2]*matrix[i+1][j+1])
            temp.append(res)
        ans.append(temp)
    return ans

matrix = [[120,125,212,239],[90,120,190,200],[85,195,210,210],[75,212,255,195]]
gx = [[-1,0,1],[-2,0,2],[-1,0,1]]
gy = [[1,2,1],[0,0,0],[-1,-2,-1]]
Gx = (find_sobels(matrix, gx))
Gy = (find_sobels(matrix, gy))
ans = []
ans_deg = []
for i in range(0,2):
    temp = []
    temp_deg = []
    for j in range(0,2):
        res = math.sqrt((Gx[i][j]**2)+(Gy[i][j]**2))
        temp.append(res)
        temp_deg.append(math.degrees(math.atan(Gy[i][j]/Gx[i][j]))+90)
    ans.append(temp)
    ans_deg.append(temp_deg)
print(ans)
print(ans_deg)