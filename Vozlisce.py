class Vozlisce:
    '''
        `Vozlisce` je razred, ki vsebuje poljubno število podatkov o objektu v omrežju. Vsebuje razredne lastnosti:
            `id` ... enolično določen id
            `sosedi` ... id-ji sosednjih vozlišč (samo, kadar je vozlišče del omrežja)
            `ime` ... lastno ime vozlišča (neobvezen podatek)
            `vsebina` ... tabela, ki vsebuje vsebino vozlišča
            `st_sosedov` ... število sosedov vozlišča
    '''

    def __init__(self, id=-1, sosedi=list(), ime=str(), vsebina=list()):
        # ti parametri morajo biti vedno podani
        assert isinstance(id, int) and id > -1, 'id mora biti podan!'
        assert not isinstance(ime, str), 'ime mora biti podano!'
        assert len(vsebina) != 0, 'vsebina mora biti podana!'
        
        self._id = id
        self.sosedi = sosedi
        self.ime = ime
        self.vsebina = vsebina


    def __repr__(self):
        zamik="\n\t"
        return f'Vozlisce({zamik}id={self.id},{zamik}sosedi={self.sosedi},{zamik}ime={self.ime},{zamik}vsebina={self.vsebina},{zamik}st_sosedov={self.st_sosedov}{zamik})'


    def __str__(self):
        zamik='\n\t'
        return f'Vozlisce({zamik}id={self.id},{zamik}sosedi={self.sosedi},{zamik}ime={self.ime},{zamik}vsebina={self.vsebina},{zamik}st_sosedov={self.st_sosedov}{zamik})'


    def __eq__(self, other):
        return self.id == other.id and self.ime == other.ime and self.sosedi == other.sosedi and self.vsebina == other.vsebina


    # ID --------------------------------------------------------------------------------------------------
    @property
    def id(self):
        return self._id


    # SOSEDI -----------------------------------------------------------------------------------------------
    @property
    def sosedi(self):
        return self._sosedi

    
    @sosedi.setter
    def sosedi(self, sosedi):
        assert isinstance(sosedi if sosedi else list(), list), 'sosedi morajo biti tipa `list` oz. nedoločeni!'

        self._sosedi = sosedi if sosedi else list()


    # IME ---------------------------------------------------------------------------------------------------
    @property
    def ime(self):
        return self._ime


    @ime.setter
    def ime(self, ime):
        if not isinstance(ime, int):
            raise TypeError('Ime vozlišča mora biti podano in mora biti celo število!')
        if ime < 0:
            raise ValueError('Ime mora biti nenegativno celo število!')

        self._ime = ime


    # VSEBINA -----------------------------------------------------------------------------------------------
    @property
    def vsebina(self):
        return self._vsebina


    @vsebina.setter
    def vsebina(self, vsebina):
        assert vsebina, 'vsebina mora biti podana!'
        assert isinstance(vsebina, list), 'vsebina mora biti tipa `list`!'

        self._vsebina = vsebina if vsebina else list()


    # ŠTEVILO SOSEDOV ---------------------------------------------------------------------------------------
    @property
    def st_sosedov(self):
        return len(self.sosedi)


# TESTI: -----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print('Začenjam testiranje ...')

    # (1.) validacije obstoja zahtevanih vrednosti -----------------------------------------------------------

    # (1.1) podanega ni ničesar
    try:
        Vozlisce()
        print(print(f'(1.1) `Vozlisce()` ne proži napake - javiti bi moralo: `id mora biti podan!`'))
    except Exception as ex:
        if ex.args[0] != 'id mora biti podan!':
            print(f'(1.1) `Vozlisce()` proži `{ex.args[0]}` namesto `id mora biti podan!`')

    # (1.2) podan je samo id
    try:
        Vozlisce(id=1)
        print(print(f'(1.2) `Vozlisce(id=1)` ne proži napake - javiti bi moralo: `ime mora biti podano!`'))
    except Exception as ex:
        if ex.args[0] != 'ime mora biti podano!':
            print(f'(1.2) `Vozlisce(id=1)` proži `{ex.args[0]}` namesto `ime mora biti podano!`')

    # (1.3) podano je samo ime
    try:
        Vozlisce(ime=1)
        print(print(f'(1.3) `Vozlisce(ime=1)` ne proži napake - javiti bi moralo: `id mora biti podan!`'))
    except Exception as ex:
        if ex.args[0] != 'id mora biti podan!':
            print(f'(1.3) `Vozlisce(ime=1)` proži `{ex.args[0]}` namesto `id mora biti podan!`')

    # (1.4) podana je samo vsebina
    try:
        Vozlisce(vsebina=[1])
        print(print(f'(1.4) `Vozlisce(vsebina=[1])` ne proži napake - javiti bi moralo: `id mora biti podan!`'))
    except Exception as ex:
        if ex.args[0] != 'id mora biti podan!':
            print(f'(1.4) `Vozlisce(vsebina=[1])` proži `{ex.args[0]}` namesto `id mora biti podan!`')

    # (1.5) podani so samo sosedi
    try:
        Vozlisce(sosedi=[1])
        print(print(f'(1.5) `Vozlisce(sosedi=[1])` ne proži napake - javiti bi moralo: `id mora biti podan!`'))
    except Exception as ex:
        if ex.args[0] != 'id mora biti podan!':
            print(f'(1.5) `Vozlisce(sosedi=[1])` proži `{ex.args[0]}` namesto `id mora biti podan!`')

    # (1.6) podana sta id in ime
    try:
        Vozlisce(id=1, ime=2)
        print(print(f'(1.6) `Vozlisce(id=1, ime=2)` ne proži napake - javiti bi moralo: `vsebina mora biti podana!`'))
    except Exception as ex:
        if ex.args[0] != 'vsebina mora biti podana!':
            print(f'(1.6) `Vozlisce(id=1, ime=2)` proži `{ex.args[0]}` namesto `vsebina mora biti podana!`')

    # (1.7) podana sta id in vsebina
    try:
        Vozlisce(id=1, vsebina=[2])
        print(print(f'(1.7) `Vozlisce(id=1, vsebina=[2])` ne proži napake - javiti bi moralo: `ime mora biti podano!`'))
    except Exception as ex:
        if ex.args[0] != 'ime mora biti podano!':
            print(f'(1.7) `Vozlisce(id=1, vsebina=[2])` proži `{ex.args[0]}` namesto `ime mora biti podano!`')

    # (1.8) podana sta id in sosedi
    try:
        Vozlisce(id=1, sosedi=[2])
        print(print(f'(1.8) `Vozlisce(id=1, sosedi=[2])` ne proži napake - javiti bi moralo: `ime mora biti podano!`'))
    except Exception as ex:
        if ex.args[0] != 'ime mora biti podano!':
            print(f'(1.8) `Vozlisce(id=1, sosedi=[2])` proži `{ex.args[0]}` namesto `ime mora biti podano!`')

    # (1.9) podani so id, ime in sosedi
    try:
        Vozlisce(id=1, ime=2, sosedi=[3])
        print(print(f'(1.9) `Vozlisce(id=1, ime=2, sosedi=[3])` ne proži napake - javiti bi moralo: `vsebina mora biti podana!`'))
    except Exception as ex:
        if ex.args[0] != 'vsebina mora biti podana!':
            print(f'(1.9) `Vozlisce(id=1, ime=2, sosedi=[3])` proži `{ex.args[0]}` namesto `vsebina mora biti podana!`')

    # (1.10) podani so id, vsebina in sosedi
    try:
        Vozlisce(id=1, vsebina=[2], sosedi=[3])
        print(print(f'(1.10) `Vozlisce(id=1, vsebina=[2], sosedi=[3])` ne proži napake - javiti bi moralo: `ime mora biti podano!`'))
    except Exception as ex:
        if ex.args[0] != 'ime mora biti podano!':
            print(f'(1.10) `Vozlisce(id=1, vsebina=[2], sosedi=[3])` proži `{ex.args[0]}` namesto `ime mora biti podano!`')

    # (1.11) podani so ime, vsebina in sosedi
    try:
        Vozlisce(ime=1, vsebina=[2], sosedi=[3])
        print(print(f'(1.11) `Vozlisce(ime=1, vsebina=[2], sosedi=[3])` ne proži napake - javiti bi moralo: `id mora biti podan!`'))
    except Exception as ex:
        if ex.args[0] != 'id mora biti podan!':
            print(f'(1.11) `Vozlisce(ime=1, vsebina=[2], sosedi=[3])` proži `{ex.args[0]}` namesto `id mora biti podan!`')

    # (1.12.1) podani so vsi potrebni podatki
    try:
        Vozlisce(id=1, ime=1, vsebina=[2], sosedi=[3])
    except Exception as ex:
        print(f'(1.12.1) `Vozlisce(id=1, ime=1, vsebina=[2], sosedi=[3])` proži `{ex.args[0]}`, čeprav se napaka ne bi smela prožiti')

    # (1.12.1) podani so vsi potrebni podatki - brez sosedov
    try:
        Vozlisce(id=1, ime=1, vsebina=[2])
    except Exception as ex:
        print(f'(1.12.2) `Vozlisce(id=1, ime=1, vsebina=[2])` proži `{ex.args[0]}`, čeprav se napaka ne bi smela prožiti')

    
    # (2.) validacija pravilnosti vnosa podatkov --------------------------------------------------------------------------
    
    # (2.1.1) neustrezen id - ni celo število
    try:
        Vozlisce(id='jaz', ime=1, vsebina=[2])
        print(print(f'(2.1.1) `Vozlisce(id="jaz", vsebina=[2], sosedi=[3])` ne proži napake - javiti bi moralo: `id mora biti podan!`'))
    except Exception as ex:
        if ex.args[0] != 'id mora biti podan!':
            print(f'(2.1.1) `Vozlisce(id="jaz", ime=1, vsebina=[2])` proži `{ex.args[0]}` namesto `id mora biti podan!`')

    # (2.1.2) neustrezen id - ni nenegativno število
    try:
        Vozlisce(id=-10, ime=1, vsebina=[2])
        print(print(f'(2.1.2) `Vozlisce(id=-10, ime=1, vsebina=[2])` ne proži napake - javiti bi moralo: `id mora biti podan!`'))
    except Exception as ex:
        if ex.args[0] != 'id mora biti podan!':
            print(f'(2.1.2) `Vozlisce(id=-10, ime=1, vsebina=[2])` proži `{ex.args[0]}` namesto `id mora biti podan!`')

    # (2.2.1) neustrezno ime - ni število
    try:
        Vozlisce(id=1, ime='jaz', vsebina=[2])
        print(f'(2.2.1) `Vozlisce(id=1, ime="jaz", vsebina=[2])` ne proži napake - javiti bi moralo: `ime mora biti podano!`')
    except Exception as ex:
        if ex.args[0] != 'ime mora biti podano!':
            print(f'(2.2.1) `Vozlisce(id=1, ime="jaz", vsebina=[2])` proži `{ex.args[0]}` namesto `ime mora biti podano!`')

    # (2.2.2) neustrezno ime - ni nenegativno število
    try:
        Vozlisce(id=1, ime=-5, vsebina=[2])
        print(f'(2.2.2) `Vozlisce(id=1, ime=-5, vsebina=[2])` ne proži napake - javiti bi moralo: `Ime mora biti nenegativno celo število!`')
    except Exception as ex:
        if ex.args[0] != 'Ime mora biti nenegativno celo število!':
            print(f'(2.2.2) `Vozlisce(id=1, ime=-5, vsebina=[2])` proži `{ex.args[0]}` namesto `Ime mora biti nenegativno celo število!`')

    # (3.) pravilnost shranjevanja vrednosti --------------------------------------------------------------------------
    
    # (3.1) preprost primer
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    if vozl.id != 1:
        print(f'(3.1) `Vozlisce(id=1, ime=2, vsebina=[3])` nastavi `id` objekta na `{vozl.id}` namesto na `1`')
    if vozl.ime != 2:
        print(f'(3.1) `Vozlisce(id=1, ime=2, vsebina=[3])` nastavi `ime` objekta na `{vozl.ime}` namesto na `2`')
    if vozl.vsebina != [3]:
        print(f'(3.1) `Vozlisce(id=1, ime=2, vsebina=[3])` nastavi `vsebina` objekta na `{vozl.vsebina}` namesto na `[3]`')
    if vozl.sosedi != []:
        print(f'(3.1) `Vozlisce(id=1, ime=2, vsebina=[3])` nastavi `sosedi` objekta na `{vozl.sosedi}` namesto na `[]`')
    if vozl.st_sosedov != 0:
        print(f'(3.1) `Vozlisce(id=1, ime=2, vsebina=[3])` nastavi `st_sosedov` objekta na `{vozl.st_sosedov}` namesto na `0`')

    # (3.2) normalni primer
    vozl = Vozlisce(id=1, sosedi=[2, 15, 3, 4, 7], ime=2, vsebina=[3, 'Tamara', 'Krompir', 7.5, True])
    if vozl.id != 1:
        print(f'(3.2) `Vozlisce(id=1, sosedi=[2, 15, 3, 4, 7], ime=2, vsebina=[3, "Tamara", "Krompir", 7.5, True])` nastavi `id` objekta na `{vozl.id}` namesto na `1`')
    if vozl.ime != 2:
        print(f'(3.2) `Vozlisce(id=1, sosedi=[2, 15, 3, 4, 7], ime=2, vsebina=[3, "Tamara", "Krompir", 7.5, True])` nastavi `ime` objekta na `{vozl.ime}` namesto na `2`')
    if vozl.vsebina != [3, 'Tamara', 'Krompir', 7.5, True]:
        print(f'(3.2) `Vozlisce(id=1, sosedi=[2, 15, 3, 4, 7], ime=2, vsebina=[3, "Tamara", "Krompir", 7.5, True])` nastavi `vsebina` objekta na `{vozl.vsebina}` namesto na `[3, "Tamara", "Krompir", 7.5, True]`')
    if vozl.sosedi != [2, 15, 3, 4, 7]:
        print(f'(3.2) `Vozlisce(id=1, sosedi=[2, 15, 3, 4, 7], ime=2, vsebina=[3, "Tamara", "Krompir", 7.5, True])` nastavi `sosedi` objekta na `{vozl.sosedi}` namesto na `[2, 15, 3, 4, 7]`')
    if vozl.st_sosedov != 5:
        print(f'(3.2) `Vozlisce(id=1, sosedi=[2, 15, 3, 4, 7], ime=2, vsebina=[3, "Tamara", "Krompir", 7.5, True])` nastavi `st_sosedov` objekta na `{vozl.st_sosedov}` namesto na `5`')

    # (4.) pravilnost spreminjanja vrednosti --------------------------------------------------------------------------

    # (4.1) spreminjanje id-ja
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    try:
        vozl.id = 5
        print('(4.1) `Vozlisce(id=1, ime=2, vsebina=[3]).id = 5` bi moral sprožiti napako `can\'t set attribute`')
    except Exception as ex:
        if str(ex) != 'can\'t set attribute':
            print(f'(4.1) `Vozlisce(id=1, ime=2, vsebina=[3]).id = 5` sproži napako {ex} namesto `can\'t set attribute`')

    # (4.2) spreminjanje imena

    # (4.2.1) pravilno spreminjanje imena
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    vozl.ime = 5
    if vozl.ime != 5:
        print(f'(4.2.1) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = 5` nastavi `ime` objekta na `{vozl.ime}` namesto na `5`')
    if vozl.id != 1:
        print(f'(4.2.1) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = 5` nastavi `id` objekta na `{vozl.id}` namesto na `1`')
    if vozl.vsebina != [3]:
        print(f'(4.2.1) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = 5` nastavi `vsebina` objekta na `{vozl.vsebina}` namesto na `[3]`')
    if vozl.sosedi != []:
        print(f'(4.2.1) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = 5` nastavi `sosedi` objekta na `{vozl.sosedi}` namesto na `[]`')
    if vozl.st_sosedov != 0:
        print(f'(4.2.1) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = 5` nastavi `st_sosedov` objekta na `{vozl.st_sosedov}` namesto na `0`')

    # (4.2.2) neparavilno spreminjanje imena - ni celo število
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    try:
        vozl.ime = 'bla'
        print('(4.2.2) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = "bla"` bi moral sprožiti napako `Ime vozlišča mora biti podano in mora biti celo število!`')
    except Exception as ex:
        if str(ex) != 'Ime vozlišča mora biti podano in mora biti celo število!':
            print(f'(4.2.2) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = "bla"` sproži napako {ex} namesto `Ime vozlišča mora biti podano in mora biti celo število!`')

    # (4.2.3) neparavilno spreminjanje imena - je negativno celo število
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    try:
        vozl.ime = -5
        print('(4.2.3) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = -5` bi moral sprožiti napako `Ime mora biti nenegativno celo število!`')
    except Exception as ex:
        if str(ex) != 'Ime mora biti nenegativno celo število!':
            print(f'(4.2.3) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = -5` sproži napako {ex} namesto `Ime mora biti nenegativno celo število!`')

    # (4.2.4) nepravilno spreminjanje imena - nastavi na `None`
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    try:
        vozl.ime = None
        print('(4.2.4) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = None` bi moral sprožiti napako `Ime vozlišča mora biti podano in mora biti celo število!`')
    except Exception as ex:
        if str(ex) != 'Ime vozlišča mora biti podano in mora biti celo število!':
            print(f'(4.2.4) `Vozlisce(id=1, ime=2, vsebina=[3]).ime = None` sproži napako {ex} namesto `Ime vozlišča mora biti podano in mora biti celo število!`')

    # (4.3) spreminjanje vsebine

    # (4.3.1) pravilno spreminjanje
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    vozl.vsebina = [5, 7]
    if vozl.id != 1:
        print(f'(4.3.1) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = [5, 7]` nastavi `id` objekta na `{vozl.id}` namesto na `1`')
    if vozl.ime != 2:
        print(f'(4.3.1) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = [5, 7]` nastavi `ime` objekta na `{vozl.ime}` namesto na `2`')
    if vozl.vsebina != [5, 7]:
        print(f'(4.3.1) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = [5, 7]` nastavi `vsebina` objekta na `{vozl.vsebina}` namesto na `[5, 7]`')
    if vozl.sosedi != []:
        print(f'(4.3.1) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = [5, 7]` nastavi `sosedi` objekta na `{vozl.sosedi}` namesto na `[]`')
    if vozl.st_sosedov != 0:
        print(f'(4.3.1) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = [5, 7]` nastavi `st_sosedov` objekta na `{vozl.st_sosedov}` namesto na `0`')

    # (4.3.2) nepravilno spreminjanje vsebine - nastavi na niz (tj. ni list)
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    try:
        vozl.vsebina = 'bla'
        print('(4.3.2) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = "bla"` bi moral sprožiti napako `vsebina mora biti tipa `list`!`')
    except Exception as ex:
        if str(ex) != 'vsebina mora biti tipa `list`!':
            print(f'(4.3.2) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = "bla"` sproži napako {ex} namesto `vsebina mora biti tipa `list`!`')


    # (4.3.3) nepravilno spreminjanje vsebine - nastavi na `None`
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    try:
        vozl.vsebina = None
        print('(4.3.3) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = None` bi moral sprožiti napako `vsebina mora biti podana!`')
    except Exception as ex:
        if str(ex) != 'vsebina mora biti podana!':
            print(f'(4.3.3) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = None` sproži napako {ex} namesto `vsebina mora biti podana!`')

    # (4.4) spreminjanje sosedov

    # (4.4.1) pravilno spreminjanje sosedov na ne Null
    vozl = Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3])
    vozl.sosedi = [5, 7]
    if vozl.id != 1:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = [5, 7]` nastavi `id` objekta na `{vozl.id}` namesto na `1`')
    if vozl.ime != 2:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = [5, 7]` nastavi `ime` objekta na `{vozl.ime}` namesto na `2`')
    if vozl.vsebina != [3]:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = [5, 7]` nastavi `vsebina` objekta na `{vozl.vsebina}` namesto na `[3]`')
    if vozl.sosedi != [5, 7]:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = [5, 7]` nastavi `sosedi` objekta na `{vozl.sosedi}` namesto na `[5, 7]`')
    if vozl.st_sosedov != 2:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = [5, 7]` nastavi `st_sosedov` objekta na `{vozl.st_sosedov}` namesto na `2`')

    # (4.4.1) pravilno spreminjanje sosedov na None
    vozl = Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3])
    vozl.sosedi = None
    if vozl.id != 1:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = None` nastavi `id` objekta na `{vozl.id}` namesto na `1`')
    if vozl.ime != 2:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = None` nastavi `ime` objekta na `{vozl.ime}` namesto na `2`')
    if vozl.vsebina != [3]:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = None` nastavi `vsebina` objekta na `{vozl.vsebina}` namesto na `[3]`')
    if vozl.sosedi != []:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = None` nastavi `sosedi` objekta na `{vozl.sosedi}` namesto na `[]`')
    if vozl.st_sosedov != 0:
        print(f'(4.3.1) `Vozlisce(id=1, sosedi=[5, 18, 6], ime=2, vsebina=[3]).sosedi = None` nastavi `st_sosedov` objekta na `{vozl.st_sosedov}` namesto na `0`')

    # (4.4.2) nepravilno spreminjanje sosedov - niso tipa `list`
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    try:
        vozl.sosedi = 'bla'
        print('(4.3.3) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = "bla"` bi moral sprožiti napako `sosedi morajo biti tipa `list` oz. nedoločeni!`')
    except Exception as ex:
        if str(ex) != 'sosedi morajo biti tipa `list` oz. nedoločeni!':
            print(f'(4.3.3) `Vozlisce(id=1, ime=2, vsebina=[3]).vsebina = "bla"` sproži napako {ex} namesto `sosedi morajo biti tipa `list` oz. nedoločeni!`')
    
    # (4.5) spreminjanje števila sosedov
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    try:
        vozl.st_sosedov = 5
        print('(4.1) `Vozlisce(id=1, ime=2, vsebina=[3]).st_sosedov = 5` bi moral sprožiti napako `can\'t set attribute`')
    except Exception as ex:
        if str(ex) != 'can\'t set attribute':
            print(f'(4.5) `Vozlisce(id=1, ime=2, vsebina=[3]).st_sosedov = 5` sproži napako {ex} namesto `can\'t set attribute`')

    # (5.) izpis objekta ----------------------------------------------------------------------------------------------

    zamik = '\n\t'

    # (5.1) preprost primer
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    zeljeni_izpis = f'Vozlisce({zamik}id=1,{zamik}sosedi=[],{zamik}ime=2,{zamik}vsebina=[3],{zamik}st_sosedov=0{zamik})'
    if str(vozl) != zeljeni_izpis:
        print(f'(5.1) `str(Vozlisce(id=1, ime=2, vsebina=[3]))` izpiše \n`{vozl}`\nnamesto\n`{zeljeni_izpis}`')

    # (5.2) kompleksnejši primer
    vozl = Vozlisce(id=7, sosedi=[9, 5, 31, 19], ime=3, vsebina=[3, 'bla', 6.4, None, True])
    zeljeni_izpis = f'Vozlisce({zamik}id=7,{zamik}sosedi=[9, 5, 31, 19],{zamik}ime=3,{zamik}vsebina=[3, \'bla\', 6.4, None, True],{zamik}st_sosedov=4{zamik})'
    if str(vozl) != zeljeni_izpis:
        print(f'(5.2) `str(Vozlisce(id=7, sosedi=[9, 5, 31, 19], ime=3, vsebina=[3, \'bla\', 6.4, None, True]))` izpiše \n`{vozl}`\nnamesto\n`{zeljeni_izpis}`')

    # (6.) enakost dveh objektov -----------------------------------------------------------------------------------------

    # (6.1) enaka objekta
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    vozl_1 = Vozlisce(id=1, ime=2, vsebina=[3])
    if vozl != vozl_1:
        print(f'(6.1) Vozlisce(id=1, ime=2, vsebina=[3]) == Vozlisce(id=1, ime=2, vsebina=[3])` vrne {vozl == vozl_1} namest True')

    # (6.2) različna objekta - id
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    vozl_1 = Vozlisce(id=2, ime=2, vsebina=[3])
    if vozl == vozl_1:
        print(f'(6.2) `Vozlisce(id=1, ime=2, vsebina=[3]) == Vozlisce(id=2, ime=2, vsebina=[3])` vrne {vozl == vozl_1} namest False')

    # (6.2) različna objekta - sosedi
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    vozl_1 = Vozlisce(id=1, sosedi=[3], ime=2, vsebina=[3])
    if vozl == vozl_1:
        print(f'(6.3) Vozlisce(id=1, ime=2, vsebina=[3]) == Vozlisce(id=1, sosedi=[3], ime=2, vsebina=[3])` vrne {vozl == vozl_1} namest False')

    # (6.2) različna objekta - ime
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    vozl_1 = Vozlisce(id=1, ime=3, vsebina=[3])
    if vozl == vozl_1:
        print(f'(6.4) Vozlisce(id=1, ime=2, vsebina=[3]) == Vozlisce(id=1, ime=3, vsebina=[3])` vrne {vozl == vozl_1} namest False')

    # (6.2) različna objekta - vsebina
    vozl = Vozlisce(id=1, ime=2, vsebina=[3])
    vozl_1 = Vozlisce(id=1, ime=2, vsebina=[1])
    if vozl == vozl_1:
        print(f'(6.4) Vozlisce(id=1, ime=2, vsebina=[3]) == Vozlisce(id=1, ime=2, vsebina=[1])` vrne {vozl == vozl_1} namest False')

    print('Testiranje zaključeno.')