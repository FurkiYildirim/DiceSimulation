from os import system
from random import randint
from time import sleep
import click

"""
discord : ! Kontragerilla ღ ヅ#1019
instagram : furkii_yildiriim
"""

@click.command()
@click.option('--trys', default=1, prompt="enter try amount", help='trial amount')


class Dice:
    def __init__(self, trys):
        self.sites = [1, 2, 3, 4, 5, 6]
        self.shakes = []
        self.trys = trys
        self.shake()
        self.show()

    def shake(self):
        for _ in range(self.trys):
            self.shakes.append(self.sites[randint(0, 5)])

    def show(self):
        for i in self.shakes:
            print(f"Shaking...")
            sleep(3)
            system("cls")
            print(f"Dice is {i}")

Dice()
