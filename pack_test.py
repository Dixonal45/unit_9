import pack
import dog

my_dog = dog.Dog("Shamu")
your_dog = dog.Dog("Piper")

my_pack = pack.Pack(my_dog)
print(my_pack.get_leader_name())
my_pack.add_member(your_dog)
my_pack.print_pack()
print(my_pack.new_leader(1))
print(my_pack.get_leader_name())