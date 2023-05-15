
class cls_combatant:
    def __init__(self, name, troops, stats):
        self.name = name
        self.troops = troops
        self.str = stats[0]
        self.dex = stats[1]
        self.int = stats[2]

class cls_battle:
    def __init__(self):
        self.turn = 1
        self.team_a = []
        self.team_a.append(cls_combatant('Liu Bei', 300, (180, 25, 180)))
        self.team_a.append(cls_combatant('Zhang Fei', 150, (250, 25, 50)))
        self.team_a.append(cls_combatant('Guan Yu', 150, (180, 25, 200)))
        self.team_a.append(cls_combatant('Huang Zhong', 125, (165, 25, 150)))
        self.team_a.append(cls_combatant('Ma Chao', 135, (225, 25, 160)))
        self.team_a.append(cls_combatant('Xu Zhe', 110, (60, 25, 220)))

        self.team_b = []
        self.team_b.append(cls_combatant('Shao Khan', 350, (225, 25, 180)))
        self.team_b.append(cls_combatant('Mortimer', 225, (200, 25, 120)))
        self.team_b.append(cls_combatant('Yan Yan', 250, (180, 25, 30)))
        self.team_b.append(cls_combatant('Lu Bu', 300, (255, 25, 20)))
        self.team_b.append(cls_combatant('Dong Zhuo', 200, (160, 25, 160)))
        self.team_b.append(cls_combatant('Li Su', 150, (80, 25, 200)))

        self.run()

    def run(self):
        running = True
        while running:
            self.player_input()
            self.execute_turn()

    def player_input(self):
        pass

    def execute_turn(self):
        pass

