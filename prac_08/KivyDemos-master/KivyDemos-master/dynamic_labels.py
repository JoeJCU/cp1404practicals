
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.lang import Builder

class DynamicLabels(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.names = {"Joe", "Tim", "Alis", "Blaze"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels/Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names: #iterating through all the name in the 'self.name' array
            label = Label(text=name)
            self.root.ids.main.add_widget(label)   #adds a seprate label for each name
        return self.root










DynamicLabels().run()