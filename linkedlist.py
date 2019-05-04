

class Counter:
    overall_total = 0
    def __init__(self):
        self.my_total = 0

    def increment(self):
        Counter.overall_total = Counter.overall_total + 1
        self.my_total = self.my_total + 1

if __name__ == '__main__':
    a = Counter()
    b = Counter()

    a.increment()
    b.increment()
    b.increment()

    print(a.my_total)
    a.increment()
    print(b.my_total)
    print(a.__class__.overall_total)