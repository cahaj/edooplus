import pynecone as pc

from ..base_state import State
from ..state.user import LoginState

def login_prompt():
    return pc.box(
            pc.vstack(
                pc.heading("Not logged in", size="lg"),
                pc.text("You must be logged in to do that!", padding_bottom="1em"),
                pc.hstack(
                        pc.link(pc.button("Log in"), href=f"/login"),

                ),
                padding="2em",
                shadow="2xl",
                border_radius="lg",
                
            ),
            padding="7em"
        )