from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainL = strs
        targetW = ""
        out = []

        groups = {}

        for word in mainL:
            targetW = "".join(sorted(word))
            if targetW not in groups:
                groups[targetW] = []
            groups[targetW].append(word)

        for group in groups.values():
            out.append(group)

        return out