import pynecone as pc
from ..base_state import State

def menu():
    return pc.menu(
        pc.menu_button(pc.button(pc.icon(tag="hamburger"), variant="ghost", padding_top="0.2em")),
        pc.menu_list(
            pc.link(pc.menu_item("Homework"), href="/homework"),
            pc.link(pc.menu_item("Exams"), href="/exams"),
            pc.link(pc.menu_item("Marks"), href="/marks"),
            pc.menu_divider(),
            pc.link(
                pc.menu_item(
                    pc.hstack(pc.icon(tag="settings"), pc.text("Settings"))
                ),
                href="/settings",
            ),
            bg="rgba(0, 0, 0, 0)",
            shadow="2xl",

            #background_image=r"radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)"
        ),
    )

def navbar():
    return pc.box(
        pc.hstack(
            pc.hstack(
                menu(),
                pc.image(src="/edookit.png", width="50px", padding_right="0.5em", padding_left="0.5em"),
                pc.heading("Edookit"),
                pc.heading(
                    "+",
                    background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                    background_clip="text",
                    font_weight="bold",
                ),
            ),
            pc.hstack(
                pc.button(
                    pc.icon(tag="moon"),
                    on_click=pc.toggle_color_mode,
                ),
                pc.link(
                    pc.button(
                        pc.icon(tag="settings"),
                    ),
                    href="/settings",
                    button=True
                ),
            ),

            justify="space-between",
            border_bottom="gray",
            padding_x="1em",
            padding_y="1em",
            #bg="rgba(0, 0, 0, 0.15)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
        #shadow="md",
    )

