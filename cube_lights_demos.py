#!/usr/bin/env python3

# Copyright (c) 2019 Génération robots

'''Control Cozmo's Cube lights

Ce script montre un exemple on allume les leds de cubes
'''

import time

import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

def shift(l, n=0):
    """
        Fonction qui décale la position des éléments d'une liste de n positions
    """
    return l[n:] + l[:n]


def cozmo_program(robot: cozmo.robot.Robot):
    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart
    cube3 = robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'

    red, green, blue, white=cozmo.lights.red_light, cozmo.lights.green_light, cozmo.lights.blue_light, cozmo.lights.white_light
    colors=[blue, white, white, white]

    if cube1 is not None:
        for l in [red, green, blue, white]: 
            cube1.set_lights(l)
            time.sleep(1)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

    if cube2 is not None:
        for i in range(20):
            colors = shift(colors, n=1)
            cube2.set_light_corners(colors[0], colors[1], colors[2], colors[3])
            time.sleep(0.4)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")


    if cube1 is not None:
        cube1.set_lights(cozmo.lights.off_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

    if cube2 is not None:
        cube2.set_lights(cozmo.lights.off_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")

    time.sleep(1)


cozmo.run_program(cozmo_program)
