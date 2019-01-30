#!/usr/bin/env python3

# Copyright (c) Génération Robots

'''Démonstration des événements de détection de mouvement des cubes

Les cubes n'ont pas besoin d'être vu par la caméra du robot

'''

import time

import cozmo


def cb_object_moving_started(evt, **kw):
    """ fonction callback appelée à chaque fois que l'événement EvtObjectMovingStarted est émis
        Si un cube commence à être déplacé (détection via l'accéléromètre du cube) l'événement est émis 
            
        On peut récupérer l'accélération du cube
    """
    
    print("Le cube %s a commencé à bouger: accéleration=%s" %
          (evt.obj.object_id, evt.acceleration))


def cb_object_moving(evt, **kw):
    """ fonction callback appelée à chaque fois que l'événement EvtObjectMoving est émis
        Si un cube commence à être déplacé (détection via l'accéléromètre du cube) l'événement est émis 

        On peut récupérer l'accélération et la durée du déplacement
    """
    print("Le cube %s est en mouvement: accéleration=%s, durée=%.1f secondes" %
          (evt.obj.object_id, evt.acceleration, evt.move_duration))


def cb_object_moving_stopped(evt, **kw):
    """ fonction callback appelée à chaque fois que l'événement EvtObjectMovingStopped est émis
        Si un cube arrête d'être déplacé (détection via l'accéléromètre du cube) l'événement est émis 

        On peut récupérer la durée du déplacement de l'objet
    """
    print("Le cube %s a arrêté de bouger: durée=%.1f secondes" %
          (evt.obj.object_id, evt.move_duration))


def cozmo_program(robot: cozmo.robot.Robot):
    # on ajoute des handlers pour chaque événement
    robot.add_event_handler(cozmo.objects.EvtObjectMovingStarted, cb_object_moving_started)
    robot.add_event_handler(cozmo.objects.EvtObjectMoving, cb_object_moving)
    robot.add_event_handler(cozmo.objects.EvtObjectMovingStopped, cb_object_moving_stopped)

    # boucle infinie jusqu'à la combinaison de touches CTRL+C
    print("Presser CTRL-C pour arrêter")
    while True:
        time.sleep(1.0)


cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger for this example
cozmo.run_program(cozmo_program)
