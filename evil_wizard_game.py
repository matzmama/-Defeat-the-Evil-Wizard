import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        low = max(1, self.attack_power - 5)
        high = self.attack_power + 5
        damage = random.randint(low, high)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        amount = random.randint(15, 25)
        old = self.health
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} heals for {self.health - old} health (now {self.health}/{self.max_health}).")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def heavy_slash(self, wizard):
        print(f"{self.name} uses Heavy Slash!")
        damage = random.randint(self.attack_power, self.attack_power + 15)
        wizard.health -= damage
        print(f"It deals {damage} damage!")

    def shield_block(self):
        print(f"{self.name} braces with Shield Block! Reduced damage next turn!")

    def special_ability(self, wizard):
        print("1. Heavy Slash\n2. Shield Block")
        choice = input("Choose ability: ")
        if choice == '1':
            self.heavy_slash(wizard)
        elif choice == '2':
            self.shield_block()
        else:
            print("Invalid ability.")


# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def fireball(self, wizard):
        print(f"{self.name} casts Fireball!")
        damage = random.randint(self.attack_power + 5, self.attack_power + 15)
        wizard.health -= damage
        print(f"Fireball hits for {damage} damage!")

    def lightning_strike(self, wizard):
        print(f"{self.name} casts Lightning Strike!")
        damage = random.randint(self.attack_power + 10, self.attack_power + 20)
        wizard.health -= damage
        print(f"Lightning Strike hits for {damage} damage!")

    def special_ability(self, wizard):
        print("1. Fireball\n2. Lightning Strike")
        choice = input("Choose ability: ")
        if choice == '1':
            self.fireball(wizard)
        elif choice == '2':
            self.lightning_strike(wizard)
        else:
            print("Invalid ability.")


# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)
        self.evading = False

    def quick_shot(self, wizard):
        print(f"{self.name} uses Quick Shot!")
        for _ in range(2):
            self.attack(wizard)

    def evade(self):
        self.evading = True
        print(f"{self.name} prepares to evade the next attack!")

    def special_ability(self, wizard):
        print("1. Quick Shot\n2. Evade")
        choice = input("Choose ability: ")
        if choice == '1':
            self.quick_shot(wizard)
        elif choice == '2':
            self.evade()
        else:
            print("Invalid ability.")


# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=22)
        self.shielded = False

    def holy_strike(self, wizard):
        print(f"{self.name} uses Holy Strike!")
        damage = random.randint(self.attack_power + 5, self.attack_power + 10)
        wizard.health -= damage
        print(f"Holy Strike deals {damage} damage!")

    def divine_shield(self):
        self.shielded = True
        print(f"{self.name} raises a Divine Shield!")

    def special_ability(self, wizard):
        print("1. Holy Strike\n2. Divine Shield")
        choice = input("Choose ability: ")
        if choice == '1':
            self.holy_strike(wizard)
        elif choice == '2':
            self.divine_shield()
        else:
            print("Invalid ability.")


# Evil Wizard class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 3, self.attack_power + 3)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")


# Character selection
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    choice = input("Enter choice: ")
    name = input("Enter your character's name: ")

    if choice == '1':
        return Warrior(name)
    elif choice == '2':
        return Mage(name)
    elif choice == '3':
        return Archer(name)
    elif choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle system
def battle(player, wizard):
    while player.health > 0 and wizard.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Special Ability")
        print("3. Heal")
        print("4. Stats")

        choice = input("Choose action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice.")

        if wizard.health > 0:
            wizard.regenerate()

            if isinstance(player, Archer) and player.evading:
                print(f"{player.name} evades the attack!")
                player.evading = False
            elif isinstance(player, Paladin) and player.shielded:
                print(f"{player.name} blocks the attack!")
                player.shielded = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")

    if wizard.health <= 0:
        print(f"You defeated {wizard.name}! 🎉")
    else:
        print("Game Over 💀")


# Main function
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()