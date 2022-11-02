from pickletools import int4
from re import L


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_list = len(nums)
        midpoint = (int)(len_list/2)
        counter = midpoint
        not_found = True
        while(not_found):
            if(target == nums[midpoint]):
                return midpoint
            if counter == 0:
                return -1
            if(target > nums[midpoint]):
                midpoint = (int)((len_list + midpoint)/2)
                counter = counter - 1
            else:
                len_list = midpoint
                midpoint = (int)(midpoint/2)
                counter = counter - 1



#define Main function to run the test cases:
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    target = 11
    test = Solution.search(Solution, nums, target)
    print(test)