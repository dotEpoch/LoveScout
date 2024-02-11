# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 11:54:39 2024

@author: kynda
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
    

class MainApp(App):
    def build(self):
        
        #create start button
        Fl = FloatLayout()
        btn = Button(text = 'Click to begin your adventure!', size_hint = (.3, .5),
                     background_color = (1,0,0.592,1), pos_hint={'x':.3, 'y':.2})
        Fl.add_widget(btn)
        return Fl
        
        
        
if __name__ == "__main__":
    app = MainApp()
    app.run()