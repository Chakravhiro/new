N=int(input())
K=int(input())
n=input()
sum=0
list=n.split(",")
for i in range(0,K,1):
	sum=sum+int(list[i])
print(sum)
