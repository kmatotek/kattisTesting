import string

class Solution:

     # @return a list of strings
    def generateAbbreviations(self, word):
        result = []

        def dfs(index=0, s=[]):
            if index == len(word):
                result.append(''.join(s))
                return

            # 1. use the letter
            dfs(index+1, s + [word[index]])

            # 2. abbreviate the letter by a number
            count = 2
            while index + count <= len(word):
                dfs(index + count, s + ['%d' % count])
                count += 1

        dfs()
        return result