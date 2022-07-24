import PIL.Image

from typing import List, Set, Sequence, Tuple, Union


class Tile:
    SOCKET = 1
    NAME = 2

    def __init__(self, name, rot, images: List[PIL.Image.Image], rules: Sequence, weight: Union[int, float], conn_type: str, tot_rots: int) -> None:
        self.name = name
        self.rot = rot
        self.images = images
        self.rules = rules
        self.weight = weight
        self.inv_weight = 1 / weight
        self.conn_type = conn_type
        self.tot_rots = tot_rots
        self.rule_names = tuple(f'{self.name}_{i}' for i in range(len(rules)))

        if conn_type == self.SOCKET:
            self.compatible = self._socket_compatible
        elif conn_type == self.NAME:
            self.compatible = self._name_compatible
        else:
            raise NotImplemented

    @property
    def rule_up(self) -> Tuple[Set, Set]:
        return self.rules[0]

    @property
    def rule_right(self) -> Tuple[Set, Set]:
        return self.rules[1]

    @property
    def rule_down(self) -> Tuple[Set, Set]:
        return self.rules[2]

    @property
    def rule_left(self) -> Tuple[Set, Set]:
        return self.rules[3]

    def _socket_compatible(self, other: 'Tile', direction: int) -> bool:
        return self.rules[direction] == other.rules[(direction + 2) % 4]

    def _name_compatible(self, other: 'Tile', direction: int) -> bool:
        o_direction = (direction + 2) % 4
        d = (4 + direction - self.rot) % 4
        od = (6 + direction - other.rot) % 4
        # print(f'check {direction} {d=} {od=} {self.name}<{d}>{self.rules[direction]} <-> {other.name}<{od}>{other.rules[o_direction]}')
        return (self.rule_names[d] in other.rules[o_direction]
                and other.rule_names[od] in self.rules[direction])
