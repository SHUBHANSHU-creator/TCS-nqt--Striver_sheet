from collections import Counter
def frequencySort(nums):
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for i in count:
            freq[count[i]].append(i)
        for i in freq:
            i.sort()
        freq = freq[::-1]
        nums = []
        for ind,i in enumerate(freq):
            for j in i:
                nums += [j for k in range(len(freq) - ind - 1)]
        return nums
nums = [-199,6,7,-199,3,5]
print(frequencySort(nums))