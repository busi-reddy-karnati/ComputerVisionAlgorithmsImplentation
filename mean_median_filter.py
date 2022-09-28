def mean_filter(arr):
    ans = []
    for i in range(1,len(arr)-1):
        temp = []
        for j in range(1,len(arr[0])-1):
            sum = arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i][j-1]+arr[i][j]+arr[i][j+1]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            mean = sum/9
            temp.append(mean)
        ans.append(temp)
    return ans


def median_filter(arr):
    ans = []
    for i in range(1, len(arr) - 1):
        temp = []
        for j in range(1, len(arr[0]) - 1):
            median = sorted([arr[i - 1][j - 1] , arr[i - 1][j] , arr[i - 1][j + 1] , arr[i][j - 1] , arr[i][j] , arr[i][j + 1] , \
                  arr[i + 1][j - 1] , arr[i + 1][j] , arr[i + 1][j + 1]])[4]
            temp.append(median)
        ans.append(temp)
    return ans



image = [[120, 125, 212, 239], [90, 120, 190, 200], [85, 195, 210, 210], [75, 212, 255, 195]]

print(mean_filter(image))
print(median_filter(image))