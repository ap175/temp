# -*- coding: utf-8 -*-
__author__ = 'Andrzej'
'''
Notatka napisana w postaci kodu Py wersja 2.
Program można uruchomić poleceniem:
> python spotkanie_2015-10-28.py
'''

class zeroweSpotkanie:
    '''
    Notatki z zebrania grupy zakładowej Py
    Spotkanie z dnia 2015-10-28
    '''

    def __init__(self):
        '''Inicjowanie klasy na pusto'''
        pass

    def zdalnaPraca(self):
        '''Punkt pierwszy dotyczy współpracy zdalnej'''
        a = 'lista mailingowa'
        b = 'repozytorium kodu'
        print('{}Zdalna praca:{}{}{}{}').format("\n", "\n- ", a, "\n- ", b)
        return

    def formulowanieWaznego(self):
        '''Punkt drugi dotyczy postawy <formułowania>'''
        self.punkty = ['cele', 'role', 'mierniki osiągania celów', 'okresowa ocena']
        print "\n", 'Formułowanie:'
        return

    def zasadyPracy(self):
        '''Punkt trzeci dotyczy zasad współpracy'''
        self.zasady = []
        self.zasady.append('czas po godzinach pracy')
        self.zasady.append('licencja sprawą otwartą')
        self.zasady.append('tworzymy cegiełki w sposób ustandaryzowany')
        # lista utworzona metodą dodawania kolejnych elementów
        print "\n", 'Zasady:'
        return

    def formatowanieKoduPy(self):
        '''Punkt czwarty dotyczy formatowania kodu pythona'''
        formaty = ['wcięcie 4 spacje', 'dokumentacja w klasach i metodach']
        formaty.append('opisy w istotnych miejscach')
        formaty.append('niezależność od systemu operacyjnego')
        return formaty

    def dwaKolejnePunkty(self):
        '''Tutaj zdefiniowane są opisy do punktu piętego i szóstego
        Zmienna do opisów to lista sparowanych stringów z listami
        '''
        self.punkt_piaty_i_szosty = [
            'Środowisko pracy (do wyboru):',
            [
                'IDLE',
                'PyCharm',
                'Eclipse',
                'Wing 101',
            ],
            'Warto poznać:',
            [
                'dokuwiki',
                'kontrola wersji - git',
            ]
        ]
        return

    def wydrukPunktowPiecSzesc(self):
        '''Tutaj korzystamy z danych klasy i drukujemy je
        Tytuł odróżniamy od podpunktów wg typu zmiennej
        '''
        for _ in self.punkt_piaty_i_szosty:
            if str == type(_):
                print "\n(typ danych poniżej)", type(_) # wydruk typu zmiennej dla informacji
                print _
            else:
                print '(typ danych poniżej):', type(_) # wydruk typu zmiennej dla informacji
                for _i in _:
                    print '-', _i
        return



######################
### Program główny ###
######################

# drukujemy dokumentację klasy
help(zeroweSpotkanie)

# tworzymy instancję, obiekt
zs = zeroweSpotkanie()

# wydruk pierwszego punktu możliwy tylko z wnętrza metody
zs.zdalnaPraca()

# wydruk listy podpunktów możliwy poza metodą, z klasy
zs.formulowanieWaznego()
for _i in zs.punkty:
    print('- {}').format(_i)

# wydruk całego obiektu listy
zs.zasadyPracy()
print(zs.zasady) # wydruk polskich znaków dziwny

# wyjście z metody do zmiennej
lista_formatow = zs.formatowanieKoduPy()
print "\n", 'Formatowanie kodu py:'
print lista_formatow # wydruk polskich znaków dziwny
for _i in lista_formatow:
    print('- {}').format(_i) # wydruk polskich znaków ok

# definicja kolejnych punktów
zs.dwaKolejnePunkty()
# wydruk punktów pięć i sześć
zs.wydrukPunktowPiecSzesc()
