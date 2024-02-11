# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from openai import OpenAI

"""
AI functions
"""
def get_prompt():
    
    client = OpenAI(api_key = "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")
    
    prompt = "Generate an outdoors scavenger hunt in the city of Montreal. A picture must be taken of the main attraction of each activity to confirm it's completion. Pictures of animal wildlife will be taken in parks. Insert these prompts into a csv format, seperated by a semi-colon, followed by  the general category of the subject of the photograph. The general categories are Sculpture, Animal, Landmark, Building, Food. Specify the exact element corresponding to their category in parenthesis. An example array is as follows: \"Visit Mount Royal Park and take a photo of the iconic Chalet du Mont Royal; Building (chalet); Visit Schwartz's Deli and try their famous smoked meat sandwich; Food (sandwich). Do not talk during your response."    
    chat_completion = client.chat.completions.create(messages=[{"role":"user", "content":prompt}],
                                                 model="gpt-3.5-turbo")

    csv = chat_completion.choices[0].message.content
    response = csv.split(';')
    
    return response




"""
KIVY app programming / windows
"""

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    def submission(self, filename):
        
        #Get submission
        global count
        treasure = self.ids.my_image.source = filename[0]
        global prompts
        prompt_type = prompts[count+1]
        count+=1
        
        #Check if valid
        
        
        #Generate new prompt
        if count == len(prompts)//2:
            App.get_running_app().root.current = 'end'
            
        new_prompt = prompts[count]
        #Update Label
        self.ids.prompt.text = new_prompt

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my.kv')

#app runner
class MyApp(App):
    def build(self):
        return kv
if __name__ == "__main__":
    
    prompts = get_prompt()
    print(prompts)
    count = 0
    app = MyApp()
    app.run()