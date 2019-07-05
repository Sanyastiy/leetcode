def median_in_two_arrays(arr1, arr2):
    sum1 = 0
    cnt1 = 0
    sum2 = 0
    cnt2 = 0
    for i in arr1:
        sum1 += i
        cnt1 += 1
    for i in arr2:
        sum2 += i
        cnt2 += 1
    return print('median of ', sorted(arr1), ' and ', sorted(arr2), ' equals: ', ((sum1/cnt1)+(sum2/cnt2))/2)


num1 = [4, 3, 6, 7, 3]
num2 = [6, 4, 2, 6, 1]
num3 = [1, 3]
num4 = [2]
num5 = [1, 2]
num6 = [3, 4]

median_in_two_arrays(num1, num2)
median_in_two_arrays(num3, num4)
median_in_two_arrays(num5, num6)
