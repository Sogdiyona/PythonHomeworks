list1=[1,1,2]
list2=[2,3,4]
union= set(list1) & set(list2)

list1_2=[i for i in list1 if i not in union]
list2_2=[i for i in list2 if i not in union]
result=list1_2+list2_2
print(result)
 
print("~"*50)

list1=[1, 2, 3]
list2=[4, 5, 6]
union= set(list1) & set(list2)

list1_2=[i for i in list1 if i not in union]
list2_2=[i for i in list2 if i not in union]
result=list1_2+list2_2
print(result)

print("~"*50)

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
union= set(list1) & set(list2)

list1_2=[i for i in list1 if i not in union]
list2_2=[i for i in list2 if i not in union]
result=list1_2+list2_2
print(result)