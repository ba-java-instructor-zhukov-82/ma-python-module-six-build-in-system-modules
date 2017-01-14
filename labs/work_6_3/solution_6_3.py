import sys  # import sys module

print(sys.platform)  # Print computer system platform
print(sys.version)  # print installed computer python version
print(sys.getsizeof('abc'))  # check and print (bytes) size of string object – 'abc'

# n variable should be received as script argument
# n variable default value set as 11 in case of read sys argument fail
try:
    name, n = sys.argv  # Unpack into 2 variables name and n system arguments
except IndexError:
    n = 11  # Set default value

list_variable = list(range(0, int(n)))  # create list variable with number items from 0 to n

# use for loop and write every number item into system stdout flow
# do not use print statement for above task
for item in list_variable:
    sys.stdout.write(str(item) + ' ')  # Write every number item into system stdout flow

# in case of n%2 ==0 exit script execution with n code
if int(n) % 2 == 0:
    sys.exit(n)  # Exit script execution with n code


# PyCharm Terminal:
#
# cd labs/work_6_3
# python3 solution_6_3.py 10
