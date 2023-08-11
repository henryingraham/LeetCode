class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        OPEN = '('
        CLOSE = ')'
        
        def gen(combo, open_count, close_count, n, res):
            # we have generated all open and close parens, add combo to result
            if open_count == close_count == n:
                # when n == 0
                if combo != '':
                    res.append(combo)
            # used all opens, must close
            elif open_count == n:
                gen(combo + ')', open_count, close_count + 1, n, res)
            # current pairs all closed, must open before another close
            elif open_count == close_count:
                gen(combo + '(', open_count + 1, close_count, n, res)
            # otherwise, free to open or close
            else:
                gen(combo + '(', open_count + 1, close_count, n, res)
                gen(combo + ')', open_count, close_count + 1, n, res)
  
        res = []
        gen('', 0, 0, n, res)
        return res
            