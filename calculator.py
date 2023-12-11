from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('frontend.kv')

class calculatorScreen(Screen):
    
    def multiply(self):
        pass

class RootWidget(ScreenManager):
    pass

class myCalculator(App):

    def build(self):
        return RootWidget()
    

myCalculator().run()