"""CP1404 Prac 8 - Miles to Kilometres Converter - Amber Hogarth"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_RATIO = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation."""
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_number_change(self, text, change):
        """Handle the number change from buttons."""
        print("handle change")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        """Update the result."""
        print("update result")
        self.output_km = str(miles * MILES_TO_KM_RATIO)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if not valid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
