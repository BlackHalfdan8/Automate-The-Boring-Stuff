import random
import zombiedice

class AdaptiveZombie:
    def __init__(self, name):
        self.name = name
        self.brains = 0
        self.shotguns = 0

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            brains_rolled = diceRollResults['brains']
            shotguns_rolled = diceRollResults['shotgun']

            self.brains += brains_rolled
            self.shotguns += shotguns_rolled

            # If we have enough brains, stop rolling
            if self.brains >= 3:
                break

            # If we have more than 2 shotguns, stop rolling
            if self.shotguns >= 2:
                break

            # If we have 1 shotgun and 1 brain, take a risk and roll again
            if self.shotguns == 1 and self.brains == 1:
                decision = zombiedice.roll()  # Roll again and check the result
                if decision is None:
                    break  # Stop rolling if we got a shotgun

            diceRollResults = zombiedice.roll()  # Roll again

        print(f'{self.name} collected {self.brains} brains and {self.shotguns} shotguns.')

class ZombieDiceBot:
    def __init__(self):
        self.brains = 0
        self.shotguns = 0

    def turn(self, gameState):
        while True:
            dice_roll = zombiedice.roll()  # Roll three dice by default
            if dice_roll['brains']:
                self.brains += dice_roll['brains']
                print('Got a brain!')
            if dice_roll['shotgun']:
                self.shotguns += dice_roll['shotgun']
                print('Got a shotgun!')
                if self.shotguns >= 2:
                    print('Two shotguns, turn over!')
                    break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    AdaptiveZombie(name='Adaptive Zombie Bot'),
    ZombieDiceBot(),  # Add your ZombieDiceBot here
)

zombiedice.runWebGui(zombies=zombies, numGames=1000)
