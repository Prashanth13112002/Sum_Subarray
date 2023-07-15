class subarray:
    def sumof_subarray_sum (self,array):
        sum1=0
        N=len(array)
        for i in range (N):
            #formumla to find sumofsubarray at a time complexity of o(n)
            sum1+=array[i](i+1)(N-i)
        return sum1
a=list(map(int,input().split()))
a1=subarray()
print(a1.sumof_subarray_sum (a))