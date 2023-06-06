class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = 0
        result = ''

        for ch in s:
            if ch.isnumeric():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append(result)
                stack.append(num)
                result = ''
                num = 0
            elif ch == ']':
                count = stack.pop()
                prev = stack.pop()
                result = prev + count * result
            else:
                result += ch
        return result
    
        