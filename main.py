from typing import List

def twoSum(nums: List[int], target:int) -> List[int]:
  length = len(nums)
  nums.sort()
  answer = []

  for i in range(length):
    for j in range(i+1, length):
      tmp = nums[i] + nums[j]
      if tmp == target:
        answer.append[i]
        answer.append[j]
        return answer