class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = []
        even = []

        for i in range(len(nums1)):
            if nums1[i] % 2 != 0:
                odd.append(nums1[i])
            else:
                even.append(nums1[i])

        if len(odd) == 0:
            return True

        mini = min(odd)

        for j in range(len(even)):
            if even[j] < mini:
                return False

        return True