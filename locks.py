class cls_locks:
    def __init__(self):
        self.key_states = {}


    def set_key_state(self, key, state):
        self.key_states[key] = state

    def get_key_state(self, key):
        return self.key_states.get(key, False)