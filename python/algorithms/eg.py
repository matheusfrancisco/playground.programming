d = {"a": 3}
b = {"a": 1, "b": 2}

print(d)

c = {**b, **d}
e = b | d

print(c)
print(e)

for key, value in b.items():
    print(f"{key} -> {value}")


def decorator(a):
    def dec(func):
        def wrpper():
            print("Before function call")
            func()
            print("After function call")

        return wrpper

    return dec


dec = decorator(1)


@dec
def greet():
    print("Hello, World!")


greet()


def fizzbuzz():
    values = {3: "Fizz", 5: "Buzz"}
    for i in range(1, 101):
        output = ""
        for key, value in values.items():
            if i % key == 0:
                output += value
        print(output)


def fizzbuzz2():
    rules = {3: "Fizz", 5: "Buzz"}
    for i in range(1, 101):
        output = "".join(value for key, value in rules.items() if i % key == 0)
        print(output or i)


fizzbuzz()
