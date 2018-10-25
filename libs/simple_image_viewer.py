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

import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Frame, Button, Style

import time

class SimpleImageViewer():
    def __init__(self, w=800, h=640):
        self.root = tk.Tk()
        self.root.title('Mes images')

        # position coordinates of root 'upper left corner'
        x = 0
        y = 0

        # make the root window the size of the image
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # root has no image argument, so use a label as a panel
        self.panel = tk.Label(self.root)


        self.panel.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        self.root.update()


    def update_image(self, new_image):
        self.panel.configure(image=new_image)
        #print("Display new image")
        self.display = new_image
        self.root.update()

        