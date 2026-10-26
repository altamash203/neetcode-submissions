class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #util func

        def validator(items):
            seen = []
            for i in items :
                if i == ".":
                    continue
                elif  i not in seen:
                    seen.append(i)
                else: 
                    return False
            return True

        def nested_validator(items):
            for i  in items :
                result = validator(i)
                if result == False:
                    return False
            return True

        
            

        #board flatter util func 
        def flatter(board):
            flat_board = []
            for i in board :
                for j in i: 
                    flat_board.append(j)
            return flat_board

        #squared sub set
        def squared_validator(board):
            flat_board= flatter(board)
            start = [0,3,6,27,30,33,54,57,60] 
            new_set = []
            sub_set = [1,2,9,10,11,18,19,20]
            for  i in start:
                new_set.append(flat_board[i])
                for j in sub_set:
                    new_set.append(flat_board[i + j])
                if validator(new_set) ==False:
                    return False
                new_set = []
            return True

        

        # columns        
        zipped = zip(*board)
        zipped = [list(i)for i in zipped]

        def main ():
            if not nested_validator(zipped):
                return False
            if not nested_validator(board):
                return False
            if not squared_validator(board):
                return False
            return True
            
        return main()

        

        

