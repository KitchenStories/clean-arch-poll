from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.use_cases import poll as use_cases
from infrastructure.web import repo_instances


def poll_list(request):
    uc = use_cases.PollListUseCase(repo_instances.poll_repo)
    questions = uc.execute()

    return JsonResponse(
        [q.dict() for q in questions],
        safe=False
    )


def poll_detail(request, question_id):
    uc = use_cases.PollGetUseCase(repo_instances.poll_repo)
    question = uc.execute(question_id)

    return JsonResponse(question.dict(), safe=False)


@csrf_exempt
def vote_choice(request, choice_id):
    uc = use_cases.PollVoteUseCase(repo_instances.choice_repo)
    choice = uc.execute(choice_id)

    return JsonResponse(choice.dict(), safe=False)
