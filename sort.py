lst = []  
n = int(input("Enter number of elements : ") )
for i in range(0, n): 
    ele = input()
    lst.append(ele)
def sort(lst):
    lst.sort()
    print(lst)
sort(lst)
