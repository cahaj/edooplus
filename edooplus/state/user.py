from ..base_state import State

class LoginState(State):
    logged_in: bool = False

    def login(self):
        self.logged_in = True

    def logout(self):
        self.logged_in = False
