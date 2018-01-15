class Classy(object):
    def __init__(self):
        self.items = []
        self.value_map = {
            "tophat": 2,
            "bowtie": 4,
            "monocle": 5
        }

    def addItem(self, item):
        self.items.append(item)

    def getClassiness(self):
        return sum([self.value_map[item] if  item in self.value_map else 0 for item in self.items])


# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())
