from django.shortcuts import render, redirect


def survey(request):
    if request.user.is_authenticated:
        return render(request,'survey/quiz1.html')
    else:
        return redirect('login')

def pattern(request):
    return render(request, 'survey/pattern.html')  