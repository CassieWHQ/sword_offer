class Solution:
    def multiply(self,A):
        B,C,D=[],[1],[1]
        N=len(A)
        for i in range(1,N):
            C.append(C[i-1]*A[i-1])
            D.append(D[i-1]*A[N-i])
        for k in range(0,N):
            B.append(C[k]*D[N-k-1])
        return B

    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1

        people = range(n)
        i = 0
        while len(people) > 1:
            i = (i + m - 1) % len(people)
            people.pop(i)
        return people[0]

    def IsContinuous(self,numbers):
        if not numbers or len(numbers)!=5:
            return False
        zeros = numbers.count(0)
        numbers.sort()
        i,j=zeros,zeros+1
        if not numbers[-1]-numbers[i]<5:
            return False

        while j<len(numbers):
            if numbers[i]==numbers[j]:
                return False
            i+=1
            j+=1

        return True

    def IsContinuous(self, numbers):
        if not numbers or len(numbers) != 5:
            return False
        zeros = numbers.count(0)
        gap = 0
        i, j = zeros, zeros + 1
        n = len(numbers)
        numbers.sort()
        while j < n:
            if numbers[i] == numbers[j]:
                return False
            gap += numbers[j] - numbers[i] - 1
            i = j
            j += 1
            if gap <= zeros:
                return True
            else:
                return False
    # def PrintMinNumber(self,numbers):
    def str_cmp(self,s1,s2):
        str1,str2 = s1+s2,s2+s1
        return cmp(str1,str2)
    def printMinNumber(self,numbers):
        if not numbers:
            return ''
        tmp = map(str,numbers)
        tmp.sort(self.str_cmp)
        return ''.join(tmp)


sol2 = Solution()
print 1,sol2.multiply([1,2,3,4,5])
print 2,sol2.LastRemaining_Solution(5,3)
print 3,sol2.IsContinuous([1,3,2,6,4])