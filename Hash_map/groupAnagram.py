class Solution(object):
    def groupAnagrams(self, strs):
        map = {}  # array of 26 entires depicting a-z : array of array containing anagrams

        for str1 in strs:
            entry = [0] * 26
            for char in str1:
                entry[ord(char) - ord("a")] += 1
            key = tuple(entry)
            if key not in map:
                map[key] = [str1]
            else:
                map[key].append(str1)
        # res=[]
        # for i in map:
        #     res.append(map[i])
        # return res

        return list(map.values())
