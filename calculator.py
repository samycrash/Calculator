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
        text_now = self.ids.result_box.text
        if text_now != '0':
            self.ids.result_box.text += '1'
        else:
            self.ids.result_box.text = '1'
    
    def btn_2(self):
        text_now = self.ids.result_box.text
        if text_now != '0':
            self.ids.result_box.text += '2'
        else:
            self.ids.result_box.text = '2'
    
    def btn_3(self):
        text_now = self.ids.result_box.text
        if text_now != '0':
            self.ids.result_box.text += '3'
        else:
            self.ids.result_box.text = '3'
    
    def btn_4(self):
        text_now = self.ids.result_box.text
        if text_now != '0':
            self.ids.result_box.text += '4'
        else:
            self.ids.result_box.text = '4'
    
    def btn_5(self):
        text_now = self.ids.result_box.text
        if text_now != '0':            
            self.ids.result_box.text += '5'
        else:
            self.ids.result_box.text = '5'
    
    def btn_6(self):
        text_now = self.ids.result_box.text
        if text_now != '0':            
            self.ids.result_box.text += '6'
        else:
            self.ids.result_box.text = '6'
    
    def btn_7(self):
        text_now = self.ids.result_box.text
        if text_now != '0':            
            self.ids.result_box.text += '7'
        else:
            self.ids.result_box.text = '7'
    
    def btn_8(self):
        text_now = self.ids.result_box.text
        if text_now != '0':
            self.ids.result_box.text += '8'
        else:
            self.ids.result_box.text = '8'
    
    def btn_9(self):
        text_now = self.ids.result_box.text
        if text_now != '0':
            self.ids.result_box.text += '9'
        else:
            self.ids.result_box.text = '9'

    def btn_0(self):
        text_now = self.ids.result_box.text 
        if len(text_now)>1:            
            self.ids.result_box.text += '0'
    
    def btn_backSpace(self):
        self.ids.result_box.do_backspace(from_undo=False, mode= 'bkspc')
        if not self.ids.result_box.text:
            self.ids.result_box.text = '0'
        
    def btn_symbolic(self):        
        text_now = self.ids.result_box.text        
        if text_now:
            if not '-' in text_now:
                symbol = '-'            
                text_now = symbol + text_now
                self.ids.result_box.text = text_now
            else:
                text_ = text_now[1:]
                self.ids.result_box.text = text_
    
    def btn_comma(self):
        text_now = self.ids.result_box.text
        if text_now:
            if not '.' in text_now:
                self.ids.result_box.text += '.'
        else:
            text_now = '0' + '.' + text_now
            self.ids.result_box.text = text_now
    
    def btn_AC(self):
        self.ids.result_box.text = '0'
        
        
    
class RootWidget(ScreenManager):
    pass

class myCalculator(App):

    def build(self):
        return RootWidget()
    

myCalculator().run()