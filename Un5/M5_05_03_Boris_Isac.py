import pandas
import csv
'''
teste with small csv file(30reg) titulos comuns
fileLol = open('lol.csv')
dFlol = pandas.read_csv(fileLol)
a = pandas.pivot_table(dFlol,index=['title', 'year'], aggfunc='size')
print(a.nlargest(5))
'''
#read csv files
fileElenco = open('05_05_imdb_elenco.csv')
fileTitulos = open('05_05_imdb_titulos.csv')
dFtitle = pandas.read_csv(fileTitulos)
dFElenco = pandas.read_csv(fileElenco)
'''
#first five regists TITULO
print('File 05_05_imdb_titulos.csv,'.upper(), len(dFtitle), 'Regists'.upper())
print(dFtitle.head())

#first five regists ELENCO
print('\nFile 05_05_imdb_elenco.csv,'.upper(), len(dFElenco), 'Regists'.upper())
print(dFElenco.head())

print("\n5 oldest regists".upper())
print(dFtitle.nsmallest(5, 'year'))

draculaFilms = dFtitle[dFtitle['title'].str.contains('Dracula')]
print("\nDracula Films:".upper(), len(draculaFilms))
pandas.set_option('display.max_rows', None)
print(draculaFilms)
pandas.set_option('display.max_row',10)
'''


print('\n5 Titolos mais comiuns'.upper()) #no csv file que eu criei funciona, aqui nao. pode me dar alguma dica
repeatList = dFtitle['title'].value_counts()
print(repeatList.head(10))




'''
romeoAndJulieta =  dFtitle[dFtitle['title'].str.contains('Romeo and Juliet')]
fRAndJ = romeoAndJulieta.nsmallest(1, 'year')
print('\nRomeo And Juliete, first film')
print(fRAndJ)

pandas.set_option('display.max_rows', None)
print('Sorted Exorcist!'.upper())
exarcistList = dFtitle[dFtitle['title'].str.contains('Exorcist')]
print(exarcistList.sort_values('year'))
pandas.set_option('display.max_rows', 10)

print('Films made in 1950: ',(len(dFtitle[dFtitle['year'] == 1950])))
dec50 = dFtitle[(dFtitle['year'] > 1950) & (dFtitle['year'] <= 1959)]
print('Films made in 1950-1959: ',len(dec50))

print('\nThe Godfather'.upper())
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
theGodfatherListTotal = dFElenco[
    ((dFElenco['title'] == 'The Godfather') |
     (dFElenco['title'] == 'The Godfather: Part II') |
     (dFElenco['title'] == 'The Godfather: Part III')
    )
]
print(theGodfatherListTotal)
alPachino = dFElenco[(dFElenco['name'] == 'Al Pacino') & ((dFElenco['title'] == 'The Godfather') |
     (dFElenco['title'] == 'The Godfather: Part II') |
     (dFElenco['title'] == 'The Godfather: Part III'))]

#I have used NAME column because characters in deferents films are deferents
#exemple michael corleone, Michael Corleone, Don michael Corleone
allRoles = pandas.pivot_table(theGodfatherListTotal, index='name', aggfunc='size')
print(allRoles)

print('\nDracula')
filmDracula1958 = dFElenco[
    (dFElenco['title'] == 'Dracula') &
    (dFElenco['year'] == 1958)
]
print(filmDracula1958.sort_values(by='n', ascending=True))


bruceWayne = dFElenco[
    dFElenco['character'].str.contains('Bruce Wayne') &
    (dFElenco['type'] == 'actor') &
    pandas.notna(dFElenco['n'])
]
print('Bruce Wayne protogonist:',len(bruceWayne))

rDNiro = dFElenco[dFElenco['name'].str.contains('Robert De Niro')]

print('Total films with Robert de Niro:',len(rDNiro))


charltonHeston = dFElenco[
    (dFElenco['name'] == 'Charlton Heston') &
    (dFElenco['n'] == 1) &
    ((dFElenco['year'] >= 1960) & (dFElenco['year'] <=1969))
]
print(charltonHeston.sort_values(by='year', ascending=False))


actor = dFElenco[dFElenco['type'] == 'actor']
actriz = len(dFElenco)-len(actor)
print('actor:',len(actor), 'actriz:',actriz)
'''