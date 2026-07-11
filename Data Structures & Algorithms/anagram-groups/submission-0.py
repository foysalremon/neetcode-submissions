from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            ss = "".join(sorted(s))
            groups[ss].append(s)

        return list(groups.values())