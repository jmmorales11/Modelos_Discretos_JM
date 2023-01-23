from collections import Counter

def solution(S):
    # write your code in Python 3.6
    dic = dict(Counter(S).items())
    print(dic)
    freq = sorted(dic.values(),reverse=True)
    print(freq)
    d = 0
    auxitem = set()
    auxitem.add(freq[0])
    for i in freq[1:]:
        while i in auxitem and i > 0:
            i -=1
            print(i)
            d +=1
        auxitem.add(i)
        print("a",auxitem)
    return (d)


if __name__ == '__main__':
    S=['a','a','b','b','c','d','a','f','f']
    print(solution(S))
