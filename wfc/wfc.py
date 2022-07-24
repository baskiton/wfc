import math
import random

from collections import deque
from pathlib import Path
from typing import Deque, List, Optional, Set, Tuple, Union

import PIL.Image

from .config import Config, Tile


class Cell:
    def __init__(self, x: int, y: int, config: Config) -> None:
        self.x = x
        self.y = y
        self.__states = set(range(len(config.tiles)))
        self.config = config
        self.collapsed = False
        self._weight_sum = None

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, v: Set):
        self.__states = v
        self._weight_sum = None

    def __repr__(self):
        return f'Cell(x={self.x}, y={self.y})'

    @property
    def entropy(self) -> float:
        if self._weight_sum is None:
            self._weight_sum = (sum(self.config.tiles[i].inv_weight
                                    for i in self.states)
                                if self.states else 0)
        return self._weight_sum


class Wave:
    def __init__(self, width: int, height: int, config: Config) -> None:
        self.width = width
        self.height = height
        self.size = width * height
        self.field = tuple(Cell(x, y, config)
                           for y in range(height)
                           for x in range(width))

    def get_min_entropy(self) -> Optional[Cell]:
        mins = []
        min_e = math.inf

        for i, cell in enumerate(self.field):
            if min_e < cell.entropy or cell.collapsed:
                continue

            if cell.entropy < min_e:
                min_e = cell.entropy
                mins.clear()
            mins.append(cell)

        if mins:
            return random.choice(mins)

    def get_neighbours(self, cell: Cell) -> List[Tuple[Cell, int]]:
        c_idx = cell.y * self.width + cell.x
        result = []

        if cell.y - 1 >= 0:  # up
            n = self.field[c_idx - self.width]
            if not n.collapsed:
                result.append((self.field[c_idx - self.width], 0))

        if cell.x + 1 < self.width:  # right
            n = self.field[c_idx + 1]
            if not n.collapsed:
                result.append((n, 1))

        if cell.y + 1 < self.height:  # down
            n = self.field[c_idx + self.width]
            if not n.collapsed:
                result.append((n, 2))

        if cell.x - 1 >= 0:  # left
            n = self.field[c_idx - 1]
            if not n.collapsed:
                result.append((n, 3))

        return result


class WFC:
    def __init__(self, config: Config = None) -> None:
        self.wave: Optional[Wave] = None
        self.result: Optional[PIL.Image.Image] = None
        self.done = 0
        self.config: Optional[Config] = None

        if config is not None:
            self.configure(config)

    @property
    def size(self) -> Tuple[int, int]:
        return self.config.size

    @property
    def width(self) -> int:
        return self.config.size[0]

    @property
    def height(self) -> int:
        return self.config.size[1]

    @property
    def tile_size(self) -> Tuple[int, int]:
        return self.config.tile_size

    @property
    def tile_width(self) -> int:
        return self.config.tile_size[0]

    @property
    def tile_height(self) -> int:
        return self.config.tile_size[1]

    def configure(self, config: Config):
        self.config = config
        self.config.freeze_tiles()
        self.reset()

    def reset(self):
        self.config.resize_images()
        self.wave = Wave(self.width, self.height, self.config)
        self.result = PIL.Image.new('RGB', (self.width * self.tile_width, self.height * self.tile_height), color='black')
        self.done = 0

    def step(self):
        collapsed = self._observe()
        if collapsed is None:
            self.done = 1
            return

        for i in self._propagate(collapsed):
            yield i

    def _observe(self) -> Optional[Cell]:
        to_collapse = self.wave.get_min_entropy()
        if to_collapse is None:
            return

        self._pre_collapse(to_collapse)
        return to_collapse

    def _pre_collapse(self, cell: Cell) -> None:
        populations = tuple(cell.states)
        weights = tuple(self.config.tiles[i].weight for i in populations)
        cell.states = set(random.choices(populations, weights))

    def _propagate_act(self, collapsed: Cell, to_propagate: Deque[Cell]):
        if len(collapsed.states) == 1 and not collapsed.collapsed:
            collapsed.collapsed = True
            x = collapsed.x * self.tile_width
            y = collapsed.y * self.tile_height
            for state in collapsed.states:
                idx = random.randint(0, len(self.config.tiles[state].images) - 1)
                self.result.paste(self.config.tiles[state].images[idx],
                                  (x, y, x + self.tile_width, y + self.tile_height))
                yield x, y, state, idx

        neighbours = self.wave.get_neighbours(collapsed)
        random.shuffle(neighbours)
        for neighbour, direction in neighbours:
            allowed = set()
            for i in collapsed.states:
                t = self.config.tiles[i]
                for i_n in neighbour.states:
                    if t.compatible(self.config.tiles[i_n], direction):
                        allowed.add(i_n)

            if not allowed:
                self.done = -1
                if self.config.conn_type == Tile.SOCKET:
                    print(f'err in {direction=}\n'
                          f'from {collapsed}{set([self.config.tiles[s].rules[direction] for s in collapsed.states])}\n'
                          f'to   {neighbour}{set([self.config.tiles[s].rules[(direction + 2) % 4] for s in neighbour.states])}')
                elif self.config.conn_type == Tile.NAME:
                    print(f'err in {direction=}\n'
                          f'from {collapsed}{[self.config.tiles[s].rules[direction] for s in collapsed.states]}\n'
                          f'to   {neighbour}{[self.config.tiles[s].rules[(direction + 2) % 4] for s in neighbour.states]}')
                yield neighbour.x * self.tile_width, neighbour.y * self.tile_height, None, -1
                return

            if allowed != neighbour.states:
                neighbour.states = allowed
                to_propagate.append(neighbour)

    def _propagate(self, collapsed: Cell):
        to_propagate = deque()
        to_propagate.append(collapsed)

        while to_propagate and not self.done:
            for i in self._propagate_act(to_propagate.pop(), to_propagate):
                yield i

    def run(self):
        if self.done:
            self.reset()
        print('\nstart')

        for cell in random.choices(self.wave.field, k=self.config.starter_points):
            self._pre_collapse(cell)
            for i in self._propagate(cell):
                yield i

        while not self.done:
            for i in self.step():
                yield i

    def save_result(self, path: Union[str, Path]) -> None:
        if self.result is None:
            return

        self.result.save(path)
