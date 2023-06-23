def check(string):
    new_string = string[::-1]
    if string == new_string:
        print(True)
    else:
        print(False)

check("aa")
check("helloworld")
