from enum import Enum
from imgui_bundle import hello_imgui


class Theme(str, Enum):
    """Themes accepted by :meth:`ara_imgui.App.apply_theme`.

    Members are strings, so both the enum member and its name work::

        app.apply_theme(themes.cherry)
        app.apply_theme("cherry")

    They can also be used for comparisons and lookups, because
    ``Theme.cherry == "cherry"``.
    """

    dark = "dark"
    light = "light"
    classic = "classic"
    material_flat = "material_flat"
    photoshop_style = "photoshop_style"
    gray_variations = "gray_variations"
    gray_variations_darker = "gray_variations_darker"
    microsoft_style = "microsoft_style"
    cherry = "cherry"
    darcula = "darcula"
    darcula_darker = "darcula_darker"
    light_rounded = "light_rounded"
    so_dark_accent_blue = "so_dark_accent_blue"
    so_dark_accent_yellow = "so_dark_accent_yellow"
    so_dark_accent_red = "so_dark_accent_red"
    black_is_black = "black_is_black"
    white_is_white = "white_is_white"

    def __str__(self) -> str:
        return self.value


themes = Theme


# Public theme name -> internal ``hello_imgui.ImGuiTheme_`` value.  Members of
# ``Theme`` are strings, so ``"dark" in IMGUI_THEMES`` also works.
IMGUI_THEMES = {
    Theme.dark: hello_imgui.ImGuiTheme_.imgui_colors_dark,
    Theme.light: hello_imgui.ImGuiTheme_.imgui_colors_light,
    Theme.classic: hello_imgui.ImGuiTheme_.imgui_colors_classic,
    Theme.material_flat: hello_imgui.ImGuiTheme_.material_flat,
    Theme.photoshop_style: hello_imgui.ImGuiTheme_.photoshop_style,
    Theme.gray_variations: hello_imgui.ImGuiTheme_.gray_variations,
    Theme.gray_variations_darker: hello_imgui.ImGuiTheme_.gray_variations_darker,
    Theme.microsoft_style: hello_imgui.ImGuiTheme_.microsoft_style,
    Theme.cherry: hello_imgui.ImGuiTheme_.cherry,
    Theme.darcula: hello_imgui.ImGuiTheme_.darcula,
    Theme.darcula_darker: hello_imgui.ImGuiTheme_.darcula_darker,
    Theme.light_rounded: hello_imgui.ImGuiTheme_.light_rounded,
    Theme.so_dark_accent_blue: hello_imgui.ImGuiTheme_.so_dark_accent_blue,
    Theme.so_dark_accent_yellow: hello_imgui.ImGuiTheme_.so_dark_accent_yellow,
    Theme.so_dark_accent_red: hello_imgui.ImGuiTheme_.so_dark_accent_red,
    Theme.black_is_black: hello_imgui.ImGuiTheme_.black_is_black,
    Theme.white_is_white: hello_imgui.ImGuiTheme_.white_is_white,
}
