def print_if_true(numbers, check_valid):
  for number in numbers:
    if check_valid(number):
      print(number)

numbers = [1, 2, 3, 4, 55, 5, 66, 77, 8]
check_odd = lambda num: (num % 2) != 0

print_if_true(numbers, check_odd)