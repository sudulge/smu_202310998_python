import pickle
import os

def input_scores():
    scores = []
    cnt = 1
    while True:
        score = input(f'#{cnt}? ')
        if score == '-1':
            break
        scores.append(int(score))
        cnt += 1
    return scores

def get_average(scores):
    sum_ = sum(scores)
    average = sum_/len(scores)
    return average

def show_scores(scores):
    print('개인점수: ', end='')
    for score in scores:
        print(score, end=' ')


filepath = 'score.bin'

if os.path.exists(filepath):
    with open(filepath, 'rb') as file:
        print('[파일 읽기]\n')
        print('[점수 출력]')
        scores = pickle.load(file)
        show_scores(scores)
        print(f'평균: {get_average(scores):.1f}')
        
else:
    with open(filepath, 'wb') as file:
        print('[점수 입력]')
        scores = input_scores()
        print('[점수 출력]')
        show_scores(scores)
        print(f'평균: {get_average(scores):.1f}')
        pickle.dump(scores, file)