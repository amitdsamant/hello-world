import os

def load(name):
    #todo : populate this from the file
    return[]

def save(name, journal_data):

    filename = os.path.abspath(os.path.join('./journals/', name + '.jrl'))
    tempfile=open('journal.py','r')
    print(tempfile.read())
    print("would load from "+filename)

    #fout = open(filename,'w')

def add_entry(text,journal_data):
    journal_data.append(text)
