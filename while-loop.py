#loops main goal is to repeat code until you do not want the code to be reapeated

#there are two types of loops

#while loop - is a loop that repeats code beased ona specific condition is broken due to the condition no longer bring met

#for loop - does similar things, but is controlled by a counter. Repeats code a certain number of times or repeats code until it processes a certain amount of data

#in many cases, while loops use flags/sentinel values to break the loop once the flag is no longer true.

#program that will record and calcaultate commsion based on a salary
#while loops are very useful for making menu-based programs.

#flag
keep_going = "y"

print("Enter the following to calculate your sales and commission. When you are done, press N and ENTER to exit. If you would like to enter another sale, press Y and ENTER.")

while keep_going == "y":
    sales = float(input("What is your sales for the day? "))
    com_rate = float(input("What is your commission rate in the form of a decimal? "))
    total_earned = sales * com_rate
    print("You have earned", total_earned, "today.")
    keep_going = input("Do you wish to run the program again? Press Y and ENTER for yes or N and ENTER for no.")

print("Thanks for using our program!")