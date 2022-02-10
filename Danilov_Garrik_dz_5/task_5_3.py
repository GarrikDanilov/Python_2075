# Задание 3

tutors = ['Иван', 'Анастасия', 'Петр',
          'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Мария', 'Ольга'
          ]

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А',
           '10Б', '9А'
           ]


def check_gen(tutors, klasses):
    if len(tutors) == len(klasses):
        for tutor, klass in zip(tutors, klasses):
            yield tutor, klass
    else:
        max_index = min(len(tutors), len(klasses))
        dict_tutor = {tutor: klass for tutor, klass in zip(tutors[:max_index], klasses[:max_index])}
        for tutor in tutors:
            yield tutor, dict_tutor.get(tutor)


generator = check_gen(tutors, klasses)
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)
