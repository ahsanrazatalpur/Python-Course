# Python from apna college
# Python is case sensitive 
# variables and datatypes

# printing output
print("Hello World!");
print('My name is Ahsan Raza');
print("My age is 20 years ");
print("i Live in Badin" , "Im learning Python");
print(20);
print(20 + 25);
print(30 - 15);

#python character set
# A to Z or a to z
# 0 to 9
# -,+,/,*,%,/ ..etc
# whitespace ,newline etc...
# python can process all ASCII and unicode character as part of data or literals

# variables (name of memory location in program)(whom values are change)
name = "Ahsan";
age = 20;
price = 5000.0;
print(name);
print(age);
age1 = age;
print("Age is :",age1);
print(price);
print("My name is ",name ,"My age is ",age , "my poket money is",price);

# operator (symbol to perform any operation)
# 1.Assignment operator (=) which assign value from right to left
# other assignment operator (+=, -=, *=, /= , %=, **= )
num = 10;
num += num; # sum and to store value in same variable
print(num);
num -= num; # minus value and store in same variable
print(num);
num /= num+1; # divide value and store in  same variable
print(num);
num *= num; # multiply value and store in same variable
print(num);
num %= num+1; # modulo value and store in same variable
print(num);
num **= num; # power value and store in same variable
print(num);

# 2.Arithmatic operator (-, +, *, /, %, **, //) 
num1 = 5;
num2 = 3;
print(num1 + num2);
print(num1 - num2);
print(num1 / num2);
print(num1 * num2);
print(num1 % num2); # reminder
print(num1 ** num2); # base and exponent (num1^num2)
# 3.relational operator / comparission operator ( == , !=, <, > , <= , >=) give value true or false
a = 5;
b = 10;
print(a == b) # false
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
# 4. Logical operator (and , or and not  (work in boolean value)
# not (make value opposite true -> false   false -> true)
#not (work in one operand)
print(not True) #false
print(not False) #true
n1 = 4;
n2 = 5;
print(not(n1<n2));
# AND (work on two operand) if both value same than true othewise false
val1 = True;
val2 = True;
print(val1 and val2);
# OR (work on two operand) if one value true than true
val1 = True;
val2 = False;
print(val1 or val2);
# we can also use expression in AND OR NOT operator
numberone = 20;
numbertwo = 30;
print((numberone > numbertwo) or (numberone == numbertwo));

# identifier in python (naming rules)
# identifier can be combination of uppercase , lowercase , digits or an underscore
# An identifier cannot start from digit.
# We can't use special symbol like !, #, @, etc
# Identifier can be of any length  

# funtion to find type of datatype
print(type(name));
print(type(age));
print(type(price));

# datatype in python
# 1.Integer (+ve , -ve or 0 values)
# 2.String (sentense or word or can be store in "" or '' or ''' ''')
name2 = 'Ahsan Raza';
name3 = "Ahsan Raza";
name4 = '''Ahsan raza''';
print(name2);
print(name3);
print(name4);
# 3.Float (ddecimal value eg 4.5 , 67.89 etc)
# 4.Boolean (True and False (first letter must be written in capital))
isAdult = True;
print(isAdult);
print(type(isAdult));
# 5.None (no value)
a = None;
print(None);
print(type(a));

# Keywords (are reserved word)

#sum
number1 = 30;
number2 = 20;
sum = number1 + number2;
print(sum) ;

# comment in python (line of code which compiler ignore)
# single-line comment (# //)
# multi-line comment  """ // """ 

# type conversion  (automatic (convert one type variable to another))
x = 3  # python automatic make int to float
y = 5.0
z = x + y; # 3.0 + 5.0
print(z);

x=int("3")
y = 5.0
z = x + y; # 3 + 5.0
print(z);

x = float("2")
x = int("2")

q = 34;
print(str(a)); # now a is string 

# input in python
myName = input("please enter your name ?")
print("Wellcome Mr,",name)

# inpurt alwaysa string
value = input("Enter any value ?") # the input will be string (ahsan,34,45.6 etc all are convert to string here)
print(type(value),value)

value2=int(input("Please enter any value :")) # we have to type datatype which value we want to axpct
print(type(value2),value2)

myNameis = input("Please enter your name?")
myAgeis = input("please enter your age?")
myMarkis = input("Please enter your marks?")
print("Name :",myNameis)
print("Age :",myAgeis)
print("Marks :",myMarkis)

# practice set
# 1. 
numb1 = int(input("enter first number \n"))
numb2 = int(input("please enter secound number \n"))
sum = numb1 + numb2
print("The sum of two number is :  ",sum)

# 2. area of square   area = side x side
side = int(input("please enter side of square"))
area = side * side
print("Area of square is : ",area)

#3. average of floating no
point1 = float(input("Enter 1st floating point : "))
point2 = float(input("Enter 2nd floting point : "))
average = (point1 + point2)/2
print("average is : ",average)

#4 2 no which is greater
no1 = int(input("please enter number 1 :"))
no2 = int(input("please enter 2 number"))
print(no1 >= no2)
 
