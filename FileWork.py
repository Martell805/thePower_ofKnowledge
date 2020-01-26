def load_inv(file):
    inventory = []
    one_item = '-'
    r_file = open(file, "r", encoding='UTF8')
    while one_item != '':
        one_item = r_file.readline()
        if one_item[len(one_item)-1:len(one_item)]=="\n":
            one_item = one_item[0:-1]
        if one_item != '':
            inventory.append(one_item)
    r_file.close()
    return inventory


class Inv:
    def __init__(self, inv):
        self.items = inv

    def delete_item(self, name):
        for j in range((len(self.items)-1)):
            if self.items[j] == name:
                del self.items[j]

    def add_item(self, name):
        self.items.append(name)

    def get_items(self):
        return self.items


def get_lection(file):
    r_file = open(file, "r", encoding='UTF8')
    num = r_file.read()
    r_file.close()

    r_file = open("lections\\"+num+".txt", "r", encoding='UTF8')
    lec = r_file.read()
    r_file.close()

    return lec


def get_task(file):
    r_file = open(file, "r", encoding='UTF8')
    num = r_file.read()
    r_file.close()

    r_file = open("tasks\\"+num+".txt", "r", encoding='UTF8')
    task = r_file.read()
    r_file.close()

    return task


def get_ad(file):
    r_file = open(file, "r", encoding='UTF8')
    num = r_file.read()
    r_file.close()

    r_file = open("ads\\"+num+".txt", "r", encoding='UTF8')
    ad = r_file.read()
    r_file.close()

    return ad
       
    
if __name__ == '__main__':
    i = Inv(load_inv('inventory.txt'))
    print(i.get_items())
    i.add_item('qwert')
    print(i.get_items())
    i.delete_item('vodka')
    print(i.get_items())
    print('\n\nЗадание:\n------------------------')
    print(get_task("num.txt"))
    print('\n\nДоска:\n------------------------')
    print(get_ad("num.txt"))
    print('\n\nЛекция:\n------------------------')
    print(get_lection("num.txt"))
