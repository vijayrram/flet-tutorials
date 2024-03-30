import flet as ft
from flet_core.control_event import ControlEvent       


class sign_up:
    def __init__(self, title: str = "Sign Up", size: int = 400):
        self.title: str = title
        self.size: int = size
        self.page: ft.Page | None = None

    def run(self, page: ft.Page) -> None:
        """Method to run the counter application.

        Args:
            page (ft.Page): The page to be rendered on screen.
        """

        page.title = self.title
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window_width = self.size
        page.window_height = self.size

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

        self.page = page

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

    def validate(self, event: ControlEvent) -> None:
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
    SIGN_UP: sign_up = sign_up()
    ft.app(target=SIGN_UP.run)




