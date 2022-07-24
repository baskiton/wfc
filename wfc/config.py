from collections import deque
from pathlib import Path
from typing import List, Sequence, Tuple, Union, Iterable

import PIL.Image

from PIL.Image import Resampling

from .tile import Tile


class Config:
    def __init__(self, name: str, size: Tuple[int, int], tile_size: Tuple[int, int] = None,
                 conn_type: str = Tile.SOCKET, starter_points=1) -> None:
        self.name = name
        self.size = size
        self.tile_size = tile_size
        self.conn_type = conn_type
        self.starter_points = starter_points

        self.tiles: List[Tile] = []
        self._origsized_images: List[List[PIL.Image.Image]] = []

    def add_tiles(self, images: Sequence[Union[str, Path, PIL.Image.Image]], name: str,
                  rule_up: Iterable, rule_right: Iterable,
                  rule_down: Iterable, rule_left: Iterable,
                  weight: Union[int, float] = 1,
                  rot_0=True, rot_90=False, rot_180=False, rot_270=False,
                  flip_v=False, flip_h=False) -> None:
        images_ = []
        for i in images:
            if isinstance(i, (str, Path)):
                images_.append(PIL.Image.open(i))
            elif isinstance(i, PIL.Image.Image):
                images_.append(i)
            else:
                raise TypeError(f'image must be str, Path, PIL.Image.Image, not {type(i)}')

        if self.tile_size is None:
            self.tile_size = images_[0].size

        # rule_up = list(rule_up)
        # rule_right = list(rule_right)
        # rule_down = list(rule_down)
        # rule_left = list(rule_left)

        rules = deque((rule_up, rule_right, rule_down, rule_left))
        if flip_v and flip_h:
            rot_180 = True
        rots = [*filter(lambda x: x[1], zip((0, 1, 2, 3), (rot_0, rot_90, rot_180, rot_270)))]
        flips = [*filter(lambda x: x[2], zip((0, 1),
                                             (PIL.Image.Transpose.FLIP_LEFT_RIGHT, PIL.Image.Transpose.FLIP_TOP_BOTTOM),
                                             (flip_v, flip_h)))]
        tot_rots = len(rots) + (1 << len(flips)) - 1

        for rot, _ in rots:
            loc_imgs = [i.rotate(-rot * 90) for i in images_]
            loc_rules = rules.copy()
            loc_rules.rotate(rot)

            if self.conn_type == Tile.SOCKET:
                if rot in (1, 2):
                    loc_rules[0] = loc_rules[0][::-1]
                    loc_rules[2] = loc_rules[2][::-1]

                if rot in (2, 3):
                    loc_rules[1] = loc_rules[1][::-1]
                    loc_rules[3] = loc_rules[3][::-1]

            self.tiles.append(Tile(name, rot, loc_imgs, loc_rules, weight / (len(rots) + len(flips)), self.conn_type, tot_rots))
            self._origsized_images.append(loc_imgs.copy())

            # for idx, i in enumerate(loc_imgs):
            #     n = f'tmp/{name}-{idx}_rot_{rot}.png'
            #     print('_rot_'.join((name, str(rot))), n, loc_rules)
            #     # i.save(Path(n))

        for flip, transp, _ in flips:
            loc_imgs = [i.transpose(transp) for i in images_]
            loc_rules = rules.copy()

            if self.conn_type == Tile.SOCKET:
                loc_rules[0 + flip] = loc_rules[0 + flip][::-1]
                loc_rules[2 + flip] = loc_rules[2 + flip][::-1]
                loc_rules[1 - flip], loc_rules[3 - flip] = loc_rules[3 - flip], loc_rules[1 - flip]

            if flip_v and flip_h:
                if flip == 0:
                    flip += 1
                elif flip == 1:
                    flip += 2
            else:
                flip = 2

            if self.conn_type == Tile.NAME:
                loc_rules.rotate(flip)

            self.tiles.append(Tile(name, flip, loc_imgs, loc_rules, weight / (len(rots) + len(flips)), self.conn_type, tot_rots))
            self._origsized_images.append(loc_imgs.copy())

            # for idx, i in enumerate(loc_imgs):
            #     n = f'tmp/{name}-{idx}_flip_{flip}.png'
            #     print('_flip_'.join((name, str(flip))), n, loc_rules)
            #     # i.save(Path(n))

    def resize_images(self):
        for i, imgs in enumerate(self._origsized_images):
            for j, img in enumerate(imgs):
                self.tiles[i].images[j] = img.resize(self.tile_size, Resampling.NEAREST)

    def freeze_tiles(self):
        self.tiles = tuple(self.tiles)
