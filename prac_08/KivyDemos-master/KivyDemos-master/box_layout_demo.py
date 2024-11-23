from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    # def handle_greet(self):
    #     print('greet')

    def handle_greet(self):
        print('test')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_handle(self):
        print('Cleared')
        self.root.ids.input_name.text = '' #targets the text field
        self.root.ids.output_label.text = '' #targets the output field


BoxLayoutDemo().run()
