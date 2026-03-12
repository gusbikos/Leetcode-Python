class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        count = 1

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
                if hash_map[num] > 1:
                    return True
            else:
                hash_map[num] = count
        return False