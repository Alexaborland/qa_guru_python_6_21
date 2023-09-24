from conftest import api_catfact


def test_get_list_with_limit():
    limit = 10
    response = api_catfact(method="get",
                           url="/breeds",
                           params={"limit": limit}
                           )

    assert response.status_code == 200
    assert len(response.json()['data']) == limit


def test_get_list_with_limit_and_breed():
    breed = "American Shorthair"
    limit = 10
    response = api_catfact(method="get",
                           url="/breeds",
                           params={"limit": limit,
                                   "breed": breed})

    assert response.status_code == 200
    assert response.json()['data'][4]['breed'] == breed


def test_get_random_fact():
    max_length = 20
    response = api_catfact(method="get",
                           url="/fact",
                           params={"max_length": max_length}
                           )

    assert response.status_code == 200
    assert response.json()['fact'] is not None


def test_get_list_of_facts():
    limit = 10
    max_length = 20
    response = api_catfact(method="get",
                           url="/fact",
                           params={"max_length": max_length,
                                   "limit": limit}
                           )

    assert response.status_code == 200
    assert response.json()['fact'] is not None


def test_get_random_fact_with_zero_length():
    max_length = 20
    response = api_catfact(method="get",
                           url="/fact",
                           params={"max_length": max_length}
                           )

    assert response.status_code == 200
    assert response.json()['fact'] == 'Cats have 3 eyelids.'
