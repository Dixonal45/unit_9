import dog


class Pack:

    def __init__(self, dog):
        self.dog = dog
        self.members = []
        self.leader_index = 0
        self.members.append(dog)

    def get_leader_name(self):
        leader_dog = self.members[self.leader_index]
        return leader_dog.get_name()
