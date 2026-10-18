class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []
        for num in numbers: 
            difference = target - num
            if difference in numbers:
                if (difference > num):
                    answer.append(numbers.index(num) + 1)
                    answer.append(numbers.index(difference) + 1)
                    return answer
                elif not (difference > num):
                    answer.append(numbers.index(difference)+1)
                    answer.append(numbers.index(num)+1)
                
        return answer