class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        l = 0
        seen = set()
        maxLen = 0
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen
