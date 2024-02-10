# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 11:54:39 2024

@author: kynda
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.temp = ['blah']
        
if __name__ == "__main__":
    app = MainApp()
    app.run()