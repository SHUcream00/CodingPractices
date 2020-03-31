class Solution:
    def meetup(self, arrival, departure) -> int:
        investors = sorted(list(zip(arrival, departure)), key = lambda x: x[1])
        total, days = 0, []

        for i in investors:
            for j in range(i[0], i[1]+1):
                if j not in days:
                    days.append(j)
                    total += 1
                    break
        return total



if "__name__" == "__main__":
    ins = Solution()
    print(ins.MUAS([2,3,4,5]))

arr = [1,2,2,2,2]
dep = [10,2,2,2,2]
ins = Solution()
print(ins.meetup(arr, dep))
