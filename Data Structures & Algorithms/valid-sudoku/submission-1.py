class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = defaultdict(set)
        colmap = defaultdict(set)
        boxmap = defaultdict(set)
        for row in range(len(board)):
            for column in range(len(board[row])):
                value = board[row][column]
                box = (row//3) * 3 + (column//3)
                if value in rowmap[row] or value in colmap[column] or value in boxmap[box]:
                    return False
                elif value == '.':
                    continue
                else:
                    rowmap[row].add(value)
                    colmap[column].add(value)
                    boxmap[box].add(value)
            
        return True
                
                
