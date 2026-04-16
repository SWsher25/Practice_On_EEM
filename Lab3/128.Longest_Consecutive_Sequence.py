from typing import List


class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		values = set(nums)
		best = 0

		for num in values:
			if num - 1 in values:
				continue

			length = 1
			current = num

			while current + 1 in values:
				current += 1
				length += 1

			if length > best:
				best = length

		return best
