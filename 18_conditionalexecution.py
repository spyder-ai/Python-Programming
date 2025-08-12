# see we humans also had some conditions
# if it is not raining then we'll go for a walk

# if true_or_not:
#     do_this_if_true

    # conditional execution: the if statement
# if sheep_counter >= 120: # evaluate a test expression
#   sleep_and_dream # execute if test expression is true
#     make_a_bed()
#     take_a_shower()
#     sleep_and_dream()
# feed_the_sheepdogs()
    # Feeding the sheepdogs, however, is always done (i.e., the feed_the_sheepdogs() function is not indented and does not belong to the if block, which means it is always executed.)

    # conditional execution: the if else statement
# if true_or_false_condition:
#     perform_if_condition_true
# else:
#     perform_if_condition_false

    # The if-else statement: more conditional execution
# if the_weather_is_good:
#     go_for_a_walk()
# else:
#     go_to_a_theater()
# have_lunch()
    # No matter if the weather is good or bad, we'll have lunch afterwards (after the walk or after going to the theater).

    # Nested if-else statements
# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()

    # The elif statement
# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()


    # Analyzing code samples

    # Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

    # Choose the larger number
    # way1:
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2

    # way2:
# if number1 > number2: larger_number = number1
# else: larger_number = number2

    # way3:
# largest_number = number1  # temporary variable

# if number2 > largest_number:
#     largest_number = number2

# if number3 > largest_number:
#      largest_number = number3

# Print the result
# print("The larger number is:", larger_number)

# largest_number = -999999999
# number = int(input())
# if number == -1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number
# Go to line 02

    # if else statement problem
# income = float(input("Enter the annual income: "))

# if income <= 85528:
# 	tax = income * 0.18 - 556.02
# 	if tax < 0:
# 	    tax = 0.0
# else:
#     tax = 14839.02 + (0.32*(income - 85528))

# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

    # if-elif-else statement problem
# year = int(input("Enter a year: "))

# if year < 1582:
# 	print("Not within the Gregorian calendar period")
# else:
# 	if year % 4 != 0:
# 		print("Common year")
# 	elif year % 100 != 0:
# 		print("Leap year")
# 	elif year % 400 != 0:
# 		print("Common year")
# 	else:
# 		print("Leap year")

# how does if else work
# x = "1"

# if x == '1':
#     print("one")
# elif x == "1":
#     if int(x) > 1:
#         print("two")
#     elif int(x) < 1:
#         print("three")
#     else:
#         print("four")
# if int(x) == 1:
#     print("five")
# else:
#     print("six")

# see, if condition is like
# if this do this, if this do that, if this do etc.. everything will execute
# if this do that, elif do this, else do this... any one condition will be met hence executed, after execution of elif condition again else condition could execute

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four") 
