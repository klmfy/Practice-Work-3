a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
list = []
def func(a,b,c):
    if a%2 == 0:
        list.append(a)
        print("Первое число парное, поэтому успешно добавленно в список!\n")
    else:
        print(f"Число {a} в первом номере, не являяется парным.\n")
    if b%2 == 0:
        print("Второе число парное, поэтому успешно добавленно в список!\n")
        list.append(b)
    else:
        print(f"Число {b} во втором номере, не являяется парным.\n")
    if c%2 == 0:
        print("Третье число парное, поэтому успешно добавленно в список!\n")
        list.append(c)
    else:
        print(f"Число {a} в третьем номере, не являяется парным.\n")
    print(f"Текущий список парных числел: {list}")
func(a,b,c)