def reverse_string():
    str="abcde"
    rev_str=str[::-1]
    print(rev_str)
reverse_string()

def Reverse_number():
    num=12345
    rev_num=str(num)[::-1]
    print(rev_num)
Reverse_number()

def Missing_number_list():
    my_list=[1,2,4,5,9,12,15,17,20]
    start=my_list[0]
    end=my_list[-1]
    result=sorted(set(range(start, end+1))-set(my_list))
    print(result)
Missing_number_list()

def Factorial_num():
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
Factorial_num()

def LargestinList():
    My_test_List=[45,85,52,96,112,456,852]
    Largest=My_test_List[0]
    for num in My_test_List:
        if num>Largest:
            Largest=num
    print(Largest)
LargestinList()