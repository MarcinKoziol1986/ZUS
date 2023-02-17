"""
Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program po uruchomieniu wyświetla informację o dostępnych komendach:

saldo
sprzedaż
zakup
konto
lista
magazyn
przegląd
koniec

Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla
każdej z nich:

saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi
znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu
(np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu
"rower" oraz dodanie do konta kwoty 100).
zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk.
Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do
 komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
konto - Program wyświetla stan konta.
lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego
nazwę.
przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla
wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”.
eżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od
początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o
 tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi
 wybrać odpowiedni zakres).
koniec - Aplikacja kończy działanie.

Dodatkowe wymagania:

Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc
użyć komendy "przeglad".
Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację
o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji
(np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę,
 aplikacja powinna wyświetlić informację o niemożności wykonania operacji i
 jej nie wykonać). Zadbaj też o prawidłowe typy danych.
"""
dostepne_komendy = ['saldo', 'sprzedaz', 'zakup', 'konto', 'lista', 'magazyn', 'przeglad',
           'koniec']
konto = 5000
magazyn = {
    'rower': [5, 1000], 'kola do roweru': [40, 250], 'siodelka': [100, 50],
    'ramy do rowerow': [10, 500], 'smar': [500, 10],
}
historia =[]
while True:
    print(f'Komendy: {dostepne_komendy}')
    komenda = input('Wprowadz Komende:').strip()
    print(f'Wprowadzona Komenda: {komenda}')
    if komenda not in dostepne_komendy:
        print('Podano Zla Komende')

    if komenda == 'koniec':
        print('Koniec Programu, Milego Dnia')
        break
    elif komenda == 'saldo':
        print(f'wykonuje akcje {komenda.upper()}...')
        kwota = float(input('Podaj Kwote, o ktora zmieni sie stan konta:'))
        if konto + kwota < 0:
            print('Ta Operacja jest niemozliwa')
        else:
            konto += kwota
            print(f'Zmieniam stan konta o {kwota}')
            historia.append([komenda, kwota])
    elif komenda == 'sprzedaz':
        print(f'wykonuje akcje {komenda.upper()}...')
        nazwa_produktu = input('Podaj Nazwe Produktu: ')
        cena = float(input('Podaj Cene Jednego Produktu: '))
        ilosc_produktow = int(input('Podaj Ilosc Produktow: '))
        koszt = cena * ilosc_produktow
        magazyn[nazwa_produktu][0] -= ilosc_produktow
        if nazwa_produktu not in magazyn:
            print("nie ma takiego produktu")
        else:
            konto += koszt
            print(f'Sprzedaje {ilosc_produktow} sztuk {nazwa_produktu} za {koszt}')
            historia.append([komenda, kwota])
    elif komenda == 'zakup':
        print(f'wykonuje akcje {komenda.upper()}...')
        nazwa_produktu = input('Podaj Nazwe Produktu: ')
        cena = float(input('Podaj Cene Jednego Produktu: '))
        ilosc_produktow = int(input('Podaj Ilosc Produktow: '))
        koszt = cena * ilosc_produktow
        magazyn[nazwa_produktu][0] += ilosc_produktow
        if koszt > konto:
            print('Nie masz tylu srodkow na koncie')
        else:
            if nazwa_produktu not in magazyn:
                magazyn[nazwa_produktu] = 0
                magazyn[nazwa_produktu] += ilosc_produktow
                konto -= koszt
            print(f'zakupiono {ilosc_produktow} sztuk {nazwa_produktu} za {koszt}')
            historia.append([komenda, kwota])
    elif komenda == 'konto':
        print(f'wykonuje akcje {komenda.upper()}...')
        print(f'Aktualny Stan Konta to: {konto}')
    elif komenda == 'lista':
        print(f'wykonuje akcje {komenda.upper()}...')
        print(f'Aktualny Stan Magazynu to: {magazyn}')
    elif komenda == 'magazyn':
        print(f'wykonuje akcje {komenda.upper()}...')
        produkt_w_magazynie = input('podaj nazwe produktu:')
        if produkt_w_magazynie not in magazyn:
            print('Brak towaru w magazynie')
        elif produkt_w_magazynie == 'rower':
            print('Wmagazynie znjaduje sie ROWER(ilosc/cena za sztuke)')
            print(magazyn['rower'])
        elif produkt_w_magazynie == 'kola do roweru':
            print('Wmagazynie znjaduje sie KOLA Do ROWERU(ilosc/ cena za sztuke)')
            print(magazyn['kola do roweru'])
        elif produkt_w_magazynie == 'siodelka':
            print('Wmagazynie znjaduje sie SIODELKA(ilosc/cena za sztuke)')
            print(magazyn['siodelka'])
        elif produkt_w_magazynie == 'ramy do rowerow':
            print('Wmagazynie znjaduje sie RAMY DO ROWEROW(ilosc/cena za sztuke)')
            print(magazyn['ramy do rowerow'])
        elif produkt_w_magazynie == 'smar':
            print('Wmagazynie znjaduje sie SMAR(ilosc/cena za sztuke)')
            print(magazyn['smar'])


    elif komenda == 'przeglad':
        print(f'wykonuje akcje {komenda.upper()}...')
        print('Prosze Wybrac Zakres od 0 do 4')
        od = int(input("podaj zakres od: "))
        do = int(input("podaj zakres do: "))
        if od < 0:
            print('poza zakresem, prosze wprowadzic poprawny zakres')
            od = int(input("podaj zakres od: "))
        if do > 4:
            print('poza zakresem, prosze wprowadzic poprawny zakres')
            do = int(input("podaj zakres do: "))
        for idx, wpis in enumerate(historia[od:do]):
            print(idx, wpis)
        print(historia)










