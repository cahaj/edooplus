import pynecone as pc
from ..helpers.navbar import navbar
from ..base_state import State

class SwitchState(State):
    remember: bool = False

    def change_remember(self, checked):
        self.remember = checked


def settings():
    return pc.center(
        navbar(),
        pc.box(
            pc.vstack(
                pc.heading("Settings", size="lg", padding_bottom="1em"),
                pc.hstack(
                    pc.text("Remember login info", padding_right="0.3em"),
                    pc.switch(is_checked=SwitchState.remember, on_change=SwitchState.change_remember),
                ),
                padding="2em",
                shadow="2xl",
                border_radius="lg",
                
            ),
            padding="7em"
        ),

        width="100%",
        height="100vh",
        background=r"radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )