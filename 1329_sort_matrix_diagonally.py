import heapq

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        dict = defaultdict(list)
        for i in range(0, m):
            for j in range(0, n):
                heappush(dict[i-j], mat[i][j])

        for i in range(0, m):
            for j in range(0, n):
                mat[i][j] = heappop(dict[i-j])


        return mat

