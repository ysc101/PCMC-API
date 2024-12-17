#Simple print
print("My name is Yogesh")

#String Reverse Program
def reverse_string():
    str="Yogesh"
    rev_str=str[::-1]
    print(rev_str)
reverse_string()

#Number Reveerse Program
def reverse_number():
    str_num=54321
    rev_num=str(str_num)[::-1]
    print(rev_num)
reverse_number()
    
#LargestinList Method1
def Largestinlist():
   my_list=[1,52,65,85,96]
   larget=max(my_list)
   print(larget)
Largestinlist()

#LargestinList Method2
def Largest_List():
    test_list=[6,12,45,85,54]
    Largest=test_list[0]
    for num in test_list:
       if num>Largest:
         Largest = num
    print(Largest)
Largest_List()

def smallest_list():
    mytestlist=[5,12,6,25,95,35,74]
    smallest=mytestlist[0]
    for num in mytestlist:
       if num<smallest:
         num=smallest
    print(smallest)
smallest_list()

#Find Missing number
def find_missing(numbers):
    for i in range(min(numbers), max(numbers) + 1):
        if i not in numbers:
            return i

# Example usage
input_list = [3, 4, 5, 7, 9]
output = find_missing(input_list)
print(f"The missing number is: {output}")


#Find duplcates
input_list = [3, 4, 5, 7, 9, 5, 8, 9, 10]
duplicates = list({x for x in input_list if input_list.count(x) > 1})
print(f"The duplicates are: {duplicates}")

    