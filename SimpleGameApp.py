# Munteanu George Ciprian
# proiect recuperare laborator 2024 MAP
# IFR anul 2, sgr 2

from tkinter import *
from tkinter import messagebox
import random
import threading
import time

# Initialize the application
app = Tk()
app.title("Game App")
app.geometry("400x200")  # Initial small size

# Create a canvas for the squares later
canvas = None
player_square = None
enemy_square = None
player_x, player_y = 50, 50  # Initial position (x, y) of player
enemy_x, enemy_y = 400, 300  # Initial position (x, y) of enemy
player_square_size = 10  # Initial size of the player square
enemy_square_size = 20  # Initial size of the enemy square
red_square_size = 10  # Initial size of the red squares
red_squares = []  # List to store red square data (coordinates and canvas ID)
enemy_running = True  # Flag to control the enemy's movement
move_interval = 0.2  # Enemy movement interval
player_name = ""  # Store the player's name

# Function to reset the game to the initial screen
def reset_game():
    global player_square, enemy_square, player_x, player_y, enemy_x, enemy_y
    global player_square_size, enemy_square_size, red_squares, enemy_running

    # Stop enemy thread
    enemy_running = False

    # Reset variables
    player_x, player_y = 50, 50
    enemy_x, enemy_y = 400, 300
    player_square_size = 10
    enemy_square_size = 20
    red_squares = []

    # Clear the canvas
    if canvas:
        canvas.pack_forget()

    # Show the initial screen
    input_frame.pack(pady=20)
    app.geometry("400x200")  # Reset the window size

# Function to handle game over
def game_over(winner):
    global player_name

    # Stop enemy movement
    global enemy_running
    enemy_running = False

    # Display message box
    if winner == "player":
        messagebox.showinfo("Game Over", f"Congratulations {player_name}, you won!")
    else:
        messagebox.showinfo("Game Over", f"You lost, better luck next time {player_name}!")

    # Reset the game
    reset_game()

# Function to move the player square
def move_square(event):
    global player_x, player_y
    if event.keysym == "Up" and player_y > 0:
        player_y -= 5  # Move up
    elif event.keysym == "Down" and player_y < 600 - player_square_size:
        player_y += 5  # Move down
    elif event.keysym == "Left" and player_x > 0:
        player_x -= 5  # Move left
    elif event.keysym == "Right" and player_x < 800 - player_square_size:
        player_x += 5  # Move right

    # Update player square position
    canvas.coords(player_square, player_x, player_y, player_x + player_square_size, player_y + player_square_size)

    # Check for collision with red squares
    check_collision(player=True)

# Function to create random red squares
def create_random_squares():
    global red_squares
    num_squares = random.randint(15, 50)  # Random number of squares
    for _ in range(num_squares):
        # Generate random position
        x = random.randint(0, 800 - red_square_size)
        y = random.randint(0, 600 - red_square_size)
        # Draw a red square
        square_id = canvas.create_rectangle(
            x, y, x + red_square_size, y + red_square_size, fill="red", outline=""
        )
        red_squares.append((x, y, x + red_square_size, y + red_square_size, square_id))

# Function to check for collision
def check_collision(player=False):
    global player_square, red_squares, player_x, player_y, player_square_size
    global enemy_square, enemy_x, enemy_y, enemy_square_size

    # Determine the active square (player or enemy)
    if player:
        square_coords = (player_x, player_y, player_x + player_square_size, player_y + player_square_size)
        square_size = player_square_size
    else:
        square_coords = (enemy_x, enemy_y, enemy_x + enemy_square_size, enemy_y + enemy_square_size)
        square_size = enemy_square_size

    # Check collision with red squares
    for square in red_squares:
        x1, y1, x2, y2, square_id = square
        if (
            square_coords[2] > x1 and square_coords[0] < x2 and
            square_coords[3] > y1 and square_coords[1] < y2
        ):
            # Collision detected
            canvas.delete(square_id)  # Remove the red square
            red_squares.remove(square)  # Update the red_squares list

            # Grow the active square
            size_increase = (x2 - x1)
            if player:
                player_square_size += size_increase
                canvas.coords(player_square, player_x, player_y, player_x + player_square_size, player_y + player_square_size)
            else:
                enemy_square_size += size_increase
                canvas.coords(enemy_square, enemy_x, enemy_y, enemy_x + enemy_square_size, enemy_y + enemy_square_size)
            break

    # Check collision between player and enemy
    if player and (
        player_x + player_square_size > enemy_x and player_x < enemy_x + enemy_square_size and
        player_y + player_square_size > enemy_y and player_y < enemy_y + enemy_square_size
    ):
        if player_square_size <= enemy_square_size:
            game_over(winner="enemy")  # Player loses
        else:
            game_over(winner="player")  # Player wins

# Function to move the enemy square randomly
def move_enemy():
    global enemy_x, enemy_y, enemy_running

    directions = ["Up", "Down", "Left", "Right"]

    while enemy_running:
        direction = random.choice(directions)

        if direction == "Up" and enemy_y > 0:
            enemy_y -= 25
        elif direction == "Down" and enemy_y < 600 - enemy_square_size:
            enemy_y += 25
        elif direction == "Left" and enemy_x > 0:
            enemy_x -= 25
        elif direction == "Right" and enemy_x < 800 - enemy_square_size:
            enemy_x += 25

        # Update enemy position
        canvas.coords(enemy_square, enemy_x, enemy_y, enemy_x + enemy_square_size, enemy_y + enemy_square_size)

        # Check for collision
        check_collision(player=False)

        # Wait for the next move
        time.sleep(move_interval)

# Function to start the game
def start_game():
    global canvas, player_square, enemy_square, enemy_running, player_name
    player_name = name_entry.get()

    # Expand the window
    app.geometry("810x610")
    
    # Hide the input layout
    input_frame.pack_forget()

    # Create a canvas to draw the squares
    canvas = Canvas(app, width=800, height=600, bg="white")
    canvas.pack()

    # Create the player's square
    player_square = canvas.create_rectangle(
        player_x, player_y, player_x + player_square_size, player_y + player_square_size, fill="blue"
    )

    # Create the enemy square
    enemy_square = canvas.create_rectangle(
        enemy_x, enemy_y, enemy_x + enemy_square_size, enemy_y + enemy_square_size, fill="black"
    )

    # Create random red squares
    create_random_squares()

    # Bind arrow keys to move the player square
    app.bind("<Up>", move_square)
    app.bind("<Down>", move_square)
    app.bind("<Left>", move_square)
    app.bind("<Right>", move_square)

    # Start the enemy movement in a separate thread
    enemy_running = True
    enemy_thread = threading.Thread(target=move_enemy, daemon=True)
    enemy_thread.start()

# Layout for the input
input_frame = Frame(app)
input_frame.pack(pady=20)

Label(input_frame, justify="center", text="Insert name: ", font=('Arial', 14), wraplength=400,).grid(row=0, column=0)
name_entry = Entry(input_frame, font=('Arial', 14), justify="center")
name_entry.grid(row=5, column=0, padx=10)
l2 = Label(
    input_frame,
    text="Game purpose is to eat all squares, take care not to be eaten by the black square. If it get's begger than you, it will eat you!",
    wraplength=400,  # Face wrap text to window size
    justify="center",  # Aliniament
    font=("Arial", 12),
    )
l2.grid(row=8)

Button(input_frame, text="Start Game!", font=('Arial', 14), command=start_game).grid(row=9, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
app.mainloop()
