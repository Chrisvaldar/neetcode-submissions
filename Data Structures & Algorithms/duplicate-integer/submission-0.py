class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = []
        for thing in nums:
            if thing not in dupe:
                dupe.append(thing)
            else:
                return True
        return False
        