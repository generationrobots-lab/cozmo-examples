#!/usr/bin/env python3

# Copyright (c) 2018 Génération Robots.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''

Stream de la caméra Cozmo vers une vue TkViewer
Utilisation d'une lib disponible dans le répertoire libs/

'''

import cozmo
import time
import sys

from PIL import Image, ImageTk
from libs.simple_image_viewer import SimpleImageViewer


def stream_camera(robot: cozmo.robot.Robot):
	
	# on active le stream camera
	robot.camera.image_stream_enabled = True

	# instance de la vue 
	image_view = SimpleImageViewer(w=320, h=240)


	print("Press CTRL-C to quit")
	try:
		while True:
			latest_image = robot.world.latest_image
			if latest_image:
				
				# affichage du image_number
				#print(latest_image.image_number)
				print('.', end='', flush=True)

				# récupération du raw
				im = latest_image.raw_image

				# update de la vue
				image = ImageTk.PhotoImage(im)
				image_view.update_image(image)

			# refresh tous les 100 ms
			time.sleep(0.1)

	# pour capter le Ctrl+C et terminer proprement		
	except KeyboardInterrupt:
		sys.exit()


cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(stream_camera)