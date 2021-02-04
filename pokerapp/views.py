from django.shortcuts import render
from django.http import HttpResponse
from pokerapp.models import Deck, Party
from random import choices
import string
import json


def index(request):
    return HttpResponse("Welcome to Pokurses!")
# Create your views here.


def getAllCards(request):
    if request.method == 'GET':
        deck = Deck()
        deck.populate_full()
        return HttpResponse(deck.cards_json, status=200)


def create(request):
    if request.method == "GET":
        party = Party.objects.create()
        join_code = ''.join(choices(string.ascii_uppercase + string.digits, k=8))
        party.join_code = join_code
        deck = Deck.objects.create()
        deck.populate_full()
        party.deck = deck
        return HttpResponse(json.dump(party), status=200)



