from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUserClass(user_number, class_name, topic_name):
    if user_number in dataset:
        if class_name in dataset[user_number]:
            dataset[user_number][class_name].update([topic_name])
        else:
            dataset[user_number][class_name]={topic_name}
    else:
        dataset[user_number] = {class_name: {topic_name}}




print("Task 1")

#Додати нового студента та нову дисципліну
addUserClass('AA № 12345678','Math','')

#Додати існуючому студенту нову дисципліну і нову тему
addUserClass('AA № 12345678','Algebra','matrix')

#Додати існуючому студенту нову тему існуючої дисципліни
addUserClass('AP № 66545774','Biology','anathomy')

print(dataset)


print("\n\n")
