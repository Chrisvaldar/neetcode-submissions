class Solution:
    def encode(self, strs: List[str]) -> str:
        comb = "".join([f"{len(thing)}/{thing}" for thing in strs])
        print(comb)
        return comb
    def decode(self, s: str) -> List[str]:
        res = []
        ptr = 0
        while ptr < len(s):
            num = ""
            while s[ptr] != '/':
                num += s[ptr]
                ptr += 1
            print(num)
            print(ptr)
            num = int(num)
            res.append(s[ptr + 1:ptr + num + 1])
            ptr = ptr +  num + 1
        return res