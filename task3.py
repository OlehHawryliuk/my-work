from data import  dataset
from task2 import addUserProductValidator

#   Написати рекурсивну функцію, що повертає інформацію: номер и сумму топиков.

result = []
def recursionByStudents(user_idents=list(dataset.keys()), result_dict=dict()):
    if user_idents == []:
       return
    else:
        him = user_idents[0]
        result.append(him)
        return recursionByStudents(user_idents[1:])

recursionByStudents()
print(result)

def recursionByTopics(user_number, topics_list, amount_of_topics = 0):
    if topics_list==[]:
        return amount_of_topics
    current_topics_list=dataset[user_number][topics_list[0]]
    amount_of_topics=sum(current_topics_list)
    return recursionByTopics(user_number, topics_list[1:], amount_of_topics)
print()

print("\n\n")
