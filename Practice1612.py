def missing_number_list():
    My_list = [1, 2, 4, 5, 6, 7, 8, 9, 11]  # Example list with missing numbers
    start = My_list[0]
    end = My_list[-1]

    # Find missing numbers
    result = sorted(set(range(start, end + 1)) - set(My_list))
    print(result)

# Call the function
missing_number_list()


