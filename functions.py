def reverseLang(self):
    print("Hello")


def objToList(list):
    index = 0
    newList = []
    #print(list)
    for row in list:
        newList.append(row[1])
        #print(row)
        index = index + 1

    return newList