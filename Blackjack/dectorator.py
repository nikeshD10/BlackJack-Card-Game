def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function.")
        original_func()
        print("Some extra code, after the original function.")
    return wrap_func

#def func_needs_decorator():
 #   print("I want to be decorated.")

#func_needs_decorator()
# Output : I want to be decorated.
#decorated_func = new_decorator(func_needs_decorator)
#decorated_func()


"""
    Output: Some extra code, before the original function.
            I want to be decorated.
            Some extra code, after the original function.
"""
# Note: What can we do instead of setting new "decorated_func" we can generate decorator
#       as @newdecorator
@new_decorator
def func_needs_decorator():
    print("I want to be decorated.")
func_needs_decorator()

# idea about having an function, defining function inside of that function and returning the defined function
def open():
    def choose():
        return "Choose the file from the location"

    return choose
click_open = open()
print(click_open())

