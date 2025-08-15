import tkinter as tk
import random

# --- Main Application Window Setup ---
# Create the main window
window = tk.Tk()
window.title("Guess the Number")
window.geometry("400x300")
window.config(bg="#f0f0f0") # Set a light gray background color

# --- Game Variables ---
# Generate a random number between 1 and 100
target_number = random.randint(1, 100)
# A counter to track the number of guesses
guess_count = 0

def check_guess():
    """
    Function to check the user's guess against the target number.
    This function is called when the 'Guess' button is clicked.
    """
    global guess_count

    try:
        # Get the guess from the input field and convert it to an integer
        guess = int(guess_input.get())
        guess_count += 1
        
        # Check if the guess is within the valid range
        if not 1 <= guess <= 100:
            message_label.config(text="Please enter a number between 1 and 100.", fg="red")
            return

        # Compare the guess to the target number
        if guess < target_number:
            message_label.config(text="Too low! Try again.", fg="orange")
        elif guess > target_number:
            message_label.config(text="Too high! Try again.", fg="orange")
        else:
            # Correct guess, display a success message and disable the game
            message_label.config(text=f"Congratulations! You guessed the number in {guess_count} guesses!", fg="green")
            guess_button.config(state=tk.DISABLED)
            restart_button.pack(pady=10) # Show the restart button

    except ValueError:
        # Handle non-integer input gracefully
        message_label.config(text="Invalid input. Please enter a whole number.", fg="red")
    
    # Clear the input field after each guess
    guess_input.delete(0, tk.END)

def restart_game():
    """
    Resets the game to its initial state.
    """
    global target_number, guess_count
    
    # Generate a new random number
    target_number = random.randint(1, 100)
    # Reset guess count
    guess_count = 0
    
    # Reset the UI elements
    message_label.config(text="I'm thinking of a number between 1 and 100.", fg="gray")
    guess_input.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)
    restart_button.pack_forget() # Hide the restart button
    guess_input.focus() # Set focus to the input field

# --- UI Elements ---
# Frame to center the content
main_frame = tk.Frame(window, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(expand=True)

# Title label
title_label = tk.Label(
    main_frame,
    text="Guess the Number!",
    font=("Arial", 20, "bold"),
    bg="#f0f0f0",
    fg="#333333"
)
title_label.pack(pady=(0, 10))

# Message label to give instructions and feedback
message_label = tk.Label(
    main_frame,
    text="I'm thinking of a number between 1 and 100.",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="gray"
)
message_label.pack(pady=(0, 15))

# Input field for the user's guess
guess_input = tk.Entry(
    main_frame,
    font=("Arial", 14),
    width=15,
    justify="center"
)
guess_input.pack()

# Guess button
guess_button = tk.Button(
    main_frame,
    text="Guess",
    font=("Arial", 12, "bold"),
    bg="#4CAF50", # Green background
    fg="white",
    activebackground="#45a049", # Darker green on click
    command=check_guess
)
guess_button.pack(pady=10)

# Restart button (initially hidden)
restart_button = tk.Button(
    main_frame,
    text="Play Again",
    font=("Arial", 12, "bold"),
    bg="#2196F3", # Blue background
    fg="white",
    activebackground="#0b7dda", # Darker blue on click
    command=restart_game
)

# Start the game by giving the input field focus
guess_input.focus()

# Run the main event loop
window.mainloop()

