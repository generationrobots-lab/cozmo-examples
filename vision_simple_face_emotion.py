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

Exemple de détection de visage et extraction de l'expression du visage

Utilisation du paramètre use_viewer=True dans run_program() de façon à visualiser à l'écran ce que le robot voit.

'''

import cozmo
import asyncio
import time

def main_program(_robot: cozmo.robot.Robot):
	global robot
	robot = _robot

	try:
		print("Positionner un visage devant la caméra ou positionner Cozmo devant vous")
		print("Ctrl+C pour terminer")
		while True:

			# l'événement renvoi un objet
			e = robot.world.wait_for(cozmo.faces.EvtFaceObserved)

			# on récupère l'objet Face
			face = e.face

			# on filtre sur un seuil de reconnaisance minimal de l'expression détectée
			if face.expression_score > 60:
				# on affiche Face.face_id, Face.know_expression, Face.expression_score et Face.name
				print("Visage ", str(face.face_id), " : ", face.known_expression, "(", str(face.expression_score), "%)")
		

		# pour éviter le rafraichissement trop rapide, une petite temporisation
		time.sleep(2)

	except (KeyboardInterrupt) as e :
		sys.exit()
	except asyncio.TimeoutError:
		print("Timeout écoulé")

cozmo.run_program(main_program, use_viewer=True)