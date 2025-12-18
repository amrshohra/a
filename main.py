import flet as ft
import webbrowser

def main(page: ft.Page):
    page.title = "عمرو"
    page.window_width = 360
    page.window_height = 720
    # أيقونة بسيطة كنص داخل AppBar
    appbar = ft.AppBar(title=ft.Text("amr", size=18, weight="bold"))
    btn = ft.ElevatedButton("افتح التطبيق", on_click=lambda e: webbrowser.open("https://sites.google.com/view/amr-app?usp=sharing"))
    page.add(appbar, ft.Column([ft.Text("تطبيق عمرو لتوصيل الإعلانات", size=16), btn], alignment="center"))

if __name__ == "__main__":
    ft.app(target=main)
