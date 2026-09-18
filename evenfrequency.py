"""def find_sum_of_even_frequency(string):
    sum=0
    count=1
    for i in range(1,len(string)):
        if string[i]==string[i-1]:
            count+=1
        else:
            if count%2==0:
                sum+=count
            count=1
    if count%2==0:
        sum+=count
    return sum
input_str=input()
result=find_sum_of_even_frequency(input_str)
print(result)"""
def find_possible_n(a,x):
    possible_values=[]
    for n in range(1,x+1):
        z=x-(a*n)
        if z>0 and n%z==0:
            possible_values.append(n)
        if possible_values:
            print(possible_values)
    else:
        print("none")
a,x=map(int,input().split())
find_possible_n(a,x)
"""MOD=1000000007
def  count_payment_ways(x):
    if x==1:
        return 1
    if x==2:
        return 3
    prev2=1
    prev1=3
    for i in range(3,x+1):
        current=(prev1+prev2)%MOD
        prev2=prev1
        prev1=current
    return prev1
x=int(input())
print(count_payment_ways(x))"""
