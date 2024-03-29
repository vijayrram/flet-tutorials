"""Script for the Counter app."""

import flet as ft


def main(page: ft.Page):
    """Method to run the Counter application.

    Args:
        page (ft.Page): _description_
        title (str, optional): _description_. Defaults to "Counter".
    """

    page.title = "Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_field: ft.TextField = ft.TextField(
        value=str(0),
        text_align=ft.TextAlign.RIGHT,
        width=100
    )

    # pylint: disable = unused-argument
    def click_plus(event):
        """Method to run if '+' is clicked.

        Args:
            event (_type_): Unused argument
        """

        text_field.value = str(int(text_field.value) + 1)
        page.update()

    # pylint: disable = unused-argument
    def click_minus(event):
        """Method to run if '+' is clicked.

        Args:
            event (_type_): Unused argument
        """

        text_field.value = str(int(text_field.value) - 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=click_minus),
                text_field,
                ft.IconButton(ft.icons.ADD, on_click=click_plus),
            ]
        )
    )


if __name__ == "__main__":
    ft.app(target=main)