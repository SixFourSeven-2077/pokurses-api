from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from pokerapp.models import Deck, Party, Player
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
        party = Party()
        join_code = ''.join(choices(string.ascii_uppercase + string.digits, k=6))
        party.join_code = join_code
        deck = Deck()
        deck.populate_full()
        party.deck = deck

        deck.save()
        party.save()

        return HttpResponse(serializers.serialize('json', [party,], cls=DjangoJSONEncoder), status=200)


def join(request, code):
    for party in Party.objects.all():
        print(party.join_code)
    if request.method == "GET":
        try:
            party = Party.objects.get(join_code=code)
            players = Player.objects.filter(party=party.id)
            return HttpResponse(serializers.serialize('json', players, cls=DjangoJSONEncoder), status=200)
        except Party.DoesNotExist:
            return HttpResponse(status=404)










