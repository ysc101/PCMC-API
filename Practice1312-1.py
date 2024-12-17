def rev_String():
    str="GANESH"
    reverse_String=str[::-1]
    print(reverse_String)
rev_String()

def Rev_Num():
    num=654321
    rev_num=str(num)[::-1]
    print(rev_num)
Rev_Num()

def find_Largest():
    my_list=[5,48,52,14,996]
    Largest=my_list[0]
    for num in my_list:
        if num > Largest:
            num=Largest
    print(Largest)
find_Largest()

