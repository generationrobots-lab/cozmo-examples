#!/usr/bin/env python3

# Copyright (c) 2019 Génération robots

''' Transporter des cubes

Ce script permet de détecter les 3 cubes, défini 1 position, déplace 1 cube à cette position puis empiler 2 cubes

Utilisation : 
- Placer les 3 cubes alignés devant Cozmo
- Executer le script
'''

import time
from cozmo.util import degrees, Pose

import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

def shift(l, n=0):
    """
        Fonction qui décale la position des éléments d'une liste de n positions
    """
    return l[n:] + l[:n]


def cozmo_program(robot: cozmo.robot.Robot):
    cube1 = robot.world.get_light_cube(LightCube1Id)  # le cube trombone
    cube2 = robot.world.get_light_cube(LightCube2Id)  # le cube lampe 
    cube3 = robot.world.get_light_cube(LightCube3Id)  # le cube ab sur un T

    # scan de l'environnement pour trouver les cubes
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    try:
        _cubes = robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, timeout=60)
        print("Found %s cubes: %s" % (len(_cubes), _cubes))
    except asyncio.TimeoutError:
        print("Didn't find a cube")
    finally:
        look_around.stop()
    
    # position arbitraire
    location1 =  Pose(cube1.pose.position.x-200, cube1.pose.position.y-50 , 0, angle_z=degrees(0))

    # déplacer le cube 1 à la position location1
    if cube1 is not None:
        robot.pickup_object(cube1, num_retries=3).wait_for_completed()
        robot.go_to_pose(location1).wait_for_completed()
        robot.place_object_on_ground_here(cube1, num_retries=3).wait_for_completed()
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

    # placer le cube 3 sur le cube 2
    if cube2 is not None and cube3 is not None:
        robot.pickup_object(cube3, num_retries=3).wait_for_completed()
        robot.place_on_object(cube2, num_retries=3).wait_for_completed()
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

cozmo.run_program(cozmo_program,  use_viewer=True)
