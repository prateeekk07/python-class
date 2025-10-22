import os
import time

# Function to clear screen (works on Windows/Mac/Linux)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print a decorative border
def print_border():
    print("🌟" * 60)

# Function to display diyas
def print_diyas():
    diyas = [
        "         🪔         ",
        "    🪔         🪔    ",
        "🪔    🪔     🪔    🪔"
    ]
    for line in diyas:
        print(line)
    print()

# Function to animate sparkles
def sparkle_effect():
    clear()
    for _ in range(10):
        print_border()
        print(("✨💥🎆 Happy Diwali 🎆💥✨").center(60))
        print_border()
        time.sleep(0.25)
        clear()

# Function to display the main greeting card
def diwali_card(name):
    clear()
    print_border()
    print("🎇".center(60))
    print("🪔✨  H A P P Y   D I W A L I  ✨🪔".center(60))
    print("🎇".center(60))
    print_border()
    print()
    print_diyas()
    time.sleep(1)
    print(f"Dear {name},".center(60))
    print()
    time.sleep(1)
    print("🌟 May this Diwali bring joy, success, and light to your life! 🌟".center(60))
    time.sleep(1)
    print("💫 Wishing you endless happiness and prosperity ahead 💫".center(60))
    time.sleep(1)
    print()
    print("With warm wishes,".center(60))
    print("🧡 Prateek 🧡".center(60))
    print()
    print_border()
    print("\n💖 Share this light, spread the happiness 💖\n")

# Function to safely get a valid name
def get_valid_name():
    while True:
        try:
            name = input("\nEnter your name: ").strip()
            if not name.isalpha():
                raise ValueError("Invalid name")
            return name.capitalize()
        except ValueError:
            print("⚠️  Please enter a valid name (letters only, no numbers or symbols).")

# Main function
if __name__ == "__main__":
    clear()
    print("🪔 Welcome to the Diwali Wish Card Generator 🪔")
    name = get_valid_name()

    sparkle_effect()
    diwali_card(name)