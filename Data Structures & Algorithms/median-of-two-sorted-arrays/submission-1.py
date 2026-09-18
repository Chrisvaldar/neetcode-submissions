class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        left = 0
        right = len(nums1)
        h = len(nums1) + len(nums2)
        half = (h+ 1)//2

        while left <= right:
            i = (left + right) // 2

            j = half - i
            
            maxTake1 = nums1[i-1] if i > 0 else float('-inf')
            noTake1 = nums1[i] if i < len(nums1) else float('inf')
            maxTake2 = nums2[j-1] if j > 0 else float('-inf')
            noTake2 = nums2[j] if j < len(nums2) else float('inf')

            print(maxTake1, maxTake2)

            if maxTake2 > noTake1:
                left = i + 1
            elif maxTake1 > noTake2:
                right = i - 1
            else:
                if h % 2 == 0:
                    return (max(maxTake1, maxTake2) + min(noTake1, noTake2)) / 2
                else:
                    return max(maxTake1, maxTake2)