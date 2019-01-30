#!/usr/bin/env python3

# Copyright (c) 2019 Génération Robots

''' Utilisation des custom objects pour créer un parcours pour Cozmo.

This example demonstrates how you can create custom objects in the world, and
automatically have Cozmo path around them as if they are real obstacles.

It creates a few walls in front of cozmo and tells him to drive around it.
He will plan a path to drive 200mm in front of himself after these objects are created.

The `use_3d_viewer=True` argument causes the 3D visualizer to open in a new
window - this shows where Cozmo believes this imaginary object is.
'''

import cozmo
from cozmo.util import degrees, Pose
import time

def cozmo_program(robot: cozmo.robot.Robot):
	
	time.sleep(4)
	WALL_HEIGHT = 20

	robot.world.delete_all_custom_objects()

	center_wall1 	= Pose(300, 0, 0,  angle_z=degrees(0))
	wall1 			= robot.world.create_custom_fixed_object(center_wall1, 400, 10, WALL_HEIGHT, relative_to_robot=True)

	center_wall2	= Pose(250, 200, 0,  angle_z=degrees(0))
	wall2 			= robot.world.create_custom_fixed_object(center_wall2, 100, 10, WALL_HEIGHT, relative_to_robot=True)

	center_wall3 	= Pose(200, 250, 0,  angle_z=degrees(0))
	wall3 			= robot.world.create_custom_fixed_object(center_wall3, 10, 100, WALL_HEIGHT, relative_to_robot=True)

	center_wall4 	= Pose(300, 250, 0,  angle_z=degrees(0))
	wall4 			= robot.world.create_custom_fixed_object(center_wall4, 10, 100, WALL_HEIGHT, relative_to_robot=True)

	center_wall5 	= Pose(200, 50, 0,  angle_z=degrees(0))
	wall5 			= robot.world.create_custom_fixed_object(center_wall5, 10, 100, WALL_HEIGHT, relative_to_robot=True)

	center_wall6 	= Pose(250, 100, 0,  angle_z=degrees(0))
	wall6 			= robot.world.create_custom_fixed_object(center_wall6, 100, 10, WALL_HEIGHT, relative_to_robot=True)


	# soulever et reposer le robot à la position (0,0) de votre repère.
	# sa position devrait être (0,0)
	print(robot.pose.position) 

	if wall1 and wall2 and wall3 and wall4 and wall5 and wall6:
		print("fixed_objects created successfully")

	# Tests en position relative
	# action = robot.go_to_pose(Pose(350, 250, 0, angle_z=degrees(90)), relative_to_robot=True)
	# action.wait_for_completed()
	# print("Completed action: result = %s" % action)
	# print("New position robot=", robot.pose.position)
	
	# action = robot.go_to_pose(Pose(100, 0, 0, angle_z=degrees(90)), relative_to_robot=True)
	# action.wait_for_completed()
	# print("Completed action: result = %s" % action)
	# print("New position robot=", robot.pose.position)
	

	# action = robot.go_to_pose(Pose(100, 0, 0, angle_z=degrees(90)), relative_to_robot=True)
	# action.wait_for_completed()
	# print("Completed action: result = %s" % action)
	# print("New position robot=", robot.pose.position)
	

	# action = robot.go_to_pose(Pose(100, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
	# action.wait_for_completed()
	# print("Completed action: result = %s" % action)
	# print("New position robot=", robot.pose.position)

	# Tests en position absolue 
	# go to position A 
	action = robot.go_to_pose(Pose(250, 250, 0, angle_z=degrees(-90)), relative_to_robot=False)
	action.wait_for_completed()
	print("Completed action: result = %s" % action)
	print("New position robot=", robot.pose.position)
	
	# go to position B
	action = robot.go_to_pose(Pose(200, -50, 0, angle_z=degrees(0)), relative_to_robot=False)
	action.wait_for_completed()
	print("Completed action: result = %s" % action)
	print("New position robot=", robot.pose.position)

	# go to position C
	action = robot.go_to_pose(Pose(250, 50, 0, angle_z=degrees(180)), relative_to_robot=False)
	action.wait_for_completed()
	print("Completed action: result = %s" % action)
	print("New position robot=", robot.pose.position)

	while True:
		time.sleep(1)


cozmo.run_program(cozmo_program, use_3d_viewer=True)
