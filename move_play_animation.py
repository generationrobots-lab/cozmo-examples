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

Exécution simple d'animations embarquées sur Cozmo par Trigger ou par nom

'''

import cozmo
import time

def cozmo_program(robot: cozmo.robot.Robot):

    # Jouer une animation à partir d'une Trigger
    print("Exécution de la trigger : OnSpeedtapRoundPlayerWinHighIntensity")
    robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapRoundPlayerWinHighIntensity).wait_for_completed()
    robot.say_text("une autre", duration_scalar=0.5).wait_for_completed()

    # # Jouer une animation à partir d'une Trigger en ignorant le mouvement des roues
    print("Exécution de la trigger : OnSpeedtapGameCozmoWinHighIntensity (sans body track)")
    robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapGameCozmoWinHighIntensity, ignore_body_track=True).wait_for_completed()
    robot.say_text("et encore une", duration_scalar=0.5).wait_for_completed()

    
    # # Jouer une animation à partir d'une Trigger avec le mouvement des roues
    print("Exécution de la trigger : OnSpeedtapGameCozmoWinHighIntensity (avec body track)")
    robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapGameCozmoWinHighIntensity, ignore_body_track=False).wait_for_completed()
    robot.say_text("une dernière ", duration_scalar=0.5).wait_for_completed()

    # # Jouer une animation par son nom.
    print("Exécution de l'animation :anim_greeting_happy_03")
    robot.play_anim(name="anim_greeting_happy_03").wait_for_completed()

    robot.say_text("C'était sympa, hein ?", duration_scalar=0.5).wait_for_completed()

cozmo.run_program(cozmo_program)