def solution(n, words):
    answer = []
    check = [words[0]]
    
    for idx, word in enumerate(words[1:], start = 1):
        if word in check:
            return [idx%n + 1, idx//n + 1]
        if check[-1][-1] == word[0]:
            check.append(word)
        else:
            return [idx%n + 1, idx//n + 1]
        
    return [0, 0]
