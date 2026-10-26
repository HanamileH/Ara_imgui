import os
import sys
from pathlib import Path
from typing import Union

from imgui_bundle import imgui, immapp, hello_imgui

from .theme import IMGUI_THEMES, Theme

class App:
    def __init__(self, title="New app", width=800, height=600):
        """Initialize the application.
        
        Args:
            title (str): Window title.
            width (int): Window width.
            height (int): Window height.
        """
        self.title = title
        self.width = width
        self.height = height

        self.font_path = None # None for default font
        self.font_size = 18

        self.theme = Theme.dark
        self._update_theme = True
   
    
    def load_font(self, font_path=None, font_size=18):
        """
        Loads a font for the application.

        Args:
            font_path (str, optional): The path to the font file. Defaults to None, which loads the default font.
            font_size (int, optional): The size of the font. Defaults to 18.
        """

        # If no font is specified, we use the default
        if self.font_path is None:
            if sys.platform == "win32":
                font_path = Path("C:/Windows/Fonts/segoeui.ttf")
            elif sys.platform == "darwin":
                font_path = Path("/System/Library/Fonts/SFNSDisplay.ttf")
            elif sys.platform == "linux":
                font_path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
            else:
                raise Exception(f"Unsupported platform {sys.platform}")
        else:
            font_path = Path(self.font_path)
            
        # Check if font file exists
        if not os.path.exists(font_path):
            raise Exception(f"Font file '{font_path}' does not exist")

        # Save font path and size
        self.font_path = str(font_path)
        self.font_size = font_size
    

    def load_default_font(self):
        """Loads the default imgui font for the application."""
        self.font_path = None
        self.font_size = 18

    def apply_theme(self, theme: Union[Theme, str]):
        """
        Applies a theme to the application.

        Args:
            theme (Theme | str): A theme from :class:`ara_imgui.Theme`
                (also available as ``ara_imgui.themes``) or its name as a
                string, for example ``themes.cherry`` or ``"cherry"``.

        Raises:
            ValueError: If the theme name is not known.
            TypeError: If ``theme`` is neither a ``Theme`` nor a string.
        """

        if isinstance(theme, Theme):
            selected = theme
        elif isinstance(theme, str):
            try:
                selected = Theme(theme)
            except ValueError:
                raise ValueError(f"Theme '{theme}' not found") from None
        else:
            raise TypeError(
                f"Theme must be a Theme or str, not {type(theme).__name__}"
            )

        self.theme = selected
        self._update_theme = True


    def run(self, render=None, update=None, terminate=None):
        """Run main loop with dependency-resolved callbacks
        
        Args:
            render (function, optional): Render callback. Defaults to None.
            update (function, optional): Update callback. Defaults to None.
            terminate (function, optional): Terminate callback. Defaults to None.
        """
        
        # Load font before launch
        def _load_font():
            # Load the font and set it as default
            io = imgui.get_io()
            io.fonts.clear()

            if self.font_path is not None:
                custom_font = io.fonts.add_font_from_file_ttf(self.font_path, self.font_size)
                io.font_default = custom_font
            else:
                io.font_default = io.fonts.add_font_default()

        # Custom rendering callback
        def _render():
            if self._update_theme:
                hello_imgui.apply_theme(IMGUI_THEMES[self.theme])
                self._update_theme = False

            # Update callback
            if update is not None:
                update()

            # Render callback
            viewport_size = imgui.get_main_viewport().size
            imgui.set_next_window_pos(imgui.ImVec2(0, 0))
            imgui.set_next_window_size(imgui.ImVec2(viewport_size.x, viewport_size.y))

            imgui.begin(
                f"##Main window", 
                flags=imgui.WindowFlags_.no_decoration |
                imgui.WindowFlags_.no_move
            )

            if render is not None:
                render()

            imgui.end()

        # Initialize the application
        params = hello_imgui.RunnerParams()
        params.app_window_params.window_geometry.size = (self.width, self.height)
        params.callbacks.load_additional_fonts = _load_font
        params.app_window_params.window_title = self.title
        params.callbacks.show_gui = _render

        if terminate is not None:
            params.callbacks.before_exit = terminate

        # Run the application
        hello_imgui.run(params)
