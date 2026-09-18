class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "".join([f"{len(string)}/{string}" for string in strs])
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []

        counter = 0
        while counter < len(s):
            num = ""
            while s[counter] != "/":
                num += s[counter]
                counter += 1
            counter += 1
            curr = ""
            for i in range(int(num)):
                curr += s[counter]
                counter += 1
            res.append(curr)
        return res
