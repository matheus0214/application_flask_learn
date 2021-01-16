def say(name, age, *args, **kwargs) -> None:
    print(args)
    print(kwargs)
    print(f"Olá {name} - {age}")
    print("+++++++++++++++++++++++++++++++")


lambda_comprehension = [(lambda value: value ** 2)(value=x) for x in range(10)]
print(lambda_comprehension)

person = ["Matheus", 25]
say(*person)

person2 = {"name": "Jose", "age": 12}
say(**person2)

say("João", 90, "Felipe", "Batata", color="blue")
