from typing import List

from django.db import models
import json
from random import shuffle
# Create your models here.

values = {
    '1': 'Ace',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': 'Jack',
    '11': 'Queen',
    '12': 'King'
}


suits = {
    '1': 'Diamonds',
    '2': 'Spades',
    '3': 'Clubs',
    '4': 'Hearts'
}


class Card(object):
    def __init__(self, suit, height):
        self.suit = suit
        self.height = height

    def get_suit(self) -> int:
        return self.suit

    def get_height(self) -> int:
        return self.height

    def get_suit_name(self) -> str:
        return suits[str(self.suit)]

    def get_height_name(self) -> str:
        return values[str(self.height)]


class Deck(models.Model):
    id = models.AutoField(primary_key=True)
    cards_json = models.JSONField(null=True)

    def populate_full(self):
        cards_list = []
        for suit in range(1, 5):
            for value in range(1, 13):
                cards_list.append(Card(suit, value))
        shuffle(cards_list)
        self.cards_json = json.dumps(json.dumps([card.__dict__ for card in cards_list]))


class Party(models.Model):
    id = models.AutoField(primary_key=True)
    join_code = models.CharField(max_length=64)
    deck = models.OneToOneField(Deck, on_delete=models.SET_NULL, null=True)


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    party = models.OneToOneField(Party, on_delete=models.SET_NULL, null=True)
    deck = models.OneToOneField(Deck, on_delete=models.SET_NULL, null=True)

