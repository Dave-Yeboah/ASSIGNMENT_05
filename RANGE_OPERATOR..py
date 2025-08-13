def calculate_range_odd (num1,num2):
    begin = min(num1,num2)
    stop = max(num1,num2)
    odd_nums = []
    for number in range(begin,stop + 1):
        if number % 2 == 1:
            odd_nums.append(number)
    return odd_nums


def calculate_range_even(num1,num2):
    begin = min(num1,num2)
    stop = max(num1,num2)
    even_nums = []
    for number in range(begin,stop +1):
        if number % 2 == 0:
            even_nums.append(number)
    return even_nums

def calculate_range_sum(num1, num2):
    start = min(num1, num2)
    end = max(num1, num2)
    total = sum(range(start, end + 1))
    return total

def calculate_range_multiple (num1,num2):
    begin = min(num1,num2)
    stop = max (num1,num2)
    import math
    total = math.prod(range(begin,stop + 1))
    return total
print(" ")
print("TWO NUMBERS RANGE OPERATOR")
print("--------------------------")
print(" ")
print("1. Odd numbers between two numbers")
print("2. Even numbers between two numbers")
print("3. Sum of numbers between two numbers")
print("4. Total multiplication of numbers between two numbers")
print("5. Exit")
print(" ")
usr_choice = input("Which one do you wish to start with (ENTER THE CORRESPONDING NUMBER ->) : ")
while usr_choice not in ["1","2","3","4","5"]:
    print("Invalid choice, try again!!!")
    usr_choice = input("please select a choice again ('5' to exit): ")
usr_choice2 = input("Confirm choice: ")
while usr_choice2 in ["1","2","3","4","5"]:
    while usr_choice2 == "1" and usr_choice2 in ["1","2","3","4","5"]:  
        print("ENTER VALUES TO SEE ALL ODD NUMBERS BETWEEN THEM!!!")
        first_num = int(input("Enter your first value: "))
        second_num = int(input("Enter your second value: "))
        odd_numbers = calculate_range_odd(first_num,second_num)
        len_odd_numbers = len(odd_numbers)
        print(f"All odd numbers between {first_num} and {second_num} is: {odd_numbers}")
        print(f"There are {len_odd_numbers} of this in total :)")
        print(" ")
        usr_choice2 = input("please select a choice again ('5' to exit): ")

    while usr_choice2 == "2" and usr_choice2 in ["1","2","3","4","5"]:
        print("ENTER VALUES TO KNOW THE EVEN NUMBERS BETWEEN THOSE VALUES!!!")
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
        even_numbers = calculate_range_even(first_num,second_num)
        len_even_numbers = len(even_numbers)
        print(f"All the even numbers between {first_num} and {second_num} are {even_numbers} ;)")
        print(f"There are {len_even_numbers} of this in total :)")
        print(" ")
        usr_choice2 = input("please select a choice again ('5' to exit): ")
    
    while usr_choice2 == "3" and usr_choice2 in ["1","2","3","4","5"]:
        print("ENTER TWO VALUES TO KNOW THE SUM OF ALL NUMBERS BETWEEN THEM!!!")
        first_num = int(input("Enter the first number: "))
        second_num = int(input("Enter the second number: "))
        sum_of_range = calculate_range_sum(first_num, second_num)
        num_range = []
        min_number = min(first_num,second_num)
        large_number = max(first_num,second_num)

        for number in range(min_number,large_number +1):
            if number % 1 == 0:
                num_range.append(number)
        len_num_range = len(num_range)

        print(f"The sum of all numbers from {min(first_num, second_num)} to {max(first_num, second_num)} is: {sum_of_range}")
        print(f"There are {len_num_range} numbers in this range :)")
        print(" ")
        usr_choice2 = input("please select a choice again ('5' to exit): ")
    
    while usr_choice2 == "4" and usr_choice2 in ["1","2","3","4","5"]:
        print("ENTER TWO VALUES TO KNOW THE MULTIPLICATION OF ALL NUMBERS BETWEEN THEM!!!")
        first_num = int(input("Enter your first value: "))
        second_num = int(input("Enter your second value: "))
        multiplication_result = calculate_range_multiple(first_num,second_num)
        num_range = []
        min_number = min(first_num,second_num)
        large_number = max(first_num,second_num)

        for number in range(min_number,large_number +1):
            if number % 1 == 0:
                num_range.append(number)
        len_num_range = len(num_range)

        print (f"The multiplication of values between {first_num} and {second_num} is: {multiplication_result}")
        print(f"There are {len_num_range} numbers in this range :)")
        print(" ")
        usr_choice2 = input("please select a choice again ('5' to exit): ")

    while usr_choice2 == "5" and usr_choice2 in ["1","2","3","4","5"]:
        import sys
        print("Exiting program...")
        sys.exit()
    
     
    while usr_choice2 not in ["1","2","3","4","5"]:
        print("Invalid choice, try again!!!")
        usr_choice2 = input("please select a choice again ('5' to exit): ")

    





        


    
