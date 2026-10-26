"""Tests for the public theme enum and its imgui_bundle mapping."""

from imgui_bundle import hello_imgui

from ara_imgui import IMGUI_THEMES, Theme, themes
from ara_imgui.app import App


def test_themes_alias_is_theme_enum():
    assert themes is Theme


def test_every_theme_is_mapped():
    for theme in Theme:
        assert theme in IMGUI_THEMES
        assert isinstance(IMGUI_THEMES[theme], hello_imgui.ImGuiTheme_)


def test_public_names_map_to_differently_named_imgui_themes():
    assert IMGUI_THEMES[Theme.dark] == hello_imgui.ImGuiTheme_.imgui_colors_dark
    assert IMGUI_THEMES[Theme.light] == hello_imgui.ImGuiTheme_.imgui_colors_light
    assert IMGUI_THEMES[Theme.classic] == hello_imgui.ImGuiTheme_.imgui_colors_classic


def test_theme_members_are_string_like():
    assert Theme.cherry == "cherry"
    assert str(Theme.cherry) == "cherry"
    assert IMGUI_THEMES[Theme.cherry] == hello_imgui.ImGuiTheme_.cherry
    # The old string API keeps working.
    assert IMGUI_THEMES["cherry"] == hello_imgui.ImGuiTheme_.cherry


def test_apply_theme_accepts_enum_and_string():
    app = App("test")

    app.apply_theme(themes.cherry)
    assert app.theme is Theme.cherry
    assert app._update_theme is True

    app.apply_theme("light")
    assert app.theme is Theme.light


def test_apply_theme_rejects_unknown_name():
    app = App("test")
    try:
        app.apply_theme("not-a-theme")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_apply_theme_rejects_wrong_type():
    app = App("test")
    try:
        app.apply_theme(42)
    except TypeError:
        pass
    else:
        raise AssertionError("expected TypeError")
