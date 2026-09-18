class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set()
        for thing in nums:
            if thing in dupe:
                return True
            dupe.add(thing)
        return False
        