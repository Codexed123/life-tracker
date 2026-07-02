import flet as ft


def main(page: ft.Page):
    page.title = "My Basic App"
    page.add(ft.Text("Hello world"))

    field = ft.TextField(label="uhm your username")
    def button_clicked(e):
        page.add(ft.Text(f"Im pressed and your name is {field.value}"))

    page.add(
        field,
        ft.ElevatedButton("Click me", on_click=button_clicked))
ft.run(main)
