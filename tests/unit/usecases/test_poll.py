from pytest import fixture

from core.use_cases import poll as use_cases


@fixture
def m_repo(mocker):
    repo = mocker.MagicMock()
    repo.__enter__.return_value = repo
    return repo


def test_poll_add_use_case(sent, m_repo):
    uc = use_cases.PollAddUseCase(m_repo)
    uc.execute(sent.entity)

    m_repo.add.assert_called_once_with(sent.entity)
    m_repo.__enter__.assert_called_once_with()
    m_repo.__exit__.assert_called_once()


def test_poll_get_use_case(sent, m_repo):
    m_repo.get.return_value = sent.entity

    uc = use_cases.PollGetUseCase(m_repo)
    resp = uc.execute(sent.uid)

    assert resp == sent.entity
    m_repo.get.assert_called_once_with(sent.uid)


def test_poll_list_use_case(sent, m_repo):
    m_repo.list.return_value = sent.entities_list
    uc = use_cases.PollListUseCase(m_repo)
    resp = uc.execute()

    assert resp == sent.entities_list
    m_repo.list.assert_called_once_with()


def test_choice_vote_use_case(mocker, sent, m_repo):
    m_choice = mocker.Mock()
    m_repo.get.return_value = m_choice
    uc = use_cases.PollVoteUseCase(m_repo)
    resp = uc.execute(sent.choice_id)

    assert resp == m_choice
    m_repo.get.assert_called_once_with(sent.choice_id)
    m_repo.add.assert_called_once_with(m_choice)
    m_repo.__enter__.assert_called_once_with()
    m_repo.__exit__.assert_called_once()
    m_choice.vote.assert_called_once_with()
