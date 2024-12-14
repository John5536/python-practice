age = 42


if age < 13:
    print("Child")
elif age < 20:
    print ("teenager")
else:
    print ("adult")

#for loops

for ages in range(5):
    print(ages)

# list 
fruits = ["banana", "cherry", "apple"]
print(fruits)
fruits.append("date")
print(fruits)

#dictionary
student = {
    "name":"Adrian",
    "age":20,
    "coursers": ["math", "Sciences"]
}
print(student["name"])
#functions
def say_goodbye():
    print("Goodbye")
say_goodbye()

#concatenate
print("Hello my name is " + str(name) + "and I have" + age + "old")