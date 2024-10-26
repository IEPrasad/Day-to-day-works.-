nums = [2, 7, 11, 15]
n = len(nums)
# print(n)

for i in range(n):
  for j in range(1,(n)):
    if nums[i] != nums[j]: 
      x = nums[i] ,nums[j]
      print(x)
 
