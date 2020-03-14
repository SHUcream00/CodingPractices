'''
Basic idea to divide and conquer
goal: nlogn

'''
class Array():
    #to be sorted
    def __init__(self, array = []):
        self.array = array

    def mergesort(self, array):

        if len(array) == 1: return array

        mid = len(array) // 2
        left = array[0:mid]
        right = array[mid:]

        self.mergesort(left)
        self.mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1



if __name__ == "__main__":
    array = [4,1,9,16,2,7,8,3]
    a = Array(array)
    a.mergesort(a.array)
    print(a.array)
