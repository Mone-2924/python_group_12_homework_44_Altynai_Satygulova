from urllib.parse import parse_qs

from django.shortcuts import render

# Create your views here.
from project.check import Check, Game


counter = {'counter': 0,}

def index_view(request):
    context = {}
    secret_nums = [5, 1, 2, 9]
    if request.method == 'GET':
        return render(request, "index.html")

    elif request.method == 'POST':
        counter['counter'] += 1
        context = {
            'numbers': request.POST.get('numbers'),
        }


        u_number = context['numbers'].split()
        user_num = Check(u_number)
        if user_num.check_len() == False:
            context['result'] = 'Please enter no more and no less than 4 numbers'
        elif user_num.checking_for_str() == False:
            context['result'] = 'Please enter a number'
        elif user_num.checking_for_numbers() == False:
            context['result'] = 'Each digit must be at least 0 and at most 9 <br>Please enter from 0 to 9'
        elif user_num.digit_matching_check() == False:
            context['result'] = 'Numbers must not be repeated <br>Please enter the numbers so that they do not repeat'
        else:
            cow, bull = Game.play(u_number, secret_nums)
            context['bull'] = bull
            context['cow'] = cow

            counter['bull'] = context['bull']
            counter['cow'] = context['cow']
            if bull == 4:
                context['result'] = 'You got it right!'
            else:
                context['result'] = f'You got {bull} bulls, {cow} cows'
        print(counter)
        return render(request, 'index.html', context)

print(counter)
def history_view(request):
    context = {}
    context['counter'] = counter['counter']
    context['bull'] = counter['bull']
    context['cow'] = counter['cow']
    return render(request, 'history.html',context)