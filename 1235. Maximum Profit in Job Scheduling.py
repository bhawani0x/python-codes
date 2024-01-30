class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """

        li = [list(a) for a in (zip(startTime, endTime, profit))]
        '''
        (1, 3, 20), (2, 5, 20), (3, 10, 100), (4, 6, 70), (6, 9, 60)
        '''
        max_profit = 0
        total_jobs = len(li)
        for count, i in enumerate(li):
            count += 1
            while count != total_jobs:
                c = li[count]
                if c[0] >= i[1]:
                    print(i, c)
                count += 1
        #     for j in li:
        #         if i != j:
        #             if i[1] not in range(j[0]+1, j[1]):
        #                 print(i, j, i[2]+j[2])
        #                 max_profit = max(max_profit, i[2]+j[2])
        #     print(" ")
        # print(max_profit)


s = Solution()
s.jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60])
