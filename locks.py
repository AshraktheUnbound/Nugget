class cls_locks:
    def __init__(self):
        self.main_display = True
        self.inventory_display = False
        self.key_pressed = False

    def inventory_toggle(self):
        self.main_display = not self.main_display
        self.inventory_display = not self.inventory_display