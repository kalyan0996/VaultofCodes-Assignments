import time
import random

# --- Pet Status and Core Logic (Class-Based) ---

class VirtualPet:
    """
    Manages the pet's attributes (Happiness and Hunger) and handles all game logic 
    like automatic changes, status effects, and game over conditions.
    """
    def __init__(self, name="Fido"):
        # Requirement: Happiness and Hunger levels start at 50 (0-100 range).
        self.name = name
        self.happiness = 50
        self.hunger = 50
        self.age = 0
        self.is_alive = True
        self.message = f"Hello! I am your pet, {self.name}."

    def _clamp_stats(self):
        """Ensures all stats are strictly kept within the 0 to 100 range."""
        self.happiness = max(0, min(100, self.happiness))
        self.hunger = max(0, min(100, self.hunger))

    def _apply_status_effects(self):
        """
        Applies effects based on current levels, specifically the High Hunger Penalty.
        Requirement: If hunger gets too high (>80), happiness decreases.
        """
        # Checks if the high hunger threshold is met (e.g., > 80)
        if self.hunger > 80:
            penalty = 8
            self.happiness -= penalty
            # print(f"🚨 {self.name} is critically hungry (>80)! Happiness decreased by {penalty}.")
            self.message = "I'm starving and sad! Feed me now!"
        elif self.happiness < 20:
            self.message = "I feel neglected... please play with me."
        elif self.hunger < 20:
            self.message = "I am perfectly full and happy!"
        else:
            self.message = "I'm content and waiting for our next activity."
            
        self._clamp_stats()

    def _check_game_over(self):
        """
        Checks for the two Game Over conditions.
        Requirement: Game ends if hunger reaches 100 OR happiness reaches 0.
        """
        if self.happiness <= 0:
            print("\n" + "="*45)
            print(f"💔 GAME OVER! {self.name} became too unhappy (Happiness: {self.happiness}).")
            print("The simulation ends.")
            print("="*45)
            self.is_alive = False
            
        if self.hunger >= 100:
            print("\n" + "="*45)
            print(f"💀 GAME OVER! {self.name} became too hungry (Hunger: {self.hunger}).")
            print("The simulation ends.")
            print("="*45)
            self.is_alive = False

    def _time_passes(self):
        """
        Simulates the passage of time (Automatic Changes).
        Requirement: Hunger gradually increases, and happiness should decrease.
        """
        self.age += 1
        print(f"\n--- A brief moment passes in {self.name}'s life... (Age: {self.age}) ---")
        
        # Gradual automatic changes (simulating need for constant care)
        hunger_increase = random.randint(3, 7)
        happiness_decrease = random.randint(3, 7)
        
        self.hunger += hunger_increase
        self.happiness -= happiness_decrease
        
        print(f"STATS WENT DOWN: Hunger +{hunger_increase}, Happiness -{happiness_decrease}.")
        
        # Check for status effects and critical conditions after changes
        self._apply_status_effects()
        self._check_game_over()


    # --- User Actions (Requirement: Functions for each major action) ---

    def feed(self):
        """
        Feeds the pet.
        Requirement: Decreases hunger but slightly decreases happiness.
        """
        if not self.is_alive: return

        # Action effects
        self.hunger -= random.randint(18, 28) # Decreases hunger significantly
        self.happiness -= 5 # Slightly decreases happiness
        
        print(f"\n[ACTION: FEED] You gave {self.name} a meal.")
        
        # Call time_passes to apply automatic changes and check game over
        self._time_passes()

    def play(self):
        """
        Plays with the pet.
        Requirement: Increases happiness but slightly increases hunger.
        """
        if not self.is_alive: return
        
        # Action effects
        self.happiness += random.randint(18, 28) # Increases happiness significantly
        self.hunger += 5 # Slightly increases hunger
        
        print(f"\n[ACTION: PLAY] You played a fun game with {self.name}.")
        
        # Call time_passes to apply automatic changes and check game over
        self._time_passes()

    def check_status(self):
        """
        Displays the current status of the pet.
        Requirement: Display current hunger and happiness levels.
        """
        print("\n" + "~"*40)
        print(f"STATUS REPORT for {self.name.upper()}:")
        print(f"Happiness: {self.happiness}% " + ("🥳" if self.happiness > 70 else "😐" if self.happiness > 30 else "😞"))
        print(f"Hunger:    {self.hunger}% " + ("😋" if self.hunger < 30 else "😊" if self.hunger < 70 else "🍽"))
        print(f"Mood:      {self.message}")
        print(f"Age:       {self.age} Days Old")
        print("~"*40)


# --- Main Game Loop and Menu ---

def display_menu(pet_name):
    """Prints the action menu to the console."""
    print("\n" + "="*35)
    print(f"What will you do for {pet_name}?")
    print("1. Feed pet (🍽 - Decreases Hunger)")
    print("2. Play with pet (⚽ - Increases Happiness)")
    print("3. Check Status (👀 - Detailed Report)")
    print("4. Quit game (👋)")
    print("="*35)

def main():
    """The main function to run the pet simulator game."""
    print("====================================")
    print("     🐾 VIRTUAL PET SIMULATOR 🐾")
    print("====================================")

    # Get pet name
    pet_name = input("Give your new pet a name: ").strip()
    if not pet_name:
        pet_name = "Pixel"
        print(f"No name given, defaulting to {pet_name}.")
        
    pet = VirtualPet(pet_name)
    pet.check_status()
    
    while pet.is_alive:
        display_menu(pet.name)
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.check_status()
        elif choice == '4':
            print(f"\nThank you for playing! Take care, {pet.name}.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            
        time.sleep(0.5)

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
