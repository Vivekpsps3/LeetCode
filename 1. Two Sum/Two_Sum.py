class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = len(nums);
        for i in range(x):
            for j in range (x-1):
                if(nums[i]+nums[j+1] == target and i!=j+1):
                    return [i,j+1]

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    test = Solution.twoSum(nums, target)
    print(test)