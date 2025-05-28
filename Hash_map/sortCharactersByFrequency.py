class Solution(object):
    def frequencySort(self, s):
        map1 = {}  # char: no. of occurences
        map2 = {}  # no.of occurences string : list of characters having that occurence
        for i in s:
            if i not in map1:
                map1[i] = 1
            else:
                map1[i] += 1

        for j in map1:
            if int(map1[j]) not in map2:
                map2[int(map1[j])] = [j]
            else:
                map2[int(map1[j])].append(j)
        # print(map2)
        res = ""
        for i in sorted(map2.keys(), reverse=True):
            for char in map2[i]:
                res += char * i
        return res
