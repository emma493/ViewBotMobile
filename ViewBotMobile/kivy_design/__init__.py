"""
Kivy Design Package - UI components and styling for ViewBot Mobile
"""

__version__ = "1.0.0"

# Import styling utilities
from .styles import MobileStyles, setup_theme

# Export for external use
__all__ = ['MobileStyles', 'setup_theme']

def init_design():
    """Initialize design components"""
    print("Kivy design components initialized")
    return True
