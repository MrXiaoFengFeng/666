import copy
list1 = ['egon','lili',[1,2]]
# list3 = list1.copy()
# list[0]='EHON'
# list[2][0] = 111


list3 = copy.deepcopy(list1)
print(list1)
print(list3)
 

