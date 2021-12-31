def solution(price, money, count):
    answer = -1
    while count > 0:
        money -= price * count
        count -= 1
    return 0 if money >= 0 else abs(money)