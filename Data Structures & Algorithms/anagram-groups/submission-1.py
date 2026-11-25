class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = dict()
        for curr_str in strs:
            sorted_str = ''.join(sorted(curr_str))
            result_dict.setdefault(sorted_str, []).append(curr_str)
        return list(result_dict.values())
