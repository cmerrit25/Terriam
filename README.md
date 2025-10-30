# Terriam RPG

> A solo-player RPG that revolves decisive actions, random encounters, training, and 
> enticing combat.

---
## Over-arching Ideas

Combining the combat system of Pokemon with the exploration and power building/scaling of Terraria.

## Features

- **Game Loop**
- [X] Add a main loop in `game()` that ends on quit or player death.  
  - Print the current situation each turn.  
    - Need to give each class __str__ function.
  - Prompt for an action (fight, train, explore, quit).  
  - Break cleanly on “quit”.

- [X] Handle state updates in one place.  
  - Keep a simple `state` object or dictionary with `player`, `nemesis`, `enemies`, `progress`, etc.  
  - Pass this into your action functions so they can modify it.

- [X] Validate input robustly.  
  - Accept only listed commands, reprompt otherwise.  
  - Optionally allow shortcuts (`f`, `t`, `e`, `q`).

- **Actions (`actions.py`)** 

### `fight()`
- [ ] Decide what can be fought (miniboss or boss).  
- [X] Implement basic combat:
  - Compare speed to determine who attacks first.  
  - Subtract armor from incoming attack damage.  
  - Reduce health accordingly.  
  - Print results each round.  
- [X] End when someone reaches 0 health.  
- [X] Reward XP or loot if the player wins.

### `train()`
- [X] Increment player stats such as health, attack, armor, or speed.          <------ DO THIS NEXT
- [X] Optionally cost time or resources.                                       <------ DO THIS NEXT
- [X] Print progress so the player can see improvement.                        <------ DO THIS NEXT

### `explore()`
- [ ] Randomly generate exploration outcomes:
  - Find gold or items.  
  - Trigger a random fight.  
  - Discover story events or locations.  
- [ ] Use small tables or weighted probabilities for variety.

- **Classes (`classes.py`)**

### Player
- [X] Add base stats (`health`, `attack`, `armor`, `speed`, `xp`, `level`).  
- [X] Add methods such as `take_damage()`, `gain_xp()`, or `level_up()`.  
- [X] Include basic validation for name input.

### Nemesis
- [ ] Store nemesis-specific attributes (motivation, level scaling, or story links).  <------ DO THIS NEXT
- [ ] Tie progression or difficulty increases to nemesis development.                 <------ DO THIS NEXT
` 
### Boss and Minibosses
- [X] Centralize base stats in parent classes (`Boss`, `Miniboss`).  
- [X] Keep multipliers in child classes (`Colossus`, `Vrolux`, `Sentry`, `Reaver`).  
- [ ] Add `name` and `description` attributes for better in-game feedback.

## Game Balance and Data

- [ ] Move base stats and multipliers into a constants file or configuration for easier tuning.  
- [ ] Add randomness and scaling functions in a shared utility module.  
- [ ] Test combat and training loops frequently to balance progression.

## Input and Output

- [X] Validate player and nemesis names (non-empty, reasonable length).  
- [ ] Use consistent prompts and error messages.                                      <------- DO THIS NEXT
- [ ] Print clear feedback for all actions.

## Testing and Debugging

- [ ] Make combat and exploration deterministic with a random seed for testing.  
- [ ] Add print or log statements for key state changes.  
- [ ] Keep modules small and testable.

## Extensibility

- [ ] Plan future systems early (inventory, skills, quests).                          <------- DO THIS NEXT
- [X] Use type hints                    
- [ ] Document each new class or function as it’s added.
