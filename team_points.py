try:
    with open('players.txt', 'r') as file:
        scores = {}
        teams = {}
        for line in file:

            if line!='':
               line = line.rstrip().split(' ')
               scores[line[0]] = line[1]
               if line[2] in teams:
                   teams[line[2]].append(line[0])
               else:
                   teams[line[2]] = [line[0]]



        pbt = {}   
        if len(teams) > 0:
            for team in teams:
                score = 0
                for player in teams[team]:
                    score += int(scores[player])
                pbt[team] = score

        print('Scores:', scores)
        print('Teams:', teams)
        print('Points by team:', pbt)

except FileNotFoundError:
    print('Something went wrong when opening the file: file not found')
