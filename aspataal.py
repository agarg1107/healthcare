import flet as ft


def main(page: ft.Page):
    page.window_full_screen
    page.window_resizable = False  # window is not resizable
    page.update()
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.START

    page.bgcolor = ft.colors.WHITE
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.AMBER_500,
                )
            )
        return items

    def column_with_alignment(align: ft.MainAxisAlignment):
        return ft.Column(
            [
                ft.Container(
                    content=ft.Column(items(3), alignment=align),
                    bgcolor=ft.colors.AMBER_100,
                    height=580,
                ),
            ]
        )
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(

        ft.Container(
            image_src='images.jpg',
            image_fit=ft.ImageFit.COVER,
            expand=True,
            content=ft.Container(
                ft.ResponsiveRow(
                    [
                        ft.ResponsiveRow(
                            [
                                ft.ResponsiveRow([
                                    ft.Container(
                                        bgcolor=ft.colors.WHITE
                                        , width=page.window_width,
                                        alignment=ft.alignment.center_left,
                                        height=50,
                                        content=ft.Container(
                                            image_src='images.jpg',
                                            width=50,
                                            height=50, ),
                                    )
                                ]),
                            ]
                        ),
                        ft.Row(
                            [
                                    ft.Column(
                                    [
                                        column_with_alignment(ft.MainAxisAlignment.CENTER),
                                    ]
                                ),
                                ft.Container(
                                    bgcolor=ft.colors.GREY,
                                    height=100,
                                    width=100,
                                )


                            ]
                        )
                    ]
                )

            )
        ),

    )


ft.app(target=main)
