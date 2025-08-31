"""
ViewBot Mobile - Professional Traffic Generator for Android
Core functionality package for generating website views.
"""

__version__ = "1.0.0"
__author__ = "ViewBot Team"
__license__ = "MIT"

# Import main components for easy access
from .traffic_generator import MobileTrafficGenerator
from .logger import Logger

# Package initialization
def init_package():
    """Initialize the ViewBot package"""
    print(f"ViewBot Mobile v{__version__} initialized")
    return True

# Export main classes
__all__ = ['MobileTrafficGenerator', 'Logger', 'init_package']