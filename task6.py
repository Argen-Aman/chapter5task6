class Gun:
    
    def __init__(self, bullet):
        self.bullet = bullet
    
    def reload(self, bullet):
        if bullet + self.bullet <= 30:
            self.bullet += bullet
            if self.bullet < 30:
                print (f'Reloaded to {bullet} bullet(s), now you have {self.bullet} bullet(s) in the magazine.')
            else:
                print ( f'Now magazine is full.' )
        else:
            self.bullet = 30
            print('Reached to maximum capacity of magazine.')
            print ( f'Now magazine is full.' )

    def fire(self, bullet):
        self.bullet -= bullet
        gun_work = 'Tah-' * bullet
        print(gun_work)
        print(f'Remaining bullet(s) in magazine: {self.bullet}')

class Soldier:
    def __init__(self, name):
        self.name = name
    
    def soldier_name(self, name):
        self.name = name
        print(f'I\'m {name}, universal soldier {name}!')

class Act_of_shooting(Soldier, Gun):
    def __init__(self, name, bullet):
        self.name = name
        self.bullet = bullet
        self.soldier_name(name)
        self.act(bullet)

    def act(self, bullet):
        shots = int(input('How many shot(s) I must to do at first: '))
        if shots <= self.bullet:
            self.fire(shots)
        else:
            self.fire(self.bullet)
            print('Magazine is empty.')

        bullets_to_reload = int(input('How many bullet(s) must be reloaded: '))
        self.reload(bullets_to_reload)
        shots2 = int(input('And now how many shot(s) do you want: '))
        if shots2 <= self.bullet:
            self.fire(shots2)
        else:
            self.fire(self.bullet)
            print('Magazine is empty.')
    
    def __str__(self):
        return 'Mission comleted.'

Ryan = Act_of_shooting('Ryan', 30)

print(Ryan)
