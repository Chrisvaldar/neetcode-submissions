class Solution:
    track = {}
    def encode(self, strs: List[str]) -> str:
        encoded = str(strs)
        self.track[encoded] = strs

        return encoded
    def decode(self, s: str) -> List[str]:
        return self.track[s]