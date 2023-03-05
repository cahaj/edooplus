import pynecone as pc
from ..helpers.navbar import navbar
from ..helpers.not_logged import login_prompt
from ..state.user import LoginState

def index():
    return pc.center(
        navbar(),
        pc.cond(
            LoginState.logged_in,
            pc.box(
                pc.vstack(
                    pc.text(f"Hello world!", padding_bottom="1em"),
                    padding="2em",
                    shadow="2xl",
                    border_radius="lg",
                    
                ),
                padding="7em"
            ),
            login_prompt(),
        ),


        width="100%",
        height="100vh",
        background=r"radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )