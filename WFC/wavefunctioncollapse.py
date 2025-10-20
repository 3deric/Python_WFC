import pygame
import os
import re
from operator import attrgetter
from worldelement import WorldElement as WE
from worldsprite import WorldSprite as WS


def _load_tiles_from_images(base_dir):
    img_dir = os.path.join(base_dir, 'img')
    tiles = []
    if not os.path.isdir(img_dir):
        return tiles
    image_files = [f for f in os.listdir(img_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif"))]
    def extract_id(name):
        m = re.search(r'(\d+)', name)
        return int(m.group(1)) if m else None
    # Prepare list of (id_or_None, fullpath)
    image_catalogue = [(extract_id(fn), os.path.join(img_dir, fn)) for fn in image_files]
    next_auto_id = 0
    for tid, fpath in image_catalogue:
        if tid is None:
            tid = next_auto_id
            next_auto_id += 1
        tiles.append(WS(tid, fpath, edges=None))
    _build_compatibility(tiles)
    return tiles

def _build_compatibility(tiles):
    # Precompute, for each tile, the list of compatible neighbor ids by direction (0:N,1:E,2:S,3:W)
    def corners_match(a, b, dir_index):
        # Corner indices: 0=NW, 1=NE, 2=SE, 3=SW
        pairs_by_dir = {
            0: [(0, 3), (1, 2)],  # North neighbor
            1: [(1, 0), (2, 3)],  # East neighbor
            2: [(3, 0), (2, 1)],  # South neighbor
            3: [(0, 1), (3, 2)],  # West neighbor
        }
        for sc, nc in pairs_by_dir[dir_index]:
            sc_col = a.corners.get(sc)
            nc_col = b.corners.get(nc)
            if sc_col is None or nc_col is None:
                # Permissive if missing data
                continue
            if tuple(sc_col[:3]) != tuple(nc_col[:3]):
                return False
        return True

    for t in tiles:
        t.compat = {0: [], 1: [], 2: [], 3: []}
    for a in tiles:
        for b in tiles:
            for d in (0, 1, 2, 3):
                if corners_match(a, b, d):
                    a.compat[d].append(b.id)
        # For backward compatibility with older filtering code
        a.neighbours = [a.compat[0], a.compat[1], a.compat[2], a.compat[3]]


class WaveFunctionCollapse:

    def __init__(self, size, screen):
        self.world_size = size
        self.world_elements = []
        self.auto_collapse_active = False
        self.last_time = -1
        self.auto_collapse_wait = 50
        self.screen = screen

        self.set_reset()

    def set_collapse(self):
        self.auto_collapse_active =  bool(1 - int(self.auto_collapse_active))

    def set_reset(self):
        self.auto_collapse_active = False
        self.setup_world_elements()
        self.set_world_element_neighbours()

    def setup_world_elements(self):
        self.world_elements = []
        elements = _load_tiles_from_images(os.path.dirname(__file__))
        for y in range(self.world_size):
            for x in range(self.world_size):
                we = WE(self.screen, elements, x, y)
                self.world_elements.append(we)

    def set_world_element_neighbours(self):
        for we in self.world_elements:
            north = None
            east = None
            south = None
            west = None

            if we.pos[1] - 1 >= 0:
                north = self.world_elements[we.pos[0] + self.world_size * (we.pos[1]-1)]
            if we.pos[0] + 1 < self.world_size:
                east = self.world_elements[we.pos[0] + 1 + self.world_size * we.pos[1]]
            if we.pos[1] + 1 < self.world_size:
                south = self.world_elements[we.pos[0] + self.world_size * (we.pos[1]+1)]
            if we.pos[0] - 1 >= 0:
                west = self.world_elements[we.pos[0] - 1 + self.world_size * we.pos[1]]
            we.set_neighbours([north, east, south, west])

    def auto_collapse(self):
        if not self.auto_collapse_active:
            return
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= self.auto_collapse_wait:
            self.last_time = current_time
            next = self.world_elements.index(min(self.world_elements, key=attrgetter('entropy')))
            self.world_elements[next].collapse()  
 
    def collapse(self, collapse_index):
        self.last_time= pygame.time.get_ticks()
        self.world_elements[collapse_index].collapse()  

    def draw(self):
        for we in self.world_elements:
            we.draw()
