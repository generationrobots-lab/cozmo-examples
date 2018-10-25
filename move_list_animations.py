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

Exécution simple d'animations embarquées sur Cozmo

'''

import cozmo

animations = ''
triggers = ''

def cozmo_program(robot: cozmo.robot.Robot):
    try:
        global animations
        global triggers

        # parcourir la liste des Triggers
        for t in dir(cozmo.anim.Triggers):
            if '__' not in t:
                triggers += t + ','
        triggers = triggers[:-1]
        print(triggers)

        print("\n" , "#########################", "\n")
        
        # parcourir les noms des animations
        for a in robot.conn.anim_names:
            animations += a + ','
        animations = animations[:-1]
        print(animations)

    except KeyboardInterrupt:
        print("\nExit requested by user")

cozmo.run_program(cozmo_program)
