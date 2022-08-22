# if, else and ifelse statements
# click "kernel" at the top on jupiter to reset the variables "reset and restart"
x=5
if x < 10:
    print('smaller')
if x > 20:
    print('bigger')
    
name = input('Anasse:  ')
handle = open(name, 'x')

a = 35.0
b = 12.50
c = a * b
print(c)

x=5
if x < 10:
    print('smaller')
if x > 20:
    print('bigger')

name = input('who are you? input')
print('welcome', input)

inp = input('Europe floor? ')
usf = int(inp) + 1
print('US floor', usf)

big = max('hello world')
print(big)

x = 5
print('Helllo')

def print_lyrics():
    print('I am a lumberjack, and I am okay')
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x= x + 2
print(x)

x = 5
print('hello')

print('hello 1')
print('hello 2')

a =1
b = 2
if a < b:
    print('a is less than b')
    print('a is definitely less than b')
print('Not sure if a is less than b')

c= 5
d= 4
if c < d:
    print('c is less than d')
else:
    print('c is NOT less than d')
    print("I don't think c is less than d")
print('outside the if block')

# BMI calculator sample, formula input = excel
e= 30
f= 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by more than 10")
else:
    print("e is greater than f")
    
    g = 9
h = 8
if g < h:
    print("g iss less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")
    
name = "YK"
height_m = 2
weight_kg = 110

bmi = weight_kg / (height_m ** 2)
print("bmi:  ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is a overwheight")