def twoNums(nums,target):
    for i in nums:
        for j in reversed(nums):
            if i + j == target:
                return print('i=',i,' index=',nums.index(i),' j=',j,' index=',nums.index(j))


nums=[1,4,7,5,3,8,0,3,1,3]
target=21
twoNums(nums,target)

