nums = [1,1,2,2,2,3,3]
nums.sort()
i=0
j=1
while(j<len(nums)):
    if nums[i]!=nums[j]:
        nums[i+1]=nums[j]
        i+=1
    j+=1

print(nums)