from collections import defaultdict
from itertools import permutations


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if len(digits) == 0:
        return []
    answer = []
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs",
         "8": "tuv", "9": "wxyz"}

    def recursive(i, curStr):
        if len(curStr) == len(digits):
            answer.append(curStr)
            return

        for c in d[digits[i]]:
            recursive(i+1, curStr+c)
    if digits:
        recursive(0, "")

    return answer
