# LOOPS, CONTROL STATEMENTS DOES NOT FOR A LOCAL SCOPE
a = 1
if a > 3:
    b = True
else:
    b = False

print(b)


def print_a():
    if a > 3:
        c = True
    else:
        c = False
    print(c)


print_a()
print(c)  # SINCE C IS DEFINED IN LOCAL SCOPE OF A FUNCTION, IT CANNOT BE ACCESSED OUTSIDE THE FUNCTION


def modify_a():
    a += 1  # SINCE A IS A GLOBAL VARIABLE, IT CANNOT BE MODIFIED INSIDE THE FUNCTION


def modify_a_():
    global a
    a += 1


modify_a()
modify_a_()


def a_function(a_parameter):
    a_variable = 15
    return a_parameter


a_function(10)
print(a_variable)
