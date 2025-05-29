from .data import summaries, verses
from .utils import *   # if you want to expose all utility functions
from .constant import *  # if constants are defined here

__version__ = "0.1.0"

# You can also add some package-level docstring
"""
gita - A Python package providing Bhagavad Gita summaries of chapters, verses and more...
"""

# Optionally, you could define what gets imported when someone uses `from gita import *`
__all__ = ['summaries', 'verses']
