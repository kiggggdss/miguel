import os, sys
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.resources import resource_add_path, resource_find

#Builder.load_file('mdAppComponents.kv')

    
class MainLayout(MDBoxLayout):
    def func(self,app):
        
        if app.theme_cls.theme_style == "Dark":
            app.theme_cls.theme_style = "Light"
            app.theme_cls.primary_palette = "Teal"
            app.theme_cls.accent_palette = "Blue"
            
        else:
            app.theme_cls.theme_style = "Dark"
            app.theme_cls.primary_palette = "Blue"
            app.theme_cls.accent_palette = "Teal"            
                
    
             
class mdAppComponents(MDApp):
    def build(self):
        #self.theme_cls.color = colors
        self.theme_cls.material_style = "M3"    
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.accent_palette= "Teal"
        return MainLayout()  
      
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    mdAppComponents().run()
    
    
