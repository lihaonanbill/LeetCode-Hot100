from typing import List

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         # 边界情况：空矩阵或空行
#         if not matrix or not matrix[0]:
#             return False

#         m, n = len(matrix), len(matrix[0])

#         # 把矩阵当作长度为 m*n 的一维有序数组，进行二分搜索
#         left, right = 0, m * n - 1

#         while left <= right:
#             mid = (left + right) // 2

#             # 将一维下标 mid 映射到二维坐标 (r, c)
#             r = mid // n
#             c = mid % n

#             val = matrix[r][c]

#             if val == target:
#                 return True
#             elif val < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return False



# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]:
#             return False
#         m,n=len(matrix), len(matrix[0])

#         left,r=0,m*n-1

#         while l<=r:
#             print("l,r",l,r)
#             mid=(l+r)//2
#             r=mid//n
#             c=mid%n
#             print("mid,r,c",mid,r,c)
#             print("matrix[r][c]",matrix[r][c])
#             if matrix[r][c]==target:
#                 return True
#             elif matrix[r][c]<target:
#                 print("<")
#                 l=mid+1
#                 print("l,r",l,r)
#             else:
#                 r=mid-1
#         return False



# if __name__ == "__main__":
#     matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
#     Solution().searchMatrix(matrix,3)
"""
Docstring for CoreAlgorithmicIdeasAndTechnique.BinarySearch.searchMatrix

核心思路（把二维映射成一维）
题目保证：
        每行从左到右递增
        下一行的第一个数 > 上一行的最后一个数
    这等价于：把整个矩阵按行展开后，是一个严格递增的一维数组，例如：
        [1,3,5,7,10,11,16,20,23,30,34,60]
    所以我们可以在区间 [0,m⋅n−1] 上做二分，并把一维下标 mid 映射回二维坐标：
        row = mid // n
        col = mid % n


        
"""


