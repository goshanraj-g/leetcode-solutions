class Solution(object):
    def searchMatrix(self, matrix, target):
        l, r = 0, len(matrix) -1
        while l <= r:
            mid = (l+r) // 2
            Ml, Mr = 0, len(matrix[mid]) - 1
            while Ml <= Mr:
                Mmid = (Ml+Mr) // 2
                if matrix[mid][Mmid] == target:
                    return True
                elif matrix[mid][Mmid] > target:
                    Mr = Mmid - 1
                else:
                    Ml = Mmid + 1
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                break
        return False
