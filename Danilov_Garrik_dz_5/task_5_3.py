# Задание 3

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors, klasses):
    if len(tutors) == len(klasses):
        return ((tutor, klass) for tutor, klass in zip(tutors, klasses))
    else:
        len_klasses = len(klasses)
        index = 0
        for tutor in tutors:
            if index < len_klasses:
                yield tutor, klasses[index]
                index += 1
            else:
                yield tutor, None


generator = check_gen(tutors, klasses)
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)
