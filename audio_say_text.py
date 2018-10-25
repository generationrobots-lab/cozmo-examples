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

Exemple d'utilisation de la méthode say_text pour faire parler Cozmo

'''

import cozmo

def bonjour(robot: cozmo.robot.Robot):
	# utilisation basique
	robot.say_text("Salut la compagnie !").wait_for_completed()
	
	# générer une voix humaine
	robot.say_text("Salut la compagnie !", False, use_cozmo_voice=False).wait_for_completed()
	
	# voix humaine et cozmo joue une animation
	robot.say_text("Salut à tous ! Je parle en bougeant.", True, use_cozmo_voice=False).wait_for_completed()
	
	# modification de la vitesse et hauteur de voix
	robot.say_text("Salut à tous ! On se dépêche !", False, voice_pitch=-5, duration_scalar=0.2, use_cozmo_voice=False).wait_for_completed()    

cozmo.run_program(bonjour)
