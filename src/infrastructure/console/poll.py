from core.use_cases import poll as use_cases

from infrastructure.web import repo_instances


def list_polls():
    uc = use_cases.PollListUseCase(repo_instances.mem_poll_repo)
    polls = uc.execute()

    print('##')
    for question in polls:
        print('name:', question.name)
        print('choices:', [(ch.text, ch.votes) for ch in question.choices])


if __name__ == '__main__':
    list_polls()
