# Pong Game 🏓

This is a simple **Pong Game** implemented in Python using the `turtle` graphics module. The game is a recreation of the classic Pong game where two players control paddles to hit a ball back and forth, and the goal is to score points when the opponent misses the ball.

## Features
* **two-player** mode.
* Simple and intuitive controls.
* Scoreboard to track points.
* Paddle and ball movement with collision detection.
* Game resets and continues after each point.

## Prerequisites
Before you run the game, ensure you have Python installed on your machine along with the `turtle` module (which is built into Python).

### To check Python installation:
```bash
python --version
```

## How to Run
1. Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/pong-game.git
```
2. Navigate into the project directory:
```bash
cd pong-game
```
3. Run the game using Python:
```bash
python main.py
```

## Game Controls
* **Right Paddle** (controlled by the first player):
     Move up: **`Up Arrow`**
     Move down: **`Down Arrow`**
* **Left Paddle** (controlled by the second player):
     Move up: **`w`**
     Move down: **`s`**

## Project Structure
* **`main.py`** - Main game loop and logic.
* **`paddle.py`** - Class to control the ball movement and logic.
* **`scoreboard.py`** - Class for displaying and updating the scoreboard.
* **`ball.py`** - Class to control the ball movement and logic.

## How it Works
1. **Paddle Movement:** Each player controls a paddle on their side of the screen. Players can move their paddle up or down using their respective keys.
2. **Ball Movement:** The ball starts at the center of the screen and moves in a diagonal direction. It bounces off the top and bottom walls. When it collides with a paddle, it bounces back towards the other player.
3. **Scoring:** If a player misses the ball, the opponent scores a point. The game continues with the ball being reset to the center after each point.
  
