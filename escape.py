# scape sequence(special character - single character write with \ ) in Python

# \n - newline
# \t - tab (4 or 8 space by default in py)
# \" content\"  - double quote
#\' content \' - single quote
# \\ forward slash
#\u to create symbol



print("My name is Ahsan I live in Badin I study in laar campus")
print("My name is Ahsan, \n I live in Badin \n I stydu in laar campus") # changing line
print("My name is Ahsan, \t I live in Badin \t I stydu in laar campus") # giving space

print("y name is \"Ahsan\"") # double quote
print("here are the name\"s of vegetable") 
print("My fathes\'s name is Amir ali")
print("My caste is 'Talpur'") # single quote
print('My name is \'Ahsan\'') # if string in single quote then must use forward slash with it otherwise not necessary
print("I love pakistan \\ as well as india")  # forward slash
print("i love in badin / sindh") # backslash

# EXERCISE
print("Hello \nworld")

print("my name is \"Ahsan Raza Talpur\" and my Father\'s name is \"Amir ali\"")

print("what does escape sequence tab \t does")

print("Im printing backslash  / in python ")

print("Name John \nage : 25  \nAddress : 123 , Main Street")

print(r".\n.\t.\".\"\'.\'") # scape sequence does not any affest on raw string

print(" My name is Jake \n i love in Uk \n i am instagram modalist \n i pay abput 2000$ per month rent")

print("\u09Ad")    # it will craete a thumb shape 
print("\u3434")    # \u and then any four number or character can creatw different shapes
print("\uabcd")

print("My name is Ahsan \v I live in badin\b") # \v can craete a copy of forward string
print(" \v My caste is Talpur and \b Im Siraiki")

print("Hello ",end= "" ) # to prevent new line use end= " " after string double quote and concatenation
print("World", end= " ")
print("My dream to be developer")

print("hello\r world") # use  \r to prevent previous 6 letter string

print("Hello\a world") # might beep 
print("hello\bworld") # \b to remove previous character

print("Name\tAge\tClass")
print("Ahsan\t20\t10")
print("Ghani\t21\t11")
print("Zain\t22\t12")

print("Hello\tWorld")
print(r"Hello\tWorld") # raw string doesn't accept any escape sequence (to write r before string to make string raw)





