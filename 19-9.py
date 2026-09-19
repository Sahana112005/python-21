#create dict and key values

"""

d={"1":"10","2":"20","3":"30"}

print(d)

print(type(d))
"""

#access a value using key

"""

d={"1":"10","2":"20","3":"30"}

print(d["2"])



"""
"""

#add new key value


d={"1":"10","2":"20","3":"30"}

d["4"]="40"

print(d)

"""



#update value



"""
d={"1":"10","2":"20","3":"30"}

d["3"]="40"

print(d)



"""




#amstrong or not
"""

n=int(input())
temp=n
armstrong=0
digits=len(str(n))
while temp>0:
    digit=temp%10
    armstrong+=digit**digits
    temp//=10
if n==armstrong:
    print("armstrong")
else:
    print("not")
    
"""

#palindrome
"""
n=input()
reverse=n[::-1]
print(reverse)
if n==reverse:
    print("palindrome")
else:
    print("not paliindrome")

"""
"""

#check perfect num or not

n=int(input())
div_sum= 0
for i in range(1, n):
    if n % i == 0:
        div_sum = div_sum + i
if div_sum == n:
    print(n, "is a Perfect Number")
else:
    print(n, "is NOT a Perfect Number")




"""






















