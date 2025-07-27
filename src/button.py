import flet as ft

class DigitButton(ft.ElevatedButton):
    def __init__(self, text, on_click=None, expand=1):
        super().__init__(text=text, on_click=on_click, expand=expand)

class ActionButton(ft.ElevatedButton):
    def __init__(self, text, on_click=None):
        super().__init__(text=text, on_click=on_click, style=ft.ButtonStyle(color=ft.Colors.ORANGE))

class ExtraActionButton(ft.ElevatedButton):
    def __init__(self, text, on_click=None):
        super().__init__(text=text, on_click=on_click, style=ft.ButtonStyle(color=ft.Colors.BLUE_GREY))

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, on_click=None, expand=1):
        super().__init__(text=text, on_click=on_click, expand=expand)
