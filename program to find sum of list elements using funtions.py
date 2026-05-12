def list_sum(numbers):
    total=sum(numbers)
    return total
n=int(input("enter number of elements:"))
numbers=[]
for i in range(n):
    num=int(input("enter element:"))
    numbers.append(num)
    result=list_sum(numbers)
    print("sum of list elements is:",result)
    
