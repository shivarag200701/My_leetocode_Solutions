class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set()
        set2 = set()
        for i in nums1:
            if i not in set1:
                set1.add(i)

        for j in nums2:
            if j not in set2:
                set2.add(j)

        intersec = set1.intersection(set2)
        return list(intersec)

        # intersec=[]
        # for i in set1:
        #     if i in set2:
        #         intersec.append(i)

        # return intersec
