# Logic for controlling units

from game import Action, is_empty, Unit, GameState, build_distance_map

def get_actions(state):
  return [
    Action('move', 'left')
  ]

def get_player_info():
  return {
    "id": "cc9ddc91-2e0d-4565-af30-a39748f2344b",
    "name": "Swamp prawns"
  }

def game_end():
  pass