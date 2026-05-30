from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(starts, visited):
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        pac_starts = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        atl_starts = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]

        for r, c in pac_starts:
            pacific[r][c] = True
        for r, c in atl_starts:
            atlantic[r][c] = True

        bfs(pac_starts, pacific)
        bfs(atl_starts, atlantic)

        res: List[List[int]] = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res
