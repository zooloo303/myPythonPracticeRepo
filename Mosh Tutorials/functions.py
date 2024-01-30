def greet_user(first_name, last_name):
    print(f"hello there {first_name} {last_name}")
    print("What's up pardner?")


print("Start")
input_name = input("whats your name?: >")
split_name = input_name.split(" ")
print(split_name)
greet_user(split_name[0], last_name=split_name[1])
print("fin")