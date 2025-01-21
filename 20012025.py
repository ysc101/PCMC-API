import re

sentense="My name and ID is Yogesh Chavan and PRM000101"

pattern=r" and (PRM\d+)"

match=re.search(pattern,sentense)

if match:
    employee_id=match.group(1)
    print("ID is ",employee_id)
else:
    print("Id Not Found")

def Reverse_String():
    str="Mystring"
    rev_str=str[::-1]
    print(rev_str)
Reverse_String()

def Reverse_Number():
    num=123456
    Rev_Num=str(num)[::-1]
    print(Rev_Num)
Reverse_Number()

def factorial_num():
    num=4
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

def misssing_number():
    my_list=[1,2,3,4,5,6,8,9,10,14,16,19,20]
    start=my_list[0]
    end=my_list[-1]
    result=sorted(set(range(start,end+1))-set(my_list))
    print(result)
misssing_number()

def second_Largest():
 numbers = [10, 20, 4, 45, 99, 45]

# Remove duplicates by converting to a set, then sort
 unique_numbers = list(set(numbers))
 unique_numbers.sort()

# The second largest is at the second-to-last position
 if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]
    print("The second largest number is:", second_largest)
 else:
    print("There is no second largest number.")


def duplicates():
    test_my_list=[4,85,96,41,52,4,3,2,3,96]
    seen=set()
    duplicates=set()
    for num in test_my_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(sorted(duplicates))
duplicates()

def Largest_in_list():
    demo_list=[5,96,4,87,23,5,6,4,1]
    Largest=demo_list[0]
    for num in demo_list:
        if num>Largest:
            Largest=num
    print(Largest)
Largest_in_list()

def Is_Palindrome():
    str="radar"
    if str==str[::-1]:
     print()
