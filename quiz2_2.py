#Author:JTI 12/7/21

statement = input("What is your mood?: ")
statement = statement.lower()

if statement == "not":
    print("I am" + statement + ".NOW SCRAM!")
else:
    print("I am not " + statement + ".NOW SCRAM!")
