import pygame

def load_tiles():
    tiles = {}

    for tile_name, tile_key in tile_map.items():
        tiles[tile_key] = pygame.image.load('resources/tiles/' + tile_name + '.png')
    return tiles

def load_textfile(afile):
    with open(afile, 'r') as f:
        rows = f.readlines()
        for x in range(len(rows) - 1, -1, -1):
            if rows[x][0] == "\n" or rows[x][0] == "#":
                rows.pop(x)
    list = []
    for x in range(len(rows)):
        list.append(rows[x])
        list[-1] = list[-1].rstrip("\n")
    return list

tile_map = {'bg_water':'w',
             'bg_grass':'g',
             'bg_sand':'s',
             'bg_tree':'t',
             'bg_house':'h',
             'bg_teepee':'e',
             'bg_grock':'r',
             'bg_road_lr':'0',
             'bg_road_ud':'1',
             'bg_road_dr':'2',
             'bg_road_dl':'3',
             'bg_road_lu':'4',
             'bg_road_ur':'5',
             'bg_troad_u':'6',
             'bg_troad_d':'7',
             'bg_troad_l':'8',
             'bg_troad_r':'9',
             'bg_xroad':'x'
             }

