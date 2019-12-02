class Dog:

    def __init__(self, name):
        self.name = name
        self.trick_list = []

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name)

    def sit(self):
        self.trick_list.append("sit")
        print(self.name + " sits")

    def ups_truck(self):
        self.trick_list.append("ups truck")
        print(self.name + " scares away the ups truck")

    def surfs_counter(self):
        self.trick_list.append("surfs counter")
        print(self.name + " surfs the counter for leftovers from dinner")

    def print_trick_list(self):
        if self.trick_list
        print(self.trick_list)