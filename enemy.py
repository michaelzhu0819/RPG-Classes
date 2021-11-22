class enemy:
    def __init__(self):
        self.e_hp = 0
        self.e_att = 0
        self.name = "a"

    def assign_val(self):
        hp = self.e_hp
        return hp

    def assign_val_2(self):
        att = self.e_att
        return att

    def assign_name(self):
        name = self.name
        return name


class thief(enemy):
    def __init__(self):
        super(thief, self).__init__()
        self.e_hp = 100
        self.e_att = 20
        self.name = "thief"
        print("\nyou encountered a skinny theif! Doesn't look " +
              "like much but he might be dangerous")


class assasin(enemy):
    def __init__(self):
        super(assasin, self).__init__()
        self.e_hp = 60
        self.e_att = 50
        self.name = "assasin"
        print("\nAn assasin appeared in front of you, " +
              "you really don't want to be touched by his weapons")


class swat_soul(enemy):
    def __init__(self):
        super(swat_soul, self).__init__()
        self.e_hp = 200
        self.e_att = 10
        self.name = "swat soul"
        print("\nYou bumped into a well armored apponent, " +
              "looks like it's going to be a long fight")


class emperor(enemy):
    def __init__(self):
        super(emperor, self).__init__()
        self.e_hp = 240
        self.e_att = 50
        self.name = "the emperor"
        print("\nBow before the mighty emperor..." +
              "you refused and now he is mad(by the way he might be a boss)")
