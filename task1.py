nums = [8, 1, 2, 2, 3]

def kichiklar_soni(nums):
    lst = []
    for i in range(len(nums)):
        count = 0
        for x in range(len(nums)):
            if i != x and nums[i] > nums[x]:
                count += 1
        lst.append(count)
    print(lst)

kichiklar_soni(nums)