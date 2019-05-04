import journaldata


def main():
    print_header()
    run_event_loop()

def print_header():
    print('-----------------------------------')
    print('       JOURNAL APP     ')
    print('-----------------------------------')
    print()

def run_event_loop():

    print("What do you want to do with your journal")
    cmd = None
    journal_name = "default"
    journal_data =  journaldata.load(journal_name)#[] #list
    while cmd != 'X':
        cmd = input("[L]ist entries, [A]dd entries, E[X]it : ")
        cmd = cmd.upper().strip()
        if cmd == 'L':
            list_entries(journal_data)
        elif cmd == 'A':
            add_entries(journal_data)
        elif cmd !='X':
            print("We don't understand the command '{}'".format(cmd))
    print('Done..Good Bye')
    journaldata.save(journal_name,journal_data)

def list_entries(data):
    print("Your journal entries:")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("The [{}] entry is {}".format(idx, entry))

def add_entries(data):
    text = input("Type your entry here : ")
    journaldata.add_entry(text,data)
    #data.append(text)

main()
