# Classe
class Hero:
  def __init__(self, name, age, heroClass):
    self.name = name
    self.age = age
    self.heroClass = heroClass

  def attack(self):
    if(self.heroClass == "Guerreiro"):
      weapon = "espada"
    elif(self.heroClass == "Mago"):
      weapon = "magia"
    elif(self.heroClass == "Monge"):
      weapon = "bastão"
    elif(self.heroClass == "Ninja"):
      weapon = "shuriken"
    print(f"O {self.heroClass} atacou com {weapon}")

  def defend(self):
    print(f"O {self.heroClass} se defendeu")

  def drink_health_potion(self):
    print(f"O {self.heroClass} bebeu Poção de Cura")

# Objetos
warrior = Hero("Adam", 16, "Guerreiro")
mage = Hero("Harry", 43, "Mago")
ninja = Hero("Naruto", 12, "Ninja")

# Exemplos
warrior.attack()
warrior.defend()
warrior.drink_health_potion()

mage.attack()
mage.defend()
mage.drink_health_potion()

ninja.attack()
ninja.defend()
ninja.drink_health_potion()