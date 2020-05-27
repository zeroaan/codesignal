def alternatingSums(a):
    # team_1, team_2 = 0, 0
    
    # for i in range(len(a)):
    #     if i % 2 == 0:
    #         team_1 += a[i]
    #     else: team_2 += a[i]

    # return [team_1, team_2]

    return [sum(a[::2]), sum(a[1::2])]
