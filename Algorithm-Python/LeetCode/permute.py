from itertools import permutations


def permute(nums):
    per = permutations(nums, len(nums))
    ans = []
    for i in list(per):
        ans.append(list(i))
    return ans


print(permute([1, 2, 1]))
