def calculate_average(numbers):
    try:
        if not numbers:
            return 0
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return 0  # Handle empty list case
    except TypeError:
        return 0 # Handle list with non-numeric values
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_list_with_zero = [1,0,3,4,5]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}")

my_list_with_string = [1,2,"a",4,5]
result = calculate_average(my_list_with_string)
print(f"The average is: {result}") 