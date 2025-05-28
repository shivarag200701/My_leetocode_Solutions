class Solution(object):
    def isAnagram(self, s, t):
        map1 = {}  # value : no. of counts
        map2 = {}  # value : no. of counts

        for i in s:
            if i not in map1:
                map1[i] = 1
            else:
                map1[i] += 1

        for j in t:
            if j not in map2:
                map2[j] = 1
            else:
                map2[j] += 1

        if len(map1) != len(map2):
            return False

        for i in map2:
            if i not in map1:
                return False
            if map2[i] != map1[i]:
                return False

        return True
