from data import dataset




from validators import getUserNumber, getClassName, getTopicsName

from task1 import addUserClass



def addUserProductValidator():
    user_number = getUserNumber()
    while not user_number:
        print("Error. Try again.")
        user_number = getUserNumber()

    user_class = getClassName()
    while not user_number:
        print("Error. Try again.")
        user_class = getClassName()

    user_topic = getTopicsName()
    while not user_number:
        print("Error. Try again.")
        user_topic = getClassName()


print("Task 1")
addUserProductValidator()
print(dataset)


print("\n\n")
