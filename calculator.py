from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file("frontend.kv")

class DisplayScreen(Screen):
        
    def multiply(self):
        pass
    
    def dividing(self):
        pass

    def plus(self):
        pass

    def minus(self):
        pass

    def btn_1(self):
        self.ids.result_box.text += '1'
    
    def btn_2(self):
        self.ids.result_box.text += '2'
    
    def btn_3(self):
        self.ids.result_box.text += '3'
    
    def btn_4(self):
        self.ids.result_box.text += '4'
    
    def btn_5(self):
        self.ids.result_box.text += '5'
    
    def btn_6(self):
        self.ids.result_box.text += '6'
    
    def btn_7(self):
        self.ids.result_box.text += '7'
    
    def btn_8(self):
        self.ids.result_box.text += '8'
    
    def btn_9(self):
        self.ids.result_box.text += '9'
    
    def btn_0(self):
        if self.ids.result_box.text :
            self.ids.result_box.text += '0'
    
    def btn_backSpace(self):
        self.ids.result_box.do_backspace(from_undo=False, mode= 'bkspc')
        
    def btn_symbolic(self):        
        text_now = self.ids.result_box.text        
        if not '-' in text_now:
            symbol = '-'            
            text_now = symbol + text_now
            self.ids.result_box.text = text_now
        else:
            text_ = text_now[1:]
            self.ids.result_box.text = text_
    
class RootWidget(ScreenManager):
    pass

class myCalculator(App):

    def build(self):
        return RootWidget()
    

myCalculator().run()