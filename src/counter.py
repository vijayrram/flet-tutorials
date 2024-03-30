"""Script for the Counter app."""

import flet as ft  # type: ignore
from flet_core.control_event import ControlEvent  # type: ignore


class Counter:
    """Class for handling Counters."""

    def __init__(self, title: str = "Counter", start: int = 0, width: int = 100):
        self.title: str = title
        self.text_field: ft.TextField = ft.TextField(
            value=str(start),
            text_align=ft.TextAlign.RIGHT,
            width=width
        )
        self.page: ft.Page | None = None

    def run(self, page: ft.Page) -> None:
        """Method to run the counter application.

        Args:
            page (ft.Page): The page to be rendered on screen.
        """

        self.page = page
        self.page.title = self.title
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.page.add(
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=self.click_minus),
                    self.text_field,
                    ft.IconButton(ft.icons.ADD, on_click=self.click_plus),
                ]
            )
        )

    # pylint: disable = unused-argument
    def click_plus(self, event: ControlEvent) -> None:
        """Method to run if '+' is clicked.

        Args:
            event (ControlEvent): Unused argument
        """

        self.text_field.value = str(int(self.text_field.value) + 1)

        assert isinstance(self.page, ft.Page)
        self.page.update()

    # pylint: disable = unused-argument
    def click_minus(self, event: ControlEvent) -> None:
        """Method to run if '+' is clicked.

        Args:
            event (ControlEvent): Unused argument
        """

        self.text_field.value = str(int(self.text_field.value) - 1)

        assert isinstance(self.page, ft.Page)
        self.page.update()



if __name__ == "__main__":
    counter: Counter = Counter()
    ft.app(target=counter.run)
