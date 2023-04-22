import kivy
#import App Class functionality located in kivy_venv\Lib\site_packages\kivy\app.py
from kivy.app import App 
#import Label Class functionality in kivy_venv\Lib\site_packages\kivy\uix\label.py
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


#file directory, in this case there is an existing folder named "kivyDesign"
#where the _base_design.kv resides.
Builder.load_file('kivyDesign\\accordions.kv')

class MyLayout(Widget):
    checklist = []
    def checkboxFunc(self, instance, checkState, LabelName):
        if(checkState == True):
            self.checklist.append(LabelName)
        else:
            self.checklist.remove(LabelName)
        print(f'{self.checklist}')
        if len(self.checklist) == 7:
            self.ids.status.text = "Application Status: Complete"


    def sliderFunc(self, test):
        acc_alpha = float(test/ 10)
        self.ids.acc_bgAlpha.background_color = (66/255, 66/255, 66/255, acc_alpha)
        self.ids.slider_label.text = f"slide value: {test}"
        
    
class accordions(App):
    title="Base Code Template"
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    accordions().run()