class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        l = 0
        arr = [0] * 26
        maxLen = 0
        for r in range(n):
            arr[ord(s[r]) - ord("A")] += 1
            while (r - l + 1) - max(arr) > k:
                arr[ord(s[l]) - ord("A")] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen
