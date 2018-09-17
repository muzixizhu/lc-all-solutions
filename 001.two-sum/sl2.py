class two_sum(self,nums,target):
    if len(nums)<=1:
        return False
    for i in nums:
        a=target-i
        m=nums.index(i)
        if a in nums:
            try:
                n=nums.index(a,m+1,len(nums))
                return [m,n]
            except:
                continue
