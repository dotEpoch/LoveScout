# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 11:54:39 2024

@author: kynda
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

<<<<<<< Updated upstream
class MainApp(App):
=======
"""
AI functions
"""
def get_prompt():
    
    client = OpenAI(api_key = "MY-API-KEY")
    
    prompt = "Generate an outdoors scavenger hunt in the city of Montreal. A picture must be taken of the main attraction of each activity to confirm it's completion. Pictures of animal wildlife will be taken in parks. Insert these prompts into a csv format, seperated by commas, followed by  the general category of the subject of the photograph. The general categories are Sculpture, Animal, Landmark, Building, Food. Specify the exact element corresponding to their category in parenthesis. An example array is as follows: \"Visit Mount Royal Park and take a photo of the iconic Chalet du Mont Royal, Building (chalet)\\n Visit Schwartz's Deli and try their famous smoked meat sandwic, Food (sandwich)\\n. Do not talk during your response.Do not add anything after the csv text"    
    chat_completion = client.chat.completions.create(messages=[{"role":"user", "content":prompt}],
                                                 model="gpt-3.5-turbo")

    csv = chat_completion.choices[0].message.content
    response = []
    
    start = 0
    for i in range(len(csv)-1):
        if csv[i] == '\n':
            response.append(csv[start:i].split(','))
            start = i+1
            
    response.append(csv[start:].split(','))
    return response




"""
KIVY app programming / windows
"""

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    def submission(self, filename):
        
        #Get submission
        #global count
        treasure = self.ids.my_image.source = filename[0]
        global prompts
        global idx
        print("***********************************************")
        print(idx)
        print(len(prompts))
        print(prompts[-1])
        print(prompts[idx])
        print("****************************************")
        prompt = prompts[idx][0]
        prompt_type = prompts[idx][1]
        #count+=1
        valid = True
        #Check if valid
        if valid:        
            #Generate new prompt
            if idx == len(prompts)-1:
                App.get_running_app().root.current = 'end'
            
            #update label
            idx +=1
            new_prompt = prompts[idx][0]
            new_label = "Good Job! Next Mission: "
            self.ids.prompt.text = new_label+new_prompt
        else:
            self.ids.prompt.text = "Try again"

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my.kv')

#app runner
class MyApp(App):
>>>>>>> Stashed changes
    def build(self):
        self.temp = ['blah']
        
if __name__ == "__main__":
    app = MainApp()
    app.run()
