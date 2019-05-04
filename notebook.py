import datetime

ID = 1


class note:
    def __init__(self, title, content):
        global ID
        self.id = ID
        ID += 1
        self.title = title
        self.content = content
        self.timestamp = datetime.datetime.now()

    def search(self, pat):
        if pat in self.title or pat in self.content:
            return True
        else:
            return False
    def print_note(self):
        print("ID:", self.id)
        print("Title:", self.title)
        print("Content:", self.content)
        print("Timestamp:", self.timestamp)


notes=[]
n = note("wishes","Hi Good Morning")
#n.print_note()
notes.append(n)
n = note("Class","We have python class")
#n.print_note()
notes.append(n)
n = note("Movie","New movie released, we have to book")
notes.append(n)
n = note("Class","There is no class on Sunday")
notes.append(n)
print(len(notes))
print(notes)
#print(search("class"))
for n in notes:
    if n.search("class"):
        n.print_note()