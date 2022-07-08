# CREATE A CLASS DOGS WHICH INHERITS PROPERTIES OF PETS AND ANIMALS
class Animals:
    animalType="mammal"
class Pets(Animals):
    color="White"
class Dogs(Pets):
    @staticmethod
    def bark():
        print("Bow bow!")

bruno=Dogs()
bruno.bark()
print(bruno.color)
