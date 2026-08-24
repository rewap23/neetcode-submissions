class Solution:
    def hammingWeight(self, n: int) -> int:
        # bit manipulation
        # O(n) time
        # 0(1) space

        result = 0
        while n != 0:
            result += 1
            n = n & (n-1)
            # decrementing number by 1 so there is one less one each time

        return result

        # AND (&): Compares two bits. It returns 1 only if both bits are 1. Otherwise, it returns 0
        # OR (|): Compares two bits. It returns 1 if at least one of the bits is 1. It returns 0 only if both bits are 0
        # XOR (^): Means "exclusive OR". It returns 1 if the two bits are different (one is 0 and the other is 1). It returns 0 if the bits are the same
        # NOT (~): Flips all the bits. It changes 1 to 0 and 0 to 1
        # Left Shift (<<): Shifts all bits to the left by a set number of spots. It fills the empty spots on the right with zeros
        # Right Shift (>>): Shifts all bits to the right by a set number of spots