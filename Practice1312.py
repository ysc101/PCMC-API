def rev_String():
    str="My String"
    reversed_String=str[::-1]
    print(reversed_String)
rev_String()

def Rev_Number():
    num=987654321
    rev_num=str(num)[::-1]
    print(rev_num)
Rev_Number()

def Larget_in_List():
    my_list=[1,25,16,85,96]
    Largest=my_list[0]
    for num in my_list:
       if num > Largest:
        Largest=num
    print(Largest)
Larget_in_List()
        
def List_Larget():
    test_list=[1,85,65,12,74]
    largest=max(test_list)
    print(largest)
List_Larget()
    
def Smallest_in_List():
    our_list=[1,5,95,63,25,41]
    Smallest=our_list[0]
    for num in our_list:
        if num < Smallest:
         num=Smallest
    print("The Smallest Number is :",Smallest)
Smallest_in_List()
            
def List_Smallest():
    Pop_List=[2,45,85,12,65]
    smallest=min(Pop_List)
    print(smallest)
List_Smallest()

