from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

check = lambda x, y: x[0] == y[0]



def get_advanced_writer(file_name):

    file = open(file_name, "w+")
    def write_everything(*data_set):
        for data in data_set:
            file.write(str(data) + "\n")
        file.close()
    return write_everything


class MysticBall:
    def __init__(self, words):
        self.words = words
    def __call__(self):
        word = choice(self.words)
        return word

write = get_advanced_writer("example.txt")
write("This is a string", ["I", "THINK", "THEREFORE", "I", "AM"])

mystic_ball = MysticBall(["Yes", "Maybe", "No", "Probably Yes", "Probably Not", "Not sure"])
print(mystic_ball())

