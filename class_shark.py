class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 0

    def __init__(self,name_p,age_p):
        self.name = name_p
        self.age = age_p

    def set_followers(self, followers):
        self.flowers = followers
        print("This user has " + str(followers) + " followers")

    def muda_nome(self, name_p):
        self.name = name_p

    def deleta(self):
        self.animal_type = ""
        self.location = ""
        self.anima_animal = ""
        self.followers = 0
        self.age = 0
        self.name = ""
        print("Tudo limpo")


new_shark = Shark("Joshi",20)

print(new_shark.name)
print(new_shark.followers)
new_shark.set_followers(5)
print(new_shark.followers)

new_shark.muda_nome("Joao")
print(new_shark.name)

new_shark.deleta()
print(new_shark.name)

