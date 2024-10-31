#a for loop repeats code a certain number of times. The big use of this is with data structures (lists, dicts, sets). We will look at this later

#There are several ways that you can do it, but the traditional for loop uses a range function to help

# for loops look like this in other languages
#  fo(int i = 10, i < 10, i = i + i)
# Python does it like this
#  for iterable_valule_name in range(starting_value, ending_value, increment)

number = 5
for i in range(0,number,1):
    print(i)

    #we can also have decrements as well as increments.
    countdown = 0

    #separate both outputs

    print("//////////////////////////////////////////")

    #countdown loop
    for i in range(10,countdown,-1):
        print(i)