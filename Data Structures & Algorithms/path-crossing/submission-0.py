class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # hash map solution
        # O(n) time
        # O(1) space
        # create hash map for moves
        moves = {
            'N': (0,1),
            'S': (0, -1),
            'W': (-1, 0),
            'E': (1, 0)
        }
        visited = {(0,0)}
        x = 0
        y = 0

        for char in path:
            dx, dy = moves[char]
            x += dx
            y += dy
            
            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
        