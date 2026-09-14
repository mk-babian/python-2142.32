def func(name, last_name, reverse = True):
    if reverse == True:
        return last_name, name
    else:
        return name, last_name

print(func("Hello", "World"))
