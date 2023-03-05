"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

from .base_state import State

from .pages.index import index
from .pages.settings import settings

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"



# Add state and page to the app.
app = pc.App(state=State)

app.add_page(index,
    title="Edookit+",
    description="Edookit wrapper written in python providing better experience and QOL features.",
    image="/edookit.png",
)

app.add_page(settings, route="/settings",
    title="Edookit+",
    description="Edookit wrapper written in python providing better experience and QOL features.",
    image="/edookit.png",
)

app.compile()
