class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        nums_dict = dict()
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        # Step 1 — Create buckets indexed by frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        # Step 2 — Drop each key into its frequency bucket
        for key, count in nums_dict.items():
            buckets[count].append(key)
        # Step 3 — Walk the buckets from the back (highest frequency) and collect keys
        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for key in buckets[count]:
                result.append(key)
                if len(result) == k:
                    return result
        # return None
        assert False, "unreachable: k exceeds number of unique elements in nums"

    def top_k_frequent_2(self, nums: list[int], k: int) -> list[int]:
        # O(n log(n))
        nums_dict = dict()
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        nums_dict_sorted = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in nums_dict_sorted[:k]]
        return result
