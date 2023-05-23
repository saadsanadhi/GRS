import matplotlib
import matplotlib.plot as plt
matplotlib.use('TkAgg')
import math
def linear_search(list1,n,key):
    for i in range(0,n+1):
        if (list1[i]==key):
            return i
    return -1
thevalues=[70,50,40,20,5,]
target=int(input("enter key to search"))
tmp=linear_search(thevalues,len(thevalues)-1,target)
if tmp==-1:
    print("target value not found")
else:
    print("target value found in list at location:",tmp)
x=list(range(1,10000))
plt.plot(x,x)
plt.title("linear search-time complexity is 0 (log n)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
