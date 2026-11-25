from kitty.fast_data_types import get_boss, get_options, wcswidth
from kitty.tab_bar import as_rgb, draw_tab_with_separator


def draw_tab(draw_data, screen, tab, before, max_tab_length, index, is_last, extra_data):
    end = draw_tab_with_separator(
        draw_data, screen, tab, before, max_tab_length, index, is_last, extra_data
    )
    if not is_last or extra_data.for_layout:
        return end

    window = get_boss().os_window_map[tab.os_window_id].active_window
    status = window.user_vars.get("GitStatus", "") if window else ""
    if status:
        text = f" 󰊢 {status} "
        start = screen.columns - wcswidth(text) - 1
        # shortcut: hide Git status when tabs fill the bar; reserve space if needed.
        if start > screen.cursor.x:
            screen.cursor.x = start
            color = get_options().color3 if "●" in status or "✚" in status else get_options().color2
            screen.cursor.fg = as_rgb(int(color))
            screen.cursor.bg = as_rgb(int(draw_data.default_bg))
            screen.draw(text)
    return end


def on_set_user_var(boss, window, data):
    if data["key"] == "GitStatus":
        tab = window.tabref()
        if tab is not None:
            tab.mark_tab_bar_dirty()
