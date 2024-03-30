"""Script for the Counter app."""

import flet as ft  # type: ignore
from flet_core.control_event import ControlEvent  # type: ignore


class SignUp:
    """Class for handling Sign Up screen."""

    def __init__(self, title: str = "Sign Up", size: int = 400):
        self.title: str = title
        self.size: int = size
        self.page: ft.Page | None = None

    def run(self, page: ft.Page) -> None:
        """Method to run the counter application.

        Args:
            page (ft.Page): The page to be rendered on screen.
        """

        self.page = page
        self.page.title = self.title
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.window_width = self.size
        self.page.window_height = self.size

        self.textfield_username: ft.TextField = ft.TextField(
            label="username",
            text_align=ft.TextAlign.LEFT,
            width=self.size // 2,
        )
        self.textfield_password: ft.TextField = ft.TextField(
            label="password",
            text_align=ft.TextAlign.LEFT,
            width=self.size // 2,
            password=True,
        )
        self.checkbox_terms: ft.Checkbox = ft.Checkbox(
            label="I have read the Terms and Conditions.",
            value=False,
        )
        self.button_submit: ft.ElevatedButton = ft.ElevatedButton(
            text="Sign Up",
            width=self.size // 2,
            disabled=True,
        )

        self.textfield_username.on_change = self.validate
        self.textfield_password.on_change = self.validate
        self.checkbox_terms.on_change = self.validate

        self.button_submit.on_click = self.submit

        page.add(
            ft.Row(
                controls=[
                    ft.Column(
                        [
                            self.textfield_username,
                            self.textfield_password,
                            self.checkbox_terms,
                            self.button_submit,
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # pylint: disable = unused-argument
    def validate(self, event: ControlEvent) -> None:
        """Method used to validate the status of the Sign Up button.

        Args:
            event (ControlEvent): Unused.
        """

        if all(
            [
                self.textfield_username.value,
                self.textfield_password.value,
                self.checkbox_terms.value,
            ]
        ):
            self.button_submit.disabled = False
        else:
            self.button_submit.disabled = True

        self.page.update()

    # pylint: disable = unused-argument
    def submit(self, event: ControlEvent) -> None:
        """Method to run when the Submit button is clicked.

        Args:
            event (ControlEvent): Unused.
        """

        self.page.clean()
        self.page.add(
            ft.Row(
                controls=[
                    ft.Text(
                        value=f"Welcome: {self.textfield_username.value}",
                        size=20,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )


if __name__ == "__main__":
    sign_up: SignUp = SignUp()
    ft.app(target=sign_up.run)
