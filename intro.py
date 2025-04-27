print('Hello World')
name = 'Ubaid'
age = 20
print(f'My name is {name} and my age is {age}')
x= 12
y= x
x+=1
l=['head', 1, 1.3]
ly= l
l[0] = 'tale'
print(x,y, l, ly)
#Data Types:
############
#List(Similar to Array):
list_example = [1,2,3,'Four']
print(type(list_example))
############
#Tuple(Similar to List, but Immutable):
tuple_example=(1,2,3,4,5)
print(type(tuple_example))
#Set(Filters out similar values):
set_example={1,2,3,4,4,5}
print(type(set_example))
############
#Dictionary(Key/Value Pairs):
dict_example={'a': 'apple', 'b': 'ball', 'c': 'cat'}
print(type(dict_example))
#################
#################
#  TYPE CASTING  #
#List into Tuple
list1 = [1,2,3,4]
listtuple = tuple(list1)
print(listtuple, type(listtuple) )
################
# String into Int
str_1= '55'
int_1=int(str_1)
print(int_1, type(int_1))
###############
#List into Set:
list_1=[1,2,3,4,5,5,6]
set_1=set(list_1)
print(set_1, type(set_1))
###############
#Dictionary into List:
dict_1={'company':'Ferrari', 'model': 'LaFerrari'}
list_2= list(dict_1.keys())
list_3= list(dict_1.values())
print(list_2, list_3, type(list_2), type(list_3))

