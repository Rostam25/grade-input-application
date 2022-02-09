import kivy
from kivy.app import App #Application module from kivy
from kivy.uix.gridlayout import GridLayout #Grid layout module from kivy
from kivy.uix.label import Label #Labels for different sections from kivy
from kivy.uix.textinput import TextInput #Text input so user can type from kivy
from kivy.uix.button import Button #Buttons from kivy

class Glayout(GridLayout):
    def __init__(self, **kwargs): #kwargs allows for unlimited arguments
        super(Glayout, self).__init__()
        self.cols = 2

        #Student Name Field
        self.add_widget(Label(text = "Student Name"))
        self.s_name = TextInput() #Stores student name in this variable
        self.add_widget(self.s_name) #Stores the student name to the corresponding widget

        #Student ID Field
        self.add_widget(Label(text = "Student ID"))
        self.s_ID = TextInput()
        self.add_widget(self.s_ID)

        #Student Percentage Field
        self.add_widget(Label(text = "Percentage Attained"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        #Creating Button
        self.press = Button(text = "Click Me")
        self.press.bind(on_press = self.click_me) #Creating an event
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Student Name: " + self.s_name.text)
        print("Student ID: " + self.s_ID.text)
        print("Percentage Attained: " + self.s_marks.text)
        print("")

class GradeInputApplication(App):
    def build(self):
        return Glayout()

if __name__ == "__main__":
    GradeInputApplication().run()