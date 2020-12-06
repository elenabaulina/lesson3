a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def degree(a, b):
    if b == 0:
        return("Делить на ноль нельзя!")
    else:
        return a // b
print(a, "/" , b , "=" , degree(a, b))

def info(name, surname, birthday, city, email, phone_number):
    print(f"name - {name}; surname - {surname}; birthday - {birthday}; city - {city}; email - {email}, phone_number - {phone_number}")
info(name = "Максим", surname = "Иванов", birthday = "25 сентября 1988", city = "Москва", email = "ivanov@maks.ru", phone_number = "89263492728")

def my_func(a, b, c):
    r = [a, b, c]
    i = min(r)
    r.remove(i)
    print(sum(r))
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
my_func(a,b,c)

x = int(input("Введите число: "))
y = abs(int(input("Введите степень : ")))
def power(x,y):
    s = x**y
    print("Возведение числа ", x, "в степень ", y, " = ", s)
power(x,y)
def power_2(x,y):
    i = 1
    d = 1
    while i <= y:
        d = d*x
        i+=1
    return(d)
print("Возведение числа ", x, "в степень ", y, " = ", power_2(x,y))



