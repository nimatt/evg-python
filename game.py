from typing import List

def build_distance_map(zero_x: int, zero_y: int, floor_map: list):
  dist_map = [[None for y in range(len(floor_map[0]))] for x in range(len(floor_map))]
  def set_distance(x: int, y: int, floor_map: list, distance: int):
    if not floor_map[x][y] or (dist_map[x][y] != None and dist_map[x][y] <= distance):
      return

    dist_map[x][y] = distance
    if x > 0:
      set_distance(x - 1, y, floor_map, distance + 1)
    if x < len(floor_map) - 1:
      set_distance(x + 1, y, floor_map, distance + 1)
    if y > 0:
      set_distance(x, y - 1, floor_map, distance + 1)
    if y < len(floor_map[0]) - 1:
      set_distance(x, y + 1, floor_map, distance + 1)
  
  set_distance(zero_x, zero_y, floor_map, 0)
  return dist_map

class Unit:
  def __init__(self, input_unit):
    self.id: str = input_unit['id']
    self.power: int = input_unit['power']
    self.health: int = input_unit['health']
    self.x: int = input_unit['x']
    self.y: int = input_unit['y']
    self.dist_map: List[List[int]] = None

  def get_distance(self, x: int, y: int, state):
    if self.dist_map == None:
      unit_empty_map = [[square for square in col] for col in state.floor_map]
      if self.id != state.unit.id:
        unit_empty_map[self.x][self.y] = True
        unit_empty_map[state.unit.x][state.unit.y] = False
      self.dist_map = build_distance_map(self.x, self.y, unit_empty_map)

    return self.dist_map[x][y]

class GameState:
  def __init__(self, input_state):
    self.unit = Unit(input_state['unit'])
    self.units: List[Unit] = [Unit(u) for u in input_state['units']]
    self.foes: List[Unit] = [Unit(u) for u in input_state['foes']]
    self.floor_map: List[List[bool]] = input_state['floorMap']
    self.empty_map: List[List[bool]] = [[square for square in col] for col in self.floor_map]

    for unit in self.units:
      if unit.health > 0 and unit.id != self.unit.id:
        self.empty_map[unit.x][unit.y] = False
    for foe in self.foes:
      if foe.health > 0:
        self.empty_map[foe.x][foe.y] = False

class Action:
  def __init__(self, action_type: str, direction: str):
    self.type = action_type
    self.direction = direction

def is_empty(x: int, y: int, state: GameState):
  return state.empty_map[x][y]
