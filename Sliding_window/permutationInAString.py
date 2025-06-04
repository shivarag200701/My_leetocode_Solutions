class Solution(object):
    def checkInclusion(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        arr1 = [0] * 26
        arr2 = [0] * 26
        for i in s1:
            arr1[ord(i) - ord("a")] += 1
        print(arr1)
        r = 0
        l = 0
        while r < n2:
            while (r - l + 1) > n1:
                arr2[ord(s2[l]) - ord("a")] -= 1
                l += 1

            arr2[ord(s2[r]) - ord("a")] += 1
            r += 1

            if arr1 == arr2:
                return True

        return False
