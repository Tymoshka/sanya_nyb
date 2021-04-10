# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/


import random
def print_field(my_field):
    print(' _ _ _')
    for i in my_field:
        c = ''
        for b in i:
            c += '|' + b
        print(c + '|')



def make_move(field, move, coo):
    if field[(coo - 1) // 3][(coo - 1) % 3] == "_":
        field[(coo - 1) // 3][(coo - 1) % 3] = move
        return field, True
    else:
        return field, False







data = 'asd asd asd asd asd dsa dsa dsa dsa'
data.lower
dara = data.split(' ')
answer = {}
print(data)
for i in data:
    if i not in answer.keys():
        answer[i] = data.count(i)
print(answer)




