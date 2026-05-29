from django.shortcuts import render
import random

fortuneList = [
  "Your crush will ask you out",
  "Mexico is waiting!",
  "You will ace that summer intership!!",
  "You will be an effective communicator!",
  "Continue the grind, king!"
]

meFacts = [
  "You are Venezuelan",
  "You are 19 years old",
  "You go to Lehigh University",
  "You fence and play volleyball for fun",
  "You love Romeo Santos"
]

imageList = [
  "/media/crush.jpg",
  "/media/mexico.webp",
  "/media/internship.jpg",
  "/media/yapping.jpg",
  "/media/king.webp",
]

# Create your views here.
def fortune(request):
  fortune = random.choice(fortuneList)
  fortune_index = fortuneList.index(fortune)  # index of the selected fortune

  context = {
    "message" : "Here is your fortune",
    "fullname" : "Julio Goitia",
    "fortune" : fortune,
    "img" : imageList[fortune_index]
  }
  return render(request, "randomfortune/fortune.html", context)

def bio(request):
  fact = random.choice(meFacts)
  context = {
    "message" : "Fun fact about ",
    "fullname" : "Julio Goitia",
    "fortune" : fact
  }
  return render(request, "randomfortune/fortune.html", context)