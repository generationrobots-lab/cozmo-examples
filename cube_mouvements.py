#!/usr/bin/env python3

# Copyright (c) Génération Robots

'''Démo des événements de détection de mouvement des cubes


'''

import time

import cozmo


def cb_object_moving_started(evt, **kw):
    """ fonction callback appelée à chaque fois que l'événement EvtObjectMovingStarted est émis
        Si un cube commence à être déplacé (détection via l'accéléromètre du cube) l'événement est émis 
            
        On peut récupérer l'accélération du cube
    """
    
    print("Cube %s started moving: acceleration=%s" %
          (evt.obj.object_id, evt.acceleration))


def cb_object_moving(evt, **kw):
    """ fonction callback appelée à chaque fois que l'événement EvtObjectMoving est émis
        Si un cube commence à être déplacé (détection via l'accéléromètre du cube) l'événement est émis 

        On peut récupérer l'accélération et la durée du déplacement
    """
    print("Cube %s is moving: acceleration=%s, duration=%.1f seconds" %
          (evt.obj.object_id, evt.acceleration, evt.move_duration))


def cb_object_moving_stopped(evt, **kw):
    """ fonction callback appelée à chaque fois que l'événement EvtObjectMovingStopped est émis
        Si un cube arrête d'être déplacé (détection via l'accéléromètre du cube) l'événement est émis 

        On peut récupérer la durée du déplacement de l'objet
    """
    print("Cube %s stopped moving: duration=%.1f seconds" %
          (evt.obj.object_id, evt.move_duration))


def cozmo_program(robot: cozmo.robot.Robot):
    # Add event handlers that will be called for the corresponding event
    robot.add_event_handler(cozmo.objects.EvtObjectMovingStarted, handle_object_moving_started)
    robot.add_event_handler(cozmo.objects.EvtObjectMoving, handle_object_moving)
    robot.add_event_handler(cozmo.objects.EvtObjectMovingStopped, handle_object_moving_stopped)

    # keep the program running until user closes / quits it
    print("Press CTRL-C to quit")
    while True:
        time.sleep(1.0)


cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger for this example
cozmo.run_program(cozmo_program)
