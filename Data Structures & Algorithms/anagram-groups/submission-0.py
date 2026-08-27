class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for s in strs:
            t = list(s)
            t.sort()
            key = "".join(t)

            if key not in hash.keys():
                hash[key] = [s]
            else:
                hash[key].append(s)
                
        return list(hash.values())