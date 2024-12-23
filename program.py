def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("Calculator:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice:"))
x = float(input("Enter 1st number:"))
y = float(input("Enter 2nd number:"))

if choice == 1:
    print(add(x,y))
elif choice == 2:
    print(sub(x,y))
elif choice == 3:
    print(mul(x,y))
elif choice == 4:
    print(div(x,y))
else:
    print("Choose the correct option")
