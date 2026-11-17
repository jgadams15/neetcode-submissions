class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = [0] *k
        index = 0
        for num, count, in freq.most_common(k):
            result[index] = num
            index += 1
        return result

