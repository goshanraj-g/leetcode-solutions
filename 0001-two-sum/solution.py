class Solution(object):
    def twoSum(self, nums, target):
        solution = []
        elementCounter = 0
        numCounter = 0
        for element in nums:
            for num in nums:
                if element + num == target and not (elementCounter == numCounter):
                    solution.append(elementCounter)
                    solution.append(numCounter)
                    return solution
                numCounter += 1
            elementCounter += 1
            numCounter = 0

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        
