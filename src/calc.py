from button import CalcButton, DigitButton, ActionButton, ExtraActionButton
import flet as ft

def main(page: ft.Page):
    page.title = "Calculator App"
    current_input = ""
    result = ft.Text(value="0", size=32, weight="bold")

    def button_click(e):
        nonlocal current_input
        btn_text = e.control.text

        if btn_text == "AC":
            current_input = ""
            result.value = "0"
        elif btn_text == "=":
            try:
                current_input = str(eval(current_input))
                result.value = current_input
            except:
                result.value = "Error"
                current_input = ""
        else:
            current_input += btn_text
            result.value = current_input

        page.update()

    page.add(
        ft.Container(
            content=ft.Row(controls=[result], alignment="end"),
            padding=20
        ),
        ft.Row(
            controls=[
                ExtraActionButton("AC", on_click=button_click),
                ExtraActionButton("+/-", on_click=button_click),
                ExtraActionButton("%", on_click=button_click),
                ActionButton("/", on_click=button_click),
            ],
            expand=True,
        ),
        ft.Row(
            controls=[
                DigitButton("7", on_click=button_click),
                DigitButton("8", on_click=button_click),
                DigitButton("9", on_click=button_click),
                ActionButton("*", on_click=button_click),
            ],
            expand=True,
        ),
        ft.Row(
            controls=[
                DigitButton("4", on_click=button_click),
                DigitButton("5", on_click=button_click),
                DigitButton("6", on_click=button_click),
                ActionButton("-", on_click=button_click),
            ],
            expand=True,
        ),
        ft.Row(
            controls=[
                DigitButton("1", on_click=button_click),
                DigitButton("2", on_click=button_click),
                DigitButton("3", on_click=button_click),
                ActionButton("+", on_click=button_click),
            ],
            expand=True,
        ),
        ft.Row(
            controls=[
                DigitButton("0", on_click=button_click, expand=2),
                DigitButton(".", on_click=button_click),
                ActionButton("=", on_click=button_click),
            ],
            expand=True,
        )
    )

ft.app(target=main)
