from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        result = []
        used = set()

        for u, i in enumerate(strs):
            if u in used:
                continue

            group = [i]
            used.add(u)

            for v in range(u + 1, len(strs)):
                if v in used:
                    continue

                j = strs[v]

                if len(i) == len(j):
                    ans = True
                    for n in i:
                        if i.count(n) != j.count(n):
                            ans = False
                            break

                    if ans:
                        group.append(j)
                        used.add(v)

            result.append(group)

        return result