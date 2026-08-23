class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum = []
        add = 0

        for i in range(1, n + 1):
            lst = list(map(int, str(i)))

            for j in range(len(lst)):
                add += lst[j]

            sum.append(add)
            add = 0

        max_count = 0

        for i in range(len(sum)):
            count = sum.count(sum[i])

            if count > max_count:
                max_count = count

        ans = 0
        done = []

        for i in range(len(sum)):
            if sum[i] not in done and sum.count(sum[i]) == max_count:
                ans += 1
                done.append(sum[i])

        return ans