from Vozlisce import Vozlisce
import itertools


class Omrezje:
    '''
        `Omrezje` je razred, ki vsebuje podatke o danem omrežju. Ima razredno lastnost:
            `slovar_vozlisc` ... slovar, katerega elementi so oblike `id_vozlišča: vozlišče`.
        Razrednih lastnosti ni mogoče spreminjati!
    '''

    # za potrebe določanja id-jev vozlišč uporabimo razredno spremenjivko
    _nov_id = 0  # začetna vrednost
    
    def nov_id():
        Omrezje._nov_id += 1
        return Omrezje._nov_id

    def reset_nov_id():
        Omrezje._nov_id = 0


    def __init__(self, vozlisca=list(), tabela_sosednosti=dict()):
        '''
            Vsak element seznama `vozlisca` mora biti oblike: `[ime, vsebina]`.
            Vsak element slovarja `tabela_sosednosti` je oblike: `ime: tab_imen_sosedov`.
        '''
        assert vozlisca and isinstance(vozlisca, list) and len(vozlisca) != 0, 'Podano mora biti najmanj eno vozlišče!'
        self._slovar_vozlisc = Omrezje.vrni_slovar_vozlisc(vozlisca, tabela_sosednosti)


    def __repr__(self):
        zamik='\n'
        vrednosti_slovarja = list(self.slovar_vozlisc.values())
        if len(vrednosti_slovarja) == 0:
            return 'Omrezje()'
        
        niz_vozlisca = f'{vrednosti_slovarja[0]}'
        for vozl in vrednosti_slovarja[1:]:
            niz_vozlisca += f',{zamik}{vozl}'

        return f'Omrezje({zamik}{niz_vozlisca}{zamik})'


    def __str__(self):
        zamik='\n'
        vrednosti_slovarja = list(self.slovar_vozlisc.values())
        if len(vrednosti_slovarja) == 0:
            return 'Omrezje()'
        
        niz_vozlisca = f'{vrednosti_slovarja[0]}'
        for vozl in vrednosti_slovarja[1:]:
            niz_vozlisca += f',{zamik}{vozl}'

        return f'Omrezje({zamik}{niz_vozlisca}{zamik})'

    
    # SLOVAR VOZLIŠČ -------------------------------------------------------------------------------
    @property
    def slovar_vozlisc(self):
        '''
            getter razredne lastnosti `slovar_vozlisc`
        '''
        return self._slovar_vozlisc

    
    def vrni_slovar_vozlisc(vozlisca, tabela_sosednosti):
        '''
            vsak element slovarja je oblike: `id_vozlišča: vozlišče`
        '''
        if not isinstance(vozlisca, list):
            raise ValueError('Podatki o vozliščih morajo biti podani v obliki seznama!')
        if len(vozlisca) == 0:
            raise ValueError('Podatki o vozliščih morajo biti podani!')
        for vozl in vozlisca:
            if not isinstance(vozl, list):
                raise ValueError('Vsa vozlišča morajo biti podana v obliki seznama!')
            if len(vozl) != 2:
                raise ValueError('Vsa vozlišča morajo vsebovati natanko dva podatka!')
            if not isinstance(vozl[0], int) or not isinstance(vozl[1], list):
                raise ValueError('Vsa vozlišča morajo biti oblike `[ime, vsebina]`, pri čemer je `ime` nenegativno celo število, `vsebina` pa seznam!')        
        for kljuc, vrednost in tabela_sosednosti.items():
            if not isinstance(kljuc, int) or not isinstance(vrednost, list):
                print(kljuc, vrednost)
                raise ValueError('Ključ vsakega elementa iz tabele sosednosti mora biti celo število, drugi podatek pa seznam!')
        if tabela_sosednosti:
            tabela_sosedov = []
            for sosedi in tabela_sosednosti.values():
                tabela_sosedov.extend(sosedi)
            mn_sosedov_iz_tab_sos = set(tabela_sosedov)
            mn_vozlisc_iz_tab_sos = set(vozl for vozl in tabela_sosednosti)
            mn_vozlisc = set(vozl[0] for vozl in vozlisca)
            for vozl in mn_sosedov_iz_tab_sos:
                if vozl not in mn_vozlisc:
                    raise ValueError('V tabeli sosednosti so lahko navedena izključno vozlišča, ki obstajajo znotraj omrežja!')
            for vozl in mn_vozlisc_iz_tab_sos:
                if vozl not in mn_vozlisc:
                    raise ValueError('V tabeli sosednosti so lahko navedena izključno vozlišča, ki obstajajo znotraj omrežja!')

        slovar_vozlisc_ime_id = dict()
        slovar_vozlisc = dict()
        for vozl in vozlisca:
            ime = vozl[0]
            vsebina = vozl[1]
            id = Omrezje.nov_id()
            sosedi = tabela_sosednosti[ime] if ime in tabela_sosednosti else list()
            slovar_vozlisc_ime_id[ime] = id

            slovar_vozlisc[id] =  Vozlisce(id, sosedi, ime, vsebina)

        # poporavimo sosede na `id`-je sosednih vozlišč namesto njihovoh imen
        for id in slovar_vozlisc:
            if len(slovar_vozlisc[id].sosedi) > 0:
                slovar_vozlisc[id].sosedi = list(slovar_vozlisc_ime_id[ime_soseda] for ime_soseda in slovar_vozlisc[id].sosedi)

        return slovar_vozlisc


# TESTI: ---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print('Začenjam testiranje ...')

    # (1.) preverjanje pravilnosti validiranja -------------------------------------------------------
    
    # (1.1) brez podanih argumentov
    Omrezje.reset_nov_id()
    try:
        Omrezje()
        print(f'(1.1) `Omrezje()` bi moralo prožiti napako `Podano mora biti najmanj eno vozlišče!`')
    except Exception as ex:
        if str(ex) != 'Podano mora biti najmanj eno vozlišče!':
            print(f'(1.1) `Omrezje()` proži napako `{ex}` namesto `Podano mora biti najmanj eno vozlišče!`')

    # (1.2) samo vozlišče ni podano
    Omrezje.reset_nov_id()
    try:
        Omrezje(tabela_sosednosti=dict([(1, [2, 3])]))
        print(f'(1.2) `Omrezje(tabela_sosednosti=dict([(1, [2, 3])]))` bi moralo prožiti napako `Podano mora biti najmanj eno vozlišče!`')
    except Exception as ex:
        if str(ex) != 'Podano mora biti najmanj eno vozlišče!':
            print(f'(1.2) `Omrezje(tabela_sosednosti=dict([(1, [2, 3])]))` proži napako `{ex}` namesto `Podano mora biti najmanj eno vozlišče!`')

    # (1.3) vozlisce ni tipa `list`
    Omrezje.reset_nov_id()
    try:
        Omrezje(vozlisca='neki', tabela_sosednosti=dict([(1, [2, 3])]))
        print(f'(1.3) `Omrezje(vozlisca=\'neki\', tabela_sosednosti=dict([(1, [2, 3])]))` bi moralo prožiti napako `Podano mora biti najmanj eno vozlišče!`')
    except Exception as ex:
        if str(ex) != 'Podano mora biti najmanj eno vozlišče!':
            print(f'(1.3) `Omrezje(vozlisca=\'neki\', tabela_sosednosti=dict([(1, [2, 3])]))` proži napako `{ex}` namesto `Podano mora biti najmanj eno vozlišče!`')

    # (1.4) vozlisce ne vsebuje natanko dveh elementov
    Omrezje.reset_nov_id()
    try:
        Omrezje(vozlisca=[[1, [2]], [3]], tabela_sosednosti=dict([(1, [2, 3])]))
        print(f'(1.4) `Omrezje(vozlisca=[[1, [2], [3]], tabela_sosednosti=dict([(1, [2, 3])]))` bi moralo prožiti napako `Vsa vozlišča morajo vsebovati natanko dva podatka!')
    except Exception as ex:
        if str(ex) != 'Vsa vozlišča morajo vsebovati natanko dva podatka!':
            print(f'(1.4) `Omrezje(vozlisca=[[1, [2], [3]], tabela_sosednosti=dict([(1, [2, 3])]))` proži napako `{ex}` namesto `Vsa vozlišča morajo vsebovati natanko dva podatka!')

    # (1.5) neustrezno generiranje objekta - ni vozlišč
    Omrezje.reset_nov_id()
    try:
        Omrezje(vozlisca=[], tabela_sosednosti=dict([(1, [2, 3])]))
        print(f'(1.5) `Omrezje(vozlisca=[], tabela_sosednosti=dict([(1, [2, 3])]))` bi moralo prožiti napako `Podano mora biti najmanj eno vozlišče!`')
    except Exception as ex:
        if str(ex) != 'Podano mora biti najmanj eno vozlišče!':
            print(f'(1.5) `Omrezje(vozlisca=[], tabela_sosednosti=dict([(1, [2, 3])]))` proži napako `{ex}` namesto `Podano mora biti najmanj eno vozlišče!`')


    # (1.6) neustrezno generiranje objekta - niso vsa vozlišča podana kot seznami
    Omrezje.reset_nov_id()
    try:
        Omrezje(vozlisca=[[6, ['neki neki']], 7], tabela_sosednosti=dict([(1, [2, 3])]))
        print(f'(1.6) `Omrezje(vozlisca=[[6, ["neki neki"]], 7], tabela_sosednosti=dict([(1, [2, 3])]))` bi moralo prožiti napako `Vsa vozlišča morajo biti podana v obliki seznama!`')
    except Exception as ex:
        if str(ex) != 'Vsa vozlišča morajo biti podana v obliki seznama!':
            print(f'(1.6) `Omrezje(vozlisca=[[6, ["neki neki"]], 7], tabela_sosednosti=dict([(1, [2, 3])]))` proži napako `{ex}` namesto `Vsa vozlišča morajo biti podana v obliki seznama!`')


    # (1.7) neustrezno generiranje objekta - tabela sosednosti kot ključ vsebuje vozlišče, ki ne obstaja v trenutnem omrežju
    Omrezje.reset_nov_id()
    try:
        Omrezje(vozlisca=[[6, ['neki neki']]], tabela_sosednosti={1: [2, 3]})
        print(f'(1.7) `Omrezje(vozlisca=[[6, ["neki neki"]]], tabela_sosednosti=dict([(1, [2, 3])]))` bi moralo prožiti napako `V tabeli sosednosti so lahko navedena izključno vozlišča, ki obstajajo znotraj omrežja!`')
    except Exception as ex:
        if str(ex) != 'V tabeli sosednosti so lahko navedena izključno vozlišča, ki obstajajo znotraj omrežja!':
            print(f'(1.7) `Omrezje(vozlisca=[[6, ["neki neki"]]], tabela_sosednosti=dict([(1, [2, 3])]))` proži napako `{ex}` namesto `V tabeli sosednosti so lahko navedena izključno vozlišča, ki obstajajo znotraj omrežja!`')

    # (1.8) neustrezno generiranje objekta - tabela sosednosti kot vrednost vsebuje vozlišče, ki ne obstaja v trenutnem omrežju
    Omrezje.reset_nov_id()
    try:
        Omrezje(vozlisca=[[1, [3, 2.3]], [2, ["petnajst"]]], tabela_sosednosti=dict([(1, [2, 3]), (2, [1])]))
        print(f'(1.8) `Omrezje(vozlisca=[[1, [3, 2.3]], [2, ["petnajst"]]], tabela_sosednosti=dict([(1, [2, 3]), (2, [1])]))` bi moralo prožiti napako `V tabeli sosednosti so lahko navedena izključno vozlišča, ki obstajajo znotraj omrežja!`')
    except Exception as ex:
        if str(ex) != 'V tabeli sosednosti so lahko navedena izključno vozlišča, ki obstajajo znotraj omrežja!':
            print(f'(1.8) `Omrezje(vozlisca=[[1, [3, 2.3]], [2, ["petnajst"]]], tabela_sosednosti=dict([(2, tabela_sosednosti=dict([(1, [2, 3]), (2, [1])]))` proži napako `{ex}` namesto `V tabeli sosednosti so lahko navedena izključno vozlišča, ki obstajajo znotraj omrežja!`')

    # (1.9) ustrezno generiranje objekta - so vozlišča, ni tabele sosednosti
    Omrezje.reset_nov_id()
    omrezje = Omrezje(vozlisca=[[1, [3, 2.3]]])
    if len(omrezje.slovar_vozlisc) != 1:
        print(f'(1.9) `Omrezje(vozlisca=[Vozlisce(id=1, ime=2, vsebina=[3])]).slovar_vozlisc` ima `{len(omrezje.slovar_vozlisc)}` elementov namesto `1`')
    sl_vozlisc = {1: Vozlisce(id=1, ime=1, vsebina=[3, 2.3])}
    if omrezje.slovar_vozlisc != sl_vozlisc:
        print(f'(1.9) `Omrezje(vozlisca=[Vozlisce(id=1, ime=2, vsebina=[3])]).slovar_vozlisc` vrne `{omrezje.slovar_vozlisc}` namesto `{sl_vozlisc}`')

    # (1.10) ustrezno generiranje objekta - so vozlišča, je tabela sosednosti
    Omrezje.reset_nov_id()
    omrezje = Omrezje(vozlisca=[[1, [3, 2.3]], [2, ["nič"]], [6, [True]]], tabela_sosednosti=dict([(1, [6]), (6, [1])]))
    if len(omrezje.slovar_vozlisc) != 3:
        print(f'(1.10) `Omrezje(vozlisca=[[1, [3, 2.3]], [2, ["nič"]], [6, [True]]], tabela_sosednosti=dict([(1, [6]), (6, [1])])).slovar_vozlisc` ima `{len(omrezje.slovar_vozlisc)}` elementov namesto `3`')
    sl_vozlisc = {1: Vozlisce(id=1, sosedi=[3], ime=1, vsebina=[3, 2.3]), 2: Vozlisce(id=2, sosedi=[], ime=2, vsebina=["nič"]), 3: Vozlisce(id=3, sosedi=[1], ime=6, vsebina=[True])}
    if omrezje.slovar_vozlisc != sl_vozlisc:
        print(f'(1.10) `Omrezje(vozlisca=[[1, [3, 2.3]], [2, ["nič"]], [6, [True]]], tabela_sosednosti=dict([(1, [6]), (6, [1])])).slovar_vozlisc` vrne `{omrezje.slovar_vozlisc}` namesto `{sl_vozlisc}`')

    # (2.) izpis objekta -------------------------------------------------------------------------------
    Omrezje.reset_nov_id()
    zamik='\n'
    omrezje = Omrezje(vozlisca=[[1, [3, 2.3]], [2, ["nič"]], [6, [True]]], tabela_sosednosti=dict([(1, [6]), (6, [1])]))
    sl_vozlisc = {1: Vozlisce(id=1, sosedi=[3], ime=1, vsebina=[3, 2.3]), 2: Vozlisce(id=2, sosedi=[], ime=2, vsebina=["nič"]), 3: Vozlisce(id=3, sosedi=[1], ime=6, vsebina=[True])}
    niz_izpis = f'Omrezje({zamik}{sl_vozlisc[1]},{zamik}{sl_vozlisc[2]},{zamik}{sl_vozlisc[3]}{zamik})'

    if str(omrezje) != niz_izpis:
        print(f'(2.) `print(Omrezje(vozlisca=[[1, [3, 2.3]], [2, ["nič"]], [6, [True]]], tabela_sosednosti=dict([(1, [6]), (6, [1])])))` vrne `{omrezje}` namesto `{niz_izpis}`')

    print('Testiranje zaključeno.')