# 🧙‍♂️ Python RPG Battle Game

A simple text-based RPG battle game built in Python where you choose a character class and fight against an evil wizard using attacks, special abilities, and strategy.

---

## 🎮 Features

- Multiple playable character classes:
  - 🛡️ Warrior
  - 🔮 Mage
  - 🏹 Archer
  - ⚔️ Paladin

- Each class has **two unique abilities**
- Turn-based combat system
- Randomized damage and healing
- Enemy AI (Evil Wizard) with regeneration
- Defensive mechanics:
  - Archer can evade attacks
  - Paladin can block attacks with a shield

---

## 🧱 Project Structure

- `Character` (Base Class)
- `Warrior`, `Mage`, `Archer`, `Paladin` (Player classes)
- `EvilWizard` (Enemy)
- Game functions:
  - `create_character()` → Choose your class
  - `battle()` → Main game loop
  - `main()` → Starts the game

---

## ⚙️ How to Run

1. Make sure you have Python installed (Python 3.x recommended)

2. Save the file as:


evil_wizard_game.py


3. Run the game:

```bash
python evil_wizard_game.py
🎯 How to Play
Choose your character class:
1 = Warrior
2 = Mage
3 = Archer
4 = Paladin
Enter your character name
Each turn you will choose an action:
1. Attack
2. Special Ability
3. Heal
4. View Stats
Special abilities give you powerful or defensive options depending on your class
The Evil Wizard will:
Attack you each turn
Regenerate health automatically
The game ends when:
You defeat the wizard ✅
OR your health reaches 0 ❌
⚔️ Character Abilities
🛡️ Warrior
Heavy Slash → High damage attack
Shield Block → Defensive ability
🔮 Mage
Fireball → Strong attack
Lightning Strike → Very high damage attack
🏹 Archer
Quick Shot → Attacks twice
Evade → Avoid next attack
⚔️ Paladin
Holy Strike → Strong attack
Divine Shield → Blocks next attack
🧙 Enemy: Evil Wizard
Attacks with dark magic
Regenerates health every turn
Uses randomized damage
🧠 Concepts Used
Object-Oriented Programming (OOP)
Inheritance
Polymorphism
Randomization
Game loop logic
User input handling
🚀 Future Improvements
Add more enemies or levels
Introduce inventory/items
Add experience points and leveling system
Improve UI (GUI or web version)
Add sound effects or animations