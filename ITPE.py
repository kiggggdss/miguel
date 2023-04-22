import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.topGrid = GridLayout()
        self.topGrid.cols = 3

        self.middleGrid = GridLayout()
        self.middleGrid.cols = 1

        self.bottomGrid = GridLayout()
        self.bottomGrid.cols = 2

        self.cols = 1
        self.topGrid.add_widget (Button(text = "submit"))
        self.topGrid.add_widget (Button(text = "submit"))
        self.topGrid.add_widget (Button(text = "submit"))
        self.add_widget(self.topGrid)

        self.middleGrid.add_widget(Button(text = "submit"))
        self.add_widget(self.middleGrid)

        self.bottomGrid.add_widget(Button(text = "submit" ))
        self.bottomGrid.add_widget(Button(text = "submit"))
        self.add_widget(self.bottomGrid)

        
        self.bottomGrid = GridLayout()
        self.bottomGrid.cols = 2

        self.cols = 1
        self.bottomGrid.add_widget(Label (text="Name: "))
        self.fname = TextInput (multiline=False)
        self.bottomGrid.add_widget(self.fname)
        
        self.bottomGrid.add_widget(Label (text="Address: "))
        self.fAddress = TextInput (multiline=False)
        self.bottomGrid.add_widget(self.fAddress)
        
        self.bottomGrid.add_widget(Label (text="number: "))
        self.fnumber = TextInput (multiline=False)
        self.bottomGrid.add_widget(self.fnumber)
        self.add_widget(self.bottomGrid)

        self.btnsubmit = Button(text="submit")
        self.btnsubmit.bind(on_press=self.press)
        self.add_widget(self.btnsubmit)

        
    
    def press(self, instance):
        name =self.fname.text
        address = self.fAddress.text
        number = self.fnumber.text
        print ('your name is' + str(name) + 'your address is:' + str(address) +'your number is:' + str(number))


class MyApp(App) :
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
  