import pynecone as pc

config = pc.Config(
    app_name="edooplus",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
