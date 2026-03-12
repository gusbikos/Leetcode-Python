class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashmap = {}
        array = []
        sorted_nums = sorted(nums)

        for idx, num in enumerate(sorted_nums):
            if num not in hashmap:
                hashmap[num] = idx

        for num in nums:
            array.append(hashmap[num])
        return array