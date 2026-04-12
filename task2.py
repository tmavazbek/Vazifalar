word = "a123bc34d8ef034"
result = ""

for i in word:
    if i.isalpha():
        result += " "
    else:
        result += i
nums = result.split()
nums = [int(i) for i in nums]
print(len(set(nums)))