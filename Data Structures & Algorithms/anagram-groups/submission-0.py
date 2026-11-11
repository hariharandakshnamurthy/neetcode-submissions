class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x in my_dict:
                my_dict[x].append(strs[i])
            else:
                my_dict[x] = [(strs[i])]

        return list(my_dict.values())
