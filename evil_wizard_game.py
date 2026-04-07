import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        # damage randomized around attack_power
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


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, wizard):
        # Warrior has a heavy slash
        print(f"{self.name} uses Heavy Slash!")
        bonus = 15
        damage = random.randint(self.attack_power, self.attack_power + bonus)
        wizard.health -= damage
        print(f"It deals {damage} damage!")
        if wizard.health <= 0:
            print(f"{wizard.name} has been defeated!")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, wizard):
        # Mage casts a fireball
        print(f"{self.name} casts Fireball!")
        damage = random.randint(self.attack_power + 5, self.attack_power + 15)
        wizard.health -= damage
        print(f"Fireball hits for {damage} damage!")
        if wizard.health <= 0:
            print(f"{wizard.name} has been defeated!")


# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)
        self.evading = False

    def quick_shot(self, wizard):
        print(f"{self.name} uses Quick Shot! Two arrows fly.")
        for i in range(2):
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
            print("Invalid ability. Turn wasted.")


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
        if wizard.health <= 0:
            print(f"{wizard.name} has been defeated!")

    def divine_shield(self):
        self.shielded = True
        print(f"{self.name} raises a Divine Shield! Next attack will be blocked.")

    def special_ability(self, wizard):
        print("1. Holy Strike\n2. Divine Shield")
        choice = input("Choose ability: ")
        if choice == '1':
            self.holy_strike(wizard)
        elif choice == '2':
            self.divine_shield()
        else:
            print("Invalid ability. Turn wasted.")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        # wizard attack can be slightly variable
        damage = random.randint(self.attack_power - 3, self.attack_power + 3)
        opponent.health -= damage
        print(f"{self.name} hurls dark energy at {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            # handle dodge/shield
            if isinstance(player, Archer) and player.evading:
                print(f"{player.name} evades the attack!")
                player.evading = False
            elif isinstance(player, Paladin) and player.shielded:
                print(f"{player.name} blocks the attack with Divine Shield!")
                player.shielded = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
    elif player.health <= 0:
        print(f"{player.name} was defeated. Game Over.")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
