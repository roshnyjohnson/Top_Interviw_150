class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),           (0,1),
            (1,-1),  (1,0),  (1,1)
        ]

        # First pass: apply encoding
        for i in range(m):
            for j in range(n):

                live_neighbors = 0

                # Count live neighbors
                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < m and 0 <= nj < n:
                        if abs(board[ni][nj]) == 1:
                            live_neighbors += 1

                # Apply rules using encoding
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1   # Alive → Dead
                else:
                    if live_neighbors == 3 :
                        board[i][j] = 2    # Dead → Alive

        # Second pass: finalize board
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
