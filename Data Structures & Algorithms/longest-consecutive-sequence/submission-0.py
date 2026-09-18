class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
        
        max_seq = 0
        for thing in num_set:
            if thing - 1 not in num_set:
                seq_len = 1
                while thing + 1 in num_set:
                    seq_len += 1
                    thing += 1
                max_seq = max(max_seq, seq_len)
        
        return max_seq