'''
There is a collection of videos to place into an empty video album,
one at a time by order of importance. Each time a video is inserted,
all subsequent videos are shifted toward the right by one position.
Given the ids of the videos and the positions where each should be placed,
find out the sequence of videos and the positions where each should be placed.
Find out the sequence of the videos in the album after all videos have been inserted.

Example
n = 5
index = [0,1,2,1,2]
identity = [0,1,2,3,4]
'''
class Solution:
    def videoalbum(self, location, targets) -> int:
        res = []
        for i,j in list(zip(location,targets)):
            res.insert(i,j)
            print(res)

        return res

    def videoalt(self, location, targets) -> int:
        res = []

        for i in range(len(targets)):
            if location[i] == i: res.append(targets[i])
            else:
                end = res[len(res)-1]
                for j in range(location[i], len(res)-1):
                    res[j+1] = res[j]
                res[location[i]] = targets[i]
                res.append(end)

            print(res)

        return res


if "__name__" == "__main__":
    ins = Solution()
    print(ins.MUAS([2,3,4,5]))

first = [0,1,2,1,2]
second = [0,1,2,3,4]
ins = Solution()
print(ins.videoalbum(first, second))
print(ins.videoalt(first, second))
