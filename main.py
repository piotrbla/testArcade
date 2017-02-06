from arcade import open_window, color, draw_text, finish_render, run, start_render


def main():
    open_window('My game', 800, 600)
    start_render()
    draw_text("Hello zażółć gęślą jaźń", 100, 100, color.WHITE, font_size=16)
    finish_render()
    run()

if __name__ == '__main__':
    main()