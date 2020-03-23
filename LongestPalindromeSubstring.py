class Solution():
    def __init__(self, str):
        self.str = str

    def longest_palindrome(self) -> str:
        if not self.str: return ""

        def ispalindrome(string):
            length = len(string)
            m = length // 2
            return string[:m] == string[:m-1:-1] if length % 2 == 0 else string[:m] == string[:m:-1]

        res, maxlen = "", 0
        for i in range(len(self.str)):
            for j in range(i, len(self.str)):
                if (j-i + 1) > maxlen and ispalindrome(self.str[i:j+1]):
                    res = self.str[i:j+1]
                    maxlen = j-i+1

        return res

    def longest_palindrome2(self) -> str:
        if not self.str: return ""

        res = ""
        for i in range(len(self.str)):
            res = max(self.helper(i,i), self.helper(i,i+1), res, key=len)

        return res


    def helper(self,l,r):

        while 0<=l and r < len(self.str) and self.str[l]==self.str[r]:
                l-=1
                r+=1
        return self.str[l+1:r]


if __name__ == "__main__":
    a = Solution("abcabcbb")
    print(a.longest_palindrome())
    print(a.longest_palindrome2())
