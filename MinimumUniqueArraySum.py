'''
[Given]
A sorted array

[Requirement]
return sum of array so that sum of elements is minimum
if some of the elements are not unique, increment them until the array consists
of unique integers.

'''
import timeit

class Solution:
    def MUAS(self, numbers) -> int:
        sum = prev = numbers[0]
        for i in range(1, len(numbers)):
            curr = numbers[i]
            if prev >= curr: curr = prev+1
            sum += curr
            prev = curr

        return sum

    def MUAS2(self, numbers) -> int:
        for i in range(1, len(numbers)):
            if numbers[i-1] >= numbers[i]: numbers[i] = numbers[i-1] +1
        return sum(numbers)

if "__name__" == "__main__":
    ins = Solution()
    print(ins.MUAS([2,3,4,5]))

target = [2,2,2]
ins = Solution()
print(ins.MUAS(target))
print(ins.MUAS2(target))
'''
start = timeit.default_timer()
for _ in range(1,100000):
    ins.MUAS([2,2,4,5])
stop = timeit.default_timer()
print('MUAS 1 Time: ', stop - start)

start2 = timeit.default_timer()
for _ in range(1,100000):
    ins.MUAS2([2,2,4,5])
stop2 = timeit.default_timer()
print('MUAS 2 Time: ', stop2 - start2)
'''
