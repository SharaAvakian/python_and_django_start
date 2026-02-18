from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
# Create your views here.
monthly_challenges = {
    "january": "start the year strong: do 20 push-ups every morning.",
    "february": "write down one thing you're grateful for each day.",
    "march": "take a 15-minute walk outside daily to enjoy spring.",
    "april": "drink at least 2 liters of water every day.",
    "may": "do 30 squats every day to get your legs ready for summer.",
    "june": "try a new hobby or skill this month, even if just for 15 mins/day.",
    "july": "do 10 minutes of stretching each morning.",
    "august": "read at least 10 pages of a book every day.",
    "september": "do 15 burpees daily to boost your cardio.",
    "october": "write down one positive thing about your day before bed.",
    "november": "try a new healthy recipe every week.",
    "december": "reflect on your year and plan one goal for next year."
}
def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):

        return HttpResponseBadRequest("Invalid month")

    redirect_month = months[month -1]
    redirect_path = reverse("month_", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseBadRequest("Invalid month")



