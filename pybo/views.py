# from django.http import HttpResponse # 질문 목록을 만들기 위해 삭제
from django.shortcuts import render, get_object_or_404
from .models import Question


# Create your views here.


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)