# 3.Napisz program, który wczyta plik o nazwie players.csv i wygeneruje następujący raport:
# a.Top 3 graczy wg największej ilości zdobytych punktów
# b.Średnia wieku graczy
# c.Najczęściej występujące imię wśród graczy
# d.Średnia ilość punktów
# e.Maksymalna ilość punktów
# f.Minimalna ilość punktów
# g.Najstarszy gracz


import pandas as pd

filename = 'players.csv'
dataframe = pd.read_csv(filename)

print("What would like to check from your data?:")
print("1. Top 3 player scores")
print("2. Average age of players")
print("3. Most common name among players")
print("4. Average player score")
print("5. The biggest score")
print("6. The lowest score")
print("7. The oldest player")

choice = int(input('Please enter number: '))
while True:
    if choice < 1 and choice > 7:
        print('Please, enter correct number')
    elif choice == 1:
        print('Top 3 player scores are: \n', dataframe.nlargest(3, 'score'))
        break
    elif choice == 2:
        print('Average players age is', dataframe['age'].mean(), 'years.' )
        break
    elif choice == 3:
        separate_col = dataframe['name'].str.split(' ',n=1,expand=True)
        most_frequent = separate_col[0].value_counts().idxmax()
        print('Most common name among players is: ', most_frequent,) #w danych jest kilka imion, ktore wystepuja taka sama ilosc razy. Program losowo wypisuje imiona. Nalezy zawezic do kilku rekordow.
        break
    elif choice == 4:
        avg_score = dataframe['score'].mean()
        print('Average player score is ', avg_score, ' points.')
        break
    elif choice == 5:
        top_score = dataframe['score'].max()
        print('The biggest player score is: ', top_score, ' points.')
        break
    elif choice == 6:
        lowest_score = dataframe['score'].min()
        print('The lowest score is: ', lowest_score, ' points.')
        break
    elif choice == 7:
        oldest = dataframe['age'].max()
        print('The oldest player is: ', oldest, ' years old.')
        break
    else:
        break