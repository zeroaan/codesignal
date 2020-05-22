
def electionsWinners(votes, k):
    # for 문 안에 max(votes)를 해줌으로써 시간초과가 일어남.
    # votes.length <= 10^5
    
    # if k == 0 and votes.count(max(votes)) == 1:
    #     return 1
    # else:
    #     return len([v for v in votes if v+k > max(votes)])

    top = max(votes)
    if k == 0 and votes.count(top) == 1:
        return 1
    else:
        return len([v for v in votes if v+k > top])

