from django.shortcuts import render


people1 = [
    {
        'id': 1,
        'name': 'Bob Smith',
        'age': 35,
        'country': 'USA'
    },
    {
        'id': 2,
        'name': 'Martha Smith',
        'age': 60,
        'country': 'USA'
    },
    {
        'id': 3,
        'name': 'Fabio Alberto',
        'age': 18,
        'country': 'Italy'
    },
    {
        'id': 4,
        'name': 'Dietrich Stein',
        'age': 85,
        'country': 'Germany'
    }
]


def people(request):
    context = {'people': people1}

    return render(request, 'main/main.html', context)


def people_id(request, id_num):
    for person in people1:
        if person['id'] == (int(id_num)):
            person_info = person
            return render(request, 'main/ids.html', {'person': person_info})
