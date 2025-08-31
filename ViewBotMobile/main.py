from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import threading
import time

from viewbot.traffic_generator import TrafficGenerator
from viewbot.logger import Logger

class ViewBotMobile(App):
    def build(self):
        # Set window size for mobile development
        Window.size = (360, 640)
        
        # Main layout
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Background
        with self.layout.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            self.rect = Rectangle(size=Window.size, pos=self.layout.pos)
        
        # Title
        title = Label(
            text='[b]📱 ViewBot Mobile[/b]',
            markup=True,
            size_hint_y=None,
            height=50,
            color=(0.2, 0.4, 0.8, 1)
        )
        
        # URL Input
        self.url_input = TextInput(
            hint_text='Enter target URL (e.g., https://example.com)',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        
        # Views Input
        self.views_input = TextInput(
            hint_text='Number of views (10-1000)',
            input_filter='int',
            multiline=False,
            size_hint_y=None,
            height=50,
            text='50'
        )
        
        # Sessions Input
        self.sessions_input = TextInput(
            hint_text='Simultaneous sessions (1-50)',
            input_filter='int',
            multiline=False,
            size_hint_y=None,
            height=50,
            text='10'
        )
        
        # Start Button
        self.start_btn = Button(
            text='🚀 START GENERATING VIEWS',
            size_hint_y=None,
            height=60,
            background_color=(0.2, 0.6, 0.2, 1),
            bold=True
        )
        self.start_btn.bind(on_press=self.start_generation)
        
        # Progress Bar
        self.progress = ProgressBar(
            max=100,
            size_hint_y=None,
            height=20
        )
        
        # Log Output
        self.log_scroll = ScrollView(size_hint_y=1)
        self.log_label = Label(
            text='[b]Activity Log:[/b]\nReady to generate traffic...',
            markup=True,
            size_hint_y=None,
            text_size=(Window.width - 40, None)
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.log_scroll.add_widget(self.log_label)
        
        # Add all widgets to layout
        self.layout.add_widget(title)
        self.layout.add_widget(self.url_input)
        self.layout.add_widget(self.views_input)
        self.layout.add_widget(self.sessions_input)
        self.layout.add_widget(self.start_btn)
        self.layout.add_widget(self.progress)
        self.layout.add_widget(self.log_scroll)
        
        # Initialize traffic generator
        self.traffic_gen = TrafficGenerator()
        self.logger = Logger()
        
        # Update log every second
        Clock.schedule_interval(self.update_log, 1)
        
        return self.layout
    
    def update_log(self, dt):
        """Update log display"""
        self.log_label.text = f'[b]Activity Log:[/b]\n{self.logger.get_logs()}'
        self.log_label.texture_update()
    
    def start_generation(self, instance):
        """Start traffic generation"""
        try:
            url = self.url_input.text.strip()
            views = int(self.views_input.text)
            sessions = int(self.sessions_input.text)
            
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            # Validate inputs
            if views < 1 or views > 1000:
                self.show_popup('Error', 'Views must be between 1-1000')
                return
            
            if sessions < 1 or sessions > 50:
                self.show_popup('Error', 'Sessions must be between 1-50')
                return
            
            # Disable button during operation
            self.start_btn.disabled = True
            self.start_btn.text = '⏳ GENERATING...'
            self.start_btn.background_color = (0.5, 0.5, 0.5, 1)
            
            # Start generation in background thread
            thread = threading.Thread(
                target=self.traffic_gen.generate_mass_traffic,
                args=(url, sessions, sessions, views, 2),
                kwargs={'logger': self.logger}
            )
            thread.daemon = True
            thread.start()
            
            # Monitor progress
            Clock.schedule_interval(self.check_progress, 0.5)
            
        except ValueError:
            self.show_popup('Error', 'Please enter valid numbers')
        except Exception as e:
            self.show_popup('Error', f'Unexpected error: {str(e)}')
    
    def check_progress(self, dt):
        """Check generation progress"""
        if not self.traffic_gen.is_running:
            self.start_btn.disabled = False
            self.start_btn.text = '🚀 START GENERATING VIEWS'
            self.start_btn.background_color = (0.2, 0.6, 0.2, 1)
            self.progress.value = 100
            return False  # Stop scheduling
        
        # Update progress
        progress = self.traffic_gen.get_progress()
        self.progress.value = progress
        return True
    
    def show_popup(self, title, message):
        """Show error/success popup"""
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        )
        popup.open()

if __name__ == '__main__':
    ViewBotMobile().run()