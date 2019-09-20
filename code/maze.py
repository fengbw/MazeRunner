#914. X of a Kind in a Deck of Cards
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dict1 = dict()
        for num in deck:
            dict1[num] = dict1.get(num, 0) + 1
        counts = []
        for value in dict1.values():
            counts.append(value)
        number = counts[0]
        for i in range(len(counts) - 1):
            number = self.gcd(number, counts[i + 1])
        if number > 1:
            return True
        else:
            return False


    def gcd(self, m, n):
        if m < n:
            temp = m
            m = n
            n = temp
        if n == 0:
            return m
        else:
            return self.gcd(n, m % n)

#s = Solution()
#print(s.hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
p = 1
s = "sss" + str(p)
print(s)
