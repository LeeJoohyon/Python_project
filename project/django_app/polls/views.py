from django.http import HttpResponse
from django.shortcuts import render,redirect


from .models import Question, Choice


def index(request):
    # pub_date컬럼(필드)를 기준으로 내림차순 정렬한 결과를 latest_question_list에 할당)
    latest_question_list = Question.objects.order_by('-pub_date')

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

    # template = loader.get_template('polls/index.html')
    # # 템플릿  context와 request 객체를 사용해서 render 해준 결과를 돌려줌
    # context = {
    #     # 'latest question list'라는 키에 값을 할당, 해당 키로 템플릿에서 사용가능하다.
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 돌려줄 문자열을 작성
    output = ','.join([q.question_text for q in latest_question_list])
    output2 = ''
    for q in latest_question_list:
        output2 += q.question_text + ','
    output2 = output2[:-3]

    return HttpResponse(output2)


def detail(request, question_id):
    if request.method == 'POST':
        # value = request.POST['choice']
        # print(value)
        # 1번
        choice_id = request.POST['choice']
        choice = Choice.objects.get(id=choice_id)

        # 2번
        choice.votes += 1
        choice.save()

        # 3번
        return redirect('polls:results', question_id=question_id)

    # return HttpResponse(value)

    else:
        question = Question.objects.get(id=question_id)
        context = {
            'question': question
        }
        return render(request, 'polls/detail.html', context)

def results(request, question_id):

    question = Question.objects.get(id=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
