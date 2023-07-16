
def solution(number):
    if number % 9 == 0:
        return f'{number} is even'
    else:
        return f'{number} is odd'

if __name__ == '__main__':
    a = int(input())
    answer = solution(a)
    print(answer)