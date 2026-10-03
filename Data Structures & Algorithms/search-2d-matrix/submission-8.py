class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1

        while (top <= bottom):
            midrow = top + ((bottom-top) // 2)

            if target < matrix[midrow][0]:
                bottom = midrow-1

            elif target > matrix[midrow][len(matrix[midrow])-1]:
                top = midrow+1


            else: #target can only be in the mid row

                l, r = 0, len(matrix[midrow])-1
                while (l <= r):
                    mid = l + ((r-l) // 2)

                    if (target < matrix[midrow][mid]):
                        r = mid - 1
                    elif (target > matrix[midrow][mid]):
                        l = mid + 1
                    elif (target == matrix[midrow][mid]):
                        return True
                    else:
                        break
                break

        return False