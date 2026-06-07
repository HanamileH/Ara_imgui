import os
import sys
from pathlib import Path
from imgui_bundle import imgui, immapp, hello_imgui

IMGUI_THEMES = {
    "dark": hello_imgui.ImGuiTheme_.imgui_colors_dark,
    "light": hello_imgui.ImGuiTheme_.imgui_colors_light,
    "classic": hello_imgui.ImGuiTheme_.imgui_colors_classic,
    "material_flat": hello_imgui.ImGuiTheme_.material_flat,
    "photoshop_style": hello_imgui.ImGuiTheme_.photoshop_style,
    "gray_variations": hello_imgui.ImGuiTheme_.gray_variations,
    "gray_variations_darker": hello_imgui.ImGuiTheme_.gray_variations_darker,
    "microsoft_style": hello_imgui.ImGuiTheme_.microsoft_style,
    "cherry": hello_imgui.ImGuiTheme_.cherry,
    "darcula": hello_imgui.ImGuiTheme_.darcula,
    "darcula_darker": hello_imgui.ImGuiTheme_.darcula_darker,
    "light_rounded": hello_imgui.ImGuiTheme_.light_rounded,
    "so_dark_accent_blue": hello_imgui.ImGuiTheme_.so_dark_accent_blue,
    "so_dark_accent_yellow": hello_imgui.ImGuiTheme_.so_dark_accent_yellow,
    "so_dark_accent_red": hello_imgui.ImGuiTheme_.so_dark_accent_red,
    "black_is_black": hello_imgui.ImGuiTheme_.black_is_black,
    "white_is_white": hello_imgui.ImGuiTheme_.white_is_white
}

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

        self.theme = "dark"
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

    def apply_theme(self, name: str):
        """
        Applies a theme to the application.

        Args:
            name (str): The name of the theme
            Available themes:
                - dark
                - light
                - classic
                - material_flat
                - photoshop_style
                - gray_variations
                - gray_variations_darker
                - microsoft_style
                - cherry
                - darcula
                - darcula_darker
                - light_rounded
                - so_dark_accent_blue
                - so_dark_accent_yellow
                - so_dark_accent_red
                - black_is_black
                - white_is_white

        Raises:
            ValueError: If the theme name is not found
        """

        if name in IMGUI_THEMES:
            self.theme = name
            self._update_theme = True
        else:
            raise ValueError(f"Theme '{name}' not found")


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
                hello_imgui.apply_theme(
                    IMGUI_THEMES[self.theme]
                )

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
