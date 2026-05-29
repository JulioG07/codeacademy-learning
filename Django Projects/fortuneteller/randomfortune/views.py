from django.shortcuts import render
import random

fortuneList = [
  "Your crush will ask you out",
  "Mexico is waiting!",
  "You will ace that summer intership!!",
  "You will be an effective communicator!",
  "Continue the grind, king!"
]

# Create your views here.
def fortune(request):
  fortune = random.choice(fortuneList)
  context = {
    "fortune" : fortune
  }
  return render(request, "randomfortune/fortune.html", context)