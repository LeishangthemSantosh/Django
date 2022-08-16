import re
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
# def januray(request):
#     return HttpResponse('This is january')
monthly_challenge = {
    'january': 'Some Text for January',
    'february': 'Some Text for Febuary',
    'march': 'Some Text for March',
    'april': 'Some Text for April',
    'may': 'Some Text for May',
    'june': 'Some Text for June',
    'july': 'Some Text for July',
    'august': 'Some Text for August',
    'september': 'Some Text for September',
    'october': 'Some Text for October',
    'november': 'Some Text for November',
    'december': None
}
def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse('monthly-challenge', args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("The Input Number Is invalid")
    redirect_month = months[month - 1]
    redirect_path = reverse('monthly-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenges(request, month):
    try:
        challenges_text = monthly_challenge[month]
        return render(request, "challenges/challenges.html", 
        {
            "month_name": month.capitalize(),
            "text": challenges_text
        })
        # response_data = f"<h1>{challenges_text}</h1>"
        # response_data = render_to_string("challenges/challenges.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()

        # return HttpResponseNotFound("This Month is Invalid")

    # challenges_text = None
    # if month == 'january':
    #     challenges_text = "This is january"
    # elif month == 'febuary':
    #     challenges_text = "This is febuary"
    # elif month == 'march':
    #     challenges_text = "This is march"
    # else:
    #     return HttpResponseNotFound("Not Found")

    # return HttpResponse(challenges_text)
