# 🧙‍♂️ Python RPG Battle Game

A simple text-based RPG battle game built in Python where you choose a character class and fight against an evil wizard using attacks, special abilities, and strategy.

---

## 🎮 Features

- Multiple playable character classes:
  - 🛡️ Warrior
  - 🔮 Mage
  - 🏹 Archer
  - ⚔️ Paladin

- Unique abilities for each class
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

2. Save the file (e.g., `game.py`)

3. Run the game:

```bash
python game.py

🎯 Gameplay
Choose your character class
Enter your character name
Battle the Evil Wizard using:
Attack
Special Ability
Heal
View Stats
⚔️ Character Abilities
🛡️ Warrior
Heavy Slash → High damage attack
🔮 Mage
Fireball → Powerful ranged attack
🏹 Archer
Quick Shot → Attacks twice
Evade → Avoid next attack
⚔️ Paladin
Holy Strike → Strong attack
Divine Shield → Blocks next attack
🧙 Enemy: Evil Wizard
Attacks with dark magic
Regenerates health every turn
Slightly randomized attack damage
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
Improve UI (maybe convert to GUI or web app)
Add sound effects or animations
📌 Notes
This is a console-based game (no GUI)
Input is required during gameplay
Random values make each playthrough unique