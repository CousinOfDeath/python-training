with open("advent_of_code_input.txt") as file_with_numbers:
    int_list = [int(num) for num in file_with_numbers.readlines()]
    print(sum(int_list))
