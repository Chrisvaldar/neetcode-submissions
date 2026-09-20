from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        if len(hand) % groupSize != 0:
            return False
            
        count = defaultdict(int)
        for card in hand:
            count[card] += 1
        
        for i in range(len(hand)):
            
            if hand[i] in count and count[hand[i]] > 0:
                count[hand[i]] -= 1
                currGroup = 1
                for _ in range(groupSize - 1):
                    if hand[i] + currGroup in count:
                        count[hand[i] + currGroup] -= 1
                        currGroup += 1
                    else:
                        return False
        return True

