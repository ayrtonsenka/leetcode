class Solution(object):
    def summaryRanges(self, nums):
        l = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i < len(nums) - 1 and nums[i+1] - nums[i] == 1:
                i+=1
            
            if start != nums[i]:
                l.append(str(start) + '->' + str(nums[i]))
            else:
                l.append(str(nums[i]))
        
            i+=1
        return l
                
        