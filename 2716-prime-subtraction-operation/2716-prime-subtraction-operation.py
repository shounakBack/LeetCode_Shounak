class Solution:
    def primeSubOperation(self, nums):
        max_ele=max(nums)
        sieve=[1]*(max_ele+1)
        sieve[1]=0
        for i in range(2,int(sqrt(max_ele))+1):
            if sieve[i]==1:
                for j in range(i*i,max_ele+1,i):
                    sieve[j]=0
        new_val=1
        i=0
        while i<len(nums):
            n=nums[i]
            prime=n-new_val
            if prime<0:
                return False
            if sieve[prime] or prime==0:
                i+=1
                new_val+=1
            else:
                new_val+=1
        return True
