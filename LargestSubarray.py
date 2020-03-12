class Solution():
    def __init__(self, array, k):
        self.array = array
        self.k = k

    def largestsubarr(self):
        no = len(self.array) - self.k + 1
        subarr = [self.array[x:x+self.k] for x in range(no)]

        #if integers are not unique
        print(sorted(subarr, key = lambda x: x[:], reverse=True))
        #if every integer is distinct
        #if every integer is distinct probably sorted is not needed.
        #return sorted(subarr, key = lambda x: x[:], reverse=True)[0]

if __name__ == "__main__":
    a = Solution([1,1,1,2,3,4,5,2,6,7,6,2], 7)
    print(a.largestsubarr())
    #What defines "Largest?"
