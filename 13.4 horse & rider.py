class Horse():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider():
    def __init__(self, name):
        self.name = name

valeriy = Rider("Валерий Харламов")

emerald = Horse("Изумруд", "мустанг", valeriy)

print(emerald.owner.name)
