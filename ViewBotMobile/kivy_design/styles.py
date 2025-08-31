"""
Mobile-optimized styling for ViewBot Android app
CSS-like styles for Kivy components
"""

from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp, sp
from kivy.utils import get_color_from_hex

class MobileStyles:
    """Mobile-optimized styling constants"""
    
    # Color palette (modern, mobile-friendly)
    COLORS = {
        'primary': get_color_from_hex('#4361ee'),
        'primary_dark': get_color_from_hex('#3a0ca3'),
        'secondary': get_color_from_hex('#4cc9f0'),
        'accent': get_color_from_hex('#f72585'),
        'success': get_color_from_hex('#4ade80'),
        'warning': get_color_from_hex('#f59e0b'),
        'error': get_color_from_hex('#ef4444'),
        'background': get_color_from_hex('#f8fafc'),
        'surface': get_color_from_hex('#ffffff'),
        'text_primary': get_color_from_hex('#1f2937'),
        'text_secondary': get_color_from_hex('#6b7280'),
        'border': get_color_from_hex('#e5e7eb'),
    }
    
    # Typography
    FONT_SIZES = {
        'h1': sp(24),
        'h2': sp(20),
        'h3': sp(18),
        'body': sp(16),
        'caption': sp(14),
        'small': sp(12),
    }
    
    # Spacing
    SPACING = {
        'xs': dp(4),
        'sm': dp(8),
        'md': dp(16),
        'lg': dp(24),
        'xl': dp(32),
    }
    
    # Border radii
    BORDER_RADIUS = {
        'sm': dp(4),
        'md': dp(8),
        'lg': dp(12),
        'xl': dp(16),
        'round': dp(24),
    }
    
    # Shadows (simulated with gradients)
    SHADOWS = {
        'sm': {'offset': (0, 2), 'blur': 4, 'color': (0, 0, 0, 0.1)},
        'md': {'offset': (0, 4), 'blur': 6, 'color': (0, 0, 0, 0.15)},
        'lg': {'offset': (0, 10), 'blur': 15, 'color': (0, 0, 0, 0.2)},
    }

def setup_theme(widget):
    """Apply mobile-optimized theme to a widget"""
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.textinput import TextInput
    from kivy.uix.progressbar import ProgressBar
    
    styles = MobileStyles()
    
    if isinstance(widget, BoxLayout):
        widget.background_color = styles.COLORS['background']
        widget.padding = styles.SPACING['md']
        widget.spacing = styles.SPACING['md']
        
    elif isinstance(widget, Label):
        widget.color = styles.COLORS['text_primary']
        widget.font_size = styles.FONT_SIZES['body']
        widget.bold = False
        
    elif isinstance(widget, Button):
        widget.background_color = styles.COLORS['primary']
        widget.color = (1, 1, 1, 1)
        widget.font_size = styles.FONT_SIZES['body']
        widget.bold = True
        widget.size_hint_y = None
        widget.height = dp(50)
        
        # Add rounded corners
        with widget.canvas.before:
            Color(*styles.COLORS['primary'])
            RoundedRectangle(
                size=widget.size,
                pos=widget.pos,
                radius=[styles.BORDER_RADIUS['lg']]
            )
        
    elif isinstance(widget, TextInput):
        widget.background_color = styles.COLORS['surface']
        widget.foreground_color = styles.COLORS['text_primary']
        widget.font_size = styles.FONT_SIZES['body']
        widget.padding = [styles.SPACING['md'], styles.SPACING['md']]
        widget.size_hint_y = None
        widget.height = dp(50)
        
        # Add border
        with widget.canvas.before:
            Color(*styles.COLORS['border'])
            RoundedRectangle(
                size=(widget.width, widget.height),
                pos=widget.pos,
                radius=[styles.BORDER_RADIUS['md']]
            )
        
    elif isinstance(widget, ProgressBar):
        widget.background_color = styles.COLORS['border']
        widget.color = styles.COLORS['primary']

def create_card(widget):
    """Apply card styling to a widget"""
    styles = MobileStyles()
    
    with widget.canvas.before:
        Color(*styles.COLORS['surface'])
        RoundedRectangle(
            size=widget.size,
            pos=widget.pos,
            radius=[styles.BORDER_RADIUS['lg']]
        )
        
        # Shadow effect
        Color(0, 0, 0, 0.1)
        Rectangle(
            size=(widget.width, dp(2)),
            pos=(widget.x, widget.y - dp(2))
        )

def apply_mobile_styles():
    """Apply mobile styles globally"""
    from kivy.config import Config
    
    # Mobile-optimized configuration
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '640')
    Config.set('graphics', 'resizable', '0')
    Config.set('kivy', 'window_icon', 'assets/icon.png')
    
    print("Mobile styles applied successfully")