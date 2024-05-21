print(f'{'Использование %':-^50}')
team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %d!' %team1_num)
print('Итого сегодня в командах участников: %d и %d !' %(team1_num, team2_num))
print()

print(f'{'Использование format()':-^50}')
score_2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
team1_time = 85.4 * score_2
print('Волшебники данных решили задачи за {}c'.format(team1_time))
print()

txt = 'Использование f-строк'
print(f'{txt:-^50}')
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач')
challenge_result = 'Результат битвы: победа команды'
if score_2 > score_1:
    print(f'{challenge_result} Мастера кода!')
    pass
if score_2 < score_1:
    print(f'{challenge_result} Волшебники данных!')
    pass
if score_2 == score_1:
    print('Победила дружба!')

tasks_total = score_2 + score_1
team1_time = 1552.512
team2_time = 2153.31451
time_avg = (team2_time + team1_time) / tasks_total
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg:4.1f}  секунды на задачу!.')