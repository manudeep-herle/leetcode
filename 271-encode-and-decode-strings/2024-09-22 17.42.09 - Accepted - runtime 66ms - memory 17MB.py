class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        l = r = 0
        res = []
        while r < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l: r])
            r += 1
            res.append(s[r: r + length])
            r += length
            l = r
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))