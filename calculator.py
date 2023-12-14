from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("frontend.kv")

class DisplayScreen(Screen):    

    def __init__(self, **kw):
        super().__init__(**kw)
        self.process = 0
        self.current_value =0
        self.result = 0
        self.display_number = ''
        self.last_value = 0
        self.cycle = 0

    def final_result(self):        
        value = self.ids.result_box.text
        if not value:
            value = self.last_value
        if self.process == 1:
            if not '%' in value:                
                self.result = self.current_value * float(value)
            else:
                self.result = self.current_value * (float(value[:-1]) / 100)
        elif self.process == 2:
            if not '%' in value:
                self.result = self.current_value / float(value)
            else:
                self.result = self.current_value / (float(value[:-1]) /100)
        elif self.process == 3:
            if not '%' in value:
                self.result = self.current_value + float(value)
            else:
                self.result = self.current_value + (float(value[:-1]) / 100 * self.current_value)
        elif self.process == 4:
            if not '%' in value:
                self.result = self.current_value - float(value)
            else:
                self.result = self.current_value - (float(value[:-1] ) /100 * self.current_value)
        
        if float(self.result).is_integer():
            self.result = int(self.result)
        self.display_number = str(self.result)
        self.ids.result_box.hint_text = self.display_number
        self.current_value = float(self.display_number)
        self.last_value = value        
        self.ids.result_box.text = ''        
        self.cycle =0
        

    def multiply(self):
        if self.cycle:
            if self.ids.result_box.text:
                self.final_result()
        self.process = 1
        if not self.display_number:
            self.display_number = self.ids.result_box.text
        elif self.ids.result_box.text:
            self.display_number = self.ids.result_box.text

        if '%' in self.display_number:
            self.display_number = '0'
        self.current_value = float(self.display_number)
        self.ids.result_box.text = ''
        self.ids.result_box.hint_text = self.display_number
        self.cycle =1
            
    def dividing(self):
        if self.cycle:
            if self.ids.result_box.text:
                self.final_result()
        self.process = 2
        if not self.display_number:
            self.display_number = self.ids.result_box.text
        elif self.ids.result_box.text:
            self.display_number = self.ids.result_box.text
        
        if '%' in self.display_number:
            self.display_number = '0'
        self.current_value = float(self.display_number)
        self.ids.result_box.text = ''
        self.ids.result_box.hint_text = self.display_number
        self.cycle =1


    def plus(self):
        if self.cycle:
            if self.ids.result_box.text:
                self.final_result()
        self.process = 3
        if not self.display_number:
            self.display_number = self.ids.result_box.text
        elif self.ids.result_box.text:
            self.display_number = self.ids.result_box.text
        
        if '%' in self.display_number:
            self.display_number = '0'
        self.current_value = float(self.display_number)
        self.ids.result_box.text = ''
        self.ids.result_box.hint_text = self.display_number
        self.cycle =1

    def minus(self):
        if self.cycle:
            if self.ids.result_box.text:
                self.final_result()
        self.process = 4
        if not self.display_number:
            self.display_number = self.ids.result_box.text
        elif self.ids.result_box.text:
            self.display_number = self.ids.result_box.text
        
        if '%' in self.display_number:
            self.display_number = '0'
        self.current_value = float(self.display_number)
        self.ids.result_box.text = ''
        self.ids.result_box.hint_text = self.display_number
        self.cycle =1

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
        if text_now != '0':            
            self.ids.result_box.text += '0'
    
    def btn_backSpace(self):
        self.ids.result_box.do_backspace(from_undo=False, mode= 'bkspc')
        if not self.ids.result_box.text:
            if not self.display_number:            
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
    
    def btn_percent(self):
        text_now = self.ids.result_box.text
        if text_now != '0':
            if not '%' in text_now:
                self.ids.result_box.text += '%'

    def btn_AC(self):
        self.ids.result_box.text = '0'        
        self.process = 0
        self.current_value =0
        self.result = 0
        self.display_number = ''
        self.last_value = 0
        self.cycle = 0    
        
        
    
class RootWidget(ScreenManager):
    pass

class myCalculator(App):

    def build(self):
        Window.clearcolor = (0,0,0,1)
        return RootWidget()
    

myCalculator().run()