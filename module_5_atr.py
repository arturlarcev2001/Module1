

class Building:
    total = 0
    def __init__(self):
        Building.total += 1

for i in range(1, 41):
    obj  = Building()
    print(obj.total)


