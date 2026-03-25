class Company:
    __next_id = 1

    def __init__(self):
        self.id = Company.__next_id
        Company.__next_id += 1
        self.name = "ABC"
