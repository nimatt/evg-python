# Setup

## Prereqs

* Docker
* Python >= 3.6
* Python package tornado

    ```pip install tornado``` 

## Run server

The game server can be run simply by running a Docker container

```
docker run -it --rm -p 8080:8080 nimatt/evg
```

After running this command you should have the game server running on your machine and the console showing

```
Now listening on: http://[::]:8080
Application started. Press Ctrl+C to shut down.
```

To view game in a browser, go to http://localhost:8080.

Note: the ```--rm``` is so that the container instance is removed when it stops.

# Game rules

Each game is between two players. Each players moving its units, one unit at a time.

## Unit order

Each unit gets one opportunety to perform actions per turn. The order of the units are determined by their location on the playing field. They are ordered top to bottom, left to right.

With a scenario where units are placed like

    ------A---
    ----------
    ---B----C-
    ------D---

The units will move in the order A, B, C, D

## Unit actions

A unit have two types of actions it can perform _move_ and _attack_. Each turn it may perform these two actions once. Both actions are performed in a direction (_up_, _down_, _left_ or _right_). A unit moves one step in the given direction, or performs an attack on the adjacent space in that direction.

Note: An attack will damage any unit occupying that space, friend or foe.

## Dead units

A unit is considered dead when its health reaches 0. The space it occupies is then considered empty.

# Controlling units

The game is played by developing the logic controlling the units. This is done in the file ```player.py```. The file contains a function called ```get_actions``` which should return an array of the actions the unit should perform.

So to only move up the function should return

```python
[ Action('move', 'up') ]
```

To move right and the attack down

```python
[ Action('move', 'right'), Action('attack', 'down') ]
```

It is also possible to attack first and then move

```python
[ Action('attack', 'up'), Action('move', 'left') ]
```

## Game state

To help you decide on what actions to perform, the ```get_actions``` function is given the current game state with the following properties.

<dl>
  <dt>empty_map</dt>
  <dd>Two dimensional list containing indication if a coordinate is empty or occupied (0,0 indicates the top left corner)</dd>
  <dt>floor_map</dt>
  <dd>Two dimensional list containing indication if a coordinate contains floor or wall (0,0 indicates the top left corner)</dd>
  <dt>unit</dt>
  <dd>Information regarding the unit that the function should return actions for</dd>
  <dt>units</dt>
  <dd>All units controlled by the player (including current and dead units)</dd>
  <dt>foes</dt>
  <dd>All units controlled by the advesary (including dead units)</dd>
</dl>

## Helper functions

There exist a few functions designed to make the task of developing the unit control logic a bit easier. These functions can be used freely and in any way you see that can benefit.

## Updating the logic

There is no need to perform any special action to use the new version of the ```player.py```. Just save the file and any changes will be automatically picked up and used.

## Modifying player name

To set a great new team name, just update ```name``` in the ```get_player_info``` function and save the file.

## Game end

A game ends when only one player has units left, or enough rounds have passed. If the game is ended due to sufficient amount of rounds, the player of which the sum of the units health is the highest. If the players units have exactly the same amount of health left, it is considered a draw and no points are awarded. At the end of each game, ```game_end``` is called.

## Testing with additional players

To start a game, you need at least two players registered. To achieve that without having two Python processes it is possible to just register more players using the same address. The easiest way to do this is to run ```.\registerPlayers.ps1``` in PowerShell. This will register 4 players that are controlled by the player on address http://10.0.75.1:9080 which should be your single Python process, if you have not changed any ports and if you have standard settings on Docker.

## Debugging

It is of course possible to attach a debugger to the player code. However, if a breakpoint is hit during action evaluation and actions are not returned within 1 second. The unit will not perform any actions and the turn will pass on to the next unit.