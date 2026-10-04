# Keyword Arguments:
def greetings(name,greet_msg):
        print(f"{greet_msg}\t{name} ")
        print(f"{name}\t{greet_msg} ")

greetings("vishaal","Welcome")

greetings(greet_msg="Welcome",name="Vishaal")
greetings(name="Vishaal",greet_msg="Welcome")