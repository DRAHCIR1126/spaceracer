# SpaceRacer 

Control the spaceship, collect stars to increase your score, and avoid getting hit by the enemy or the walls. You have 3 lives, so try to survive for as long as possible!

## Features

- **Spaceship controls:** Rotate and move around the arena using the keyboard.
- **Collect stars:** Collect stars that appear for a limited time around the map to increase your score.
- **Enemy AI:** An enemy ship home on the player's position.
- **Collision detection:** Collisions with the enemy or arena boundaries cost a life.
- **Game over and restart:** Start a new game when you run out of lives.

## Controls

| Key | Action |
|---|---|
| `←` / `A` | Turn left |
| `→` / `D` | Turn right |
| `↑` / `W` | Increase speed |
| `↓` / `S` | Decrease speed |
| `Y` | Restart after game over |
| `N` | Exit after game over |

## Requirements

- Python 3
- Turtle
- Playsound3

## How to Run

1. Clone or download this repository.
2. Install the required package and corresponding graphic and sound effects:

   ```bash
   pip install playsound3
   ```

3. Make sure the `images` and `sounds` folders are in the same directory as the Python script.
4. Run the game:

   ```bash
   python main.py
   ```
## Assets

The game uses images for the spaceship, enemy, star, and background, along with WAV files for sound effects. These are stored in the `images` and `sounds` folders.
The game uses graphics and sound effects from external sources, including:

[Space Shooter Extension](https://opengameart.org/content/space-shooter-extension-250)

[Simple Space] (https://opengameart.org/content/simple-space)

The assets are organised into the images and sounds folders.

Credit is given to the original creators. Please refer to each source for its licence and attribution requirements.
## Built With

- Python
- Turtle Graphics
- `playsound3`
