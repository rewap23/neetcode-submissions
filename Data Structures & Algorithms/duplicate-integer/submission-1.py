class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # need to use hash sets
        # one way to solve - brute force
        # checking every sinlge element in arrray and return true at the end if any pair has equal values - too inefficient
        seen = set() # creating an empty set to track numbers that have been seen or gone over
        for num in nums:
            if num in seen: # if the number was already in seen set that would mean there is a duplicate integer
                return True
            seen.add(num)
        return False

        