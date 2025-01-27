import re

sentense="MY Employee ID is PRM000101"

pattern=r"ID is (\w+)"

match=re.search(pattern,sentense)

if match:
    emp_id=match.group(1)
    print(emp_id)
else:
     print("Employee ID is not found")

def is_palindrome():
    str="MYNAME"
    if str==str[::-1]:
        print("String is Palindrome")
    else:
        print("String is not palindrome")
is_palindrome()

def String_Reverse():
  str="Shoaib"
  Rev_str=str[::-1]
  print(Rev_str)
String_Reverse()

def Number_Reverse():
    num=123456
    Rev_Num=str(num)[::-1]
    print(Rev_Num)
Number_Reverse()

def Largest_in_List():
    mylist=[45,12,59,789,12,11,35]
    Largest=mylist[0]
    for num in mylist:
        if num>Largest:
          Largest=num
    print(Largest)
Largest_in_List()

def Largest_in_List():
    List=[45,12,74,85,96,51,11,22,1]
    min_List=min(List)
    print(min_List)
Largest_in_List()

String = 'Hello World'
slice_obj = slice(6,9)
print(String[slice_obj])

my_string = "Hello, World!"
sliced_string = my_string[0:6]  # Extracts 'Hello'
print(sliced_string)

my_string = "Hello, World!"
split_list = my_string.split(",")  # Splits at ', '
print(split_list)

def factorial_num():
    num=5
    if num<0:
        print("Number should be positive")
    elif num==0:
        print(0)
    elif num==1:
        print(1)
    else:
        result=1
        for i in range(2,num+1):
          result*=i
          print(result)
factorial_num()

def missing_number():
    test_list=[1,2,3,6,8,9,11,15]
    start=test_list[0]
    end=test_list[-1]
    result=sorted(set(range(start,end+1))-set(test_list))
    print(result)
missing_number()

def duplicates():
    forlist=[1,3,4,5,9,2,1,5,7,10,11,7,65,45,45]
    seen=set()
    duplicates=set()
    for num in forlist:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(sorted(duplicates))
duplicates()

def String_operations():
    