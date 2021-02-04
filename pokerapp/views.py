from django.shortcuts import render
from django.http import HttpResponse
from pokerapp.models import Deck
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
    if request.method == "POST":
        data = json.loads(request.body)
        name = data["name"]

