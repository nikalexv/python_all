import random
import math

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай", "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет", "Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать", "Перспективы не очень хорошие",  "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Ask me, i know eveything')
print('Enter your name ?')
print('Hi,', input())

while True:
    print('Enter your question')
    input()
    print(random.choice(answers))
    print('Another question?')
    if input().lower() == 'no':
        print('Good luck')
        break
    else:
        continue


