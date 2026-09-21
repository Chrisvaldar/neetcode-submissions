class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefix = [0] * len(boxes)
        ballCount = 0
        for i in range(len(boxes)):
            if i > 0:
                prefix[i] = ballCount + prefix[i - 1]

            if boxes[i] == "1":
                ballCount += 1
        
        
        ballCount = 0
        suffix = [0] *  len(boxes)
        for j in range(len(boxes) - 1, -1, -1):
            if j < len(boxes) - 1:
                suffix[j] = ballCount + suffix[j + 1]

            if boxes[j] == "1":
                ballCount += 1
        
        output = [0] * len(boxes)
        for k in range(len(boxes)):
            output[k] = prefix[k] + suffix[k]
        return output