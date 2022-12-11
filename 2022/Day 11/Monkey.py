class Monkey:
    def __init__(self, items, operation, operation_amount, test, test_true, test_false):
        self.items = []
        for i in items:
            self.items.append(i)
        self.operation = operation
        self.operation_amount = operation_amount
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.count = 0

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self):
        return self.items.pop(0)
