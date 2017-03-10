from django.shortcuts import render
from django.contrib import admin


def index(request):
    # pub_date컬럼(필드)를 기준으로 내림차순 정렬한 결과를 latest_question_list에 할당)

    return render(request, 'index/index.html', {})
