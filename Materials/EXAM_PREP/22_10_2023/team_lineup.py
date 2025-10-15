def team_lineup (*args):
    players = {}
    reuslt = []

    for player,country in args:
        if country not in players.keys():
            players[country] = []
        players[country].append(player)

    sorted_players = sorted(players.items(),key = lambda x: (-len(x[1]),x[0]))
    
    for country,players in sorted_players:
        reuslt.append(f'{country}:')
        for player in players:
            reuslt.append(f'  -{player}')

    return '\n'.join(reuslt)




print(team_lineup(("Harry Kane", "England"),("Manuel Neuer", "Germany"),("Raheem Sterling", "England"),
                  ("Toni Kroos", "Germany"),("Cristiano Ronaldo", "Portugal"),
                  ("Thomas Muller", "Germany")))

print('#########################################################################################')

print(team_lineup(("Lionel Messi", "Argentina"),("Neymar", "Brazil"),("Cristiano Ronaldo", "Portugal"),
                  ("Harry Kane", "England"),("Kylian Mbappe", "France"),("Raheem Sterling", "England")))

print('#########################################################################################')

print(team_lineup(("Harry Kane", "England"),("Manuel Neuer", "Germany"),("Raheem Sterling", "England"),
                  ("Toni Kroos", "Germany"),("Cristiano Ronaldo", "Portugal"),("Thomas Muller", "Germany"),
                  ("Bruno Fernandes", "Portugal"),("Bernardo Silva", "Portugal"),("Harry Maguire", "England")))

