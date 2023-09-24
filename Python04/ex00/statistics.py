from math import sqrt
from typing import Any

class Stats:

    """
    Class for handling statistical calculations.
    """

    def __init__(self, nums: list[int | float]) -> None:
        """
        Initialises the stats class.

        @return None
        """
        self.nums = nums
        self.sorted_nums = sorted(nums)
        self.size = len(nums)
    
    def getSize(self) -> int:
        """
        Getter for size of nums list.

        @return self.size: size of nums list
        """
        return self.size
    
    def getNums(self) -> list[int | float]:
        """
        Getter for nums list.
        
        @return self.nums: nums list
        """
        return self.nums
    
    def mean(self) -> float:
        """
        Calculate the mean of the numbers in nums list.

        @return mean
        """
        return sum(self.nums) / self.size

    def median(self) -> int | float:
        """
        Calculate the median of the numbers in nums list.

        @return median
        """
        if self.size % 2 == 0: # even
            return (self.sorted_nums[int(self.size / 2)] + self.sorted_nums[int((self.size - 1) / 2)]) / 2
        else: # odd
            return self.sorted_nums[int((self.size - 1) / 2)]
    
    def quartile(self) -> list[int | float]:
        """
        Calculate the upper and lower quartiles of the numbers in nums list.

        @return [lower_quartile, upper_quartile]
        """
        lower_quartile = self.sorted_nums[int((self.size - 1) / 4)]
        upper_quartile = self.sorted_nums[int((self.size - 1) * 3 / 4)]
        return [lower_quartile, upper_quartile]
    
    def variance(self) -> float:
        """
        Calculate the variance of the numbers in nums list.
        
        @return var
        """
        squared_mean = sum([n ** 2 for n in self.nums]) / self.size
        return squared_mean - (self.mean() ** 2)

    def standardDeviation(self) -> float:
        """
        Calculate the standard deviation of the numbers in nums list.

        @return std
        """
        return sqrt(self.variance())

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Function that parses args and kwargs and performs statistical calculations.
    """

    s = Stats([arg for arg in args])

    try:
        assert all([isinstance(elem, (int, float)) for elem in s.getNums()]) is True, "Args must be int or float"
    except AssertionError:
        print("ERROR")
        return

    for key, value in kwargs.items():
        
        if s.getSize() == 0:
            print("ERROR")
            continue

        match value:
            case "mean":
                res = s.mean()
            case "median":
                res = s.median()
            case "quartile":
                res = s.quartile()
            case "var":
                res = s.variance()
            case "std":
                res = s.standardDeviation()
            case _:
                continue

        print(f"{value}: {res}")
