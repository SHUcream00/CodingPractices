class Solution():
    def __init__(self, str):
        self.str = str

    def longestsubstring(self):
        seen = {}
        start = maxlen = 0
        for i, j in enumerate(self.str):
            if seen.get(j) != None and seen[j] >= start:
                start = seen.get(j, 0) + 1
            else: maxlen = max(maxlen, i-start+1)
            seen[j] = i

        return maxlen

if __name__ == "__main__":
    a = Solution("abcabcbb")
    print(a.longestsubstring())
