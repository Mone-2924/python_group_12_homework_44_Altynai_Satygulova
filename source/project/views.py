from urllib.parse import parse_qs

from django.shortcuts import render

# Create your views here.

def index_view(request):
    context = {}

    if request.method == 'GET':
        return render(request, "index.html")

    elif request.method == 'POST':
        context = {
            'numbers': request.POST.get('numbers'),
        }
        print(context)

        # if context.get("numbers"):
        #     numbers_str = context["numbers"][0].split()
        #     user_num = Check(numbers_str)
        #     if user_num.check_len() == False:
        #         response_body += 'Please enter no more and no less than 4 numbers'
        #     elif user_num.checking_for_str() == False:
        #         response_body += 'Please enter a number'
        #     elif user_num.checking_for_numbers() == False:
        #         response_body += 'Each digit must be at least 0 and at most 9 <br>Please enter from 0 to 9'
        #     elif user_num.digit_matching_check() == False:
        #         response_body += 'Numbers must not be repeated <br>Please enter the numbers so that they do not repeat'
        #     else:
        #         result = Game.play(numbers_str, secret_nums)
        #         print(result)
        #         response_body += f"You got it right"
        return render(request, 'index.html', context)
