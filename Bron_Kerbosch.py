from Omrezje import Omrezje
from Vozlisce import Vozlisce
import numpy as np


def posodobi_seznam_maksimalnih_klik(klika, sez_klik, st_vozlisc_v_najvecji_kliki, samo_najvecje=False):
    '''
        Vrne število vozlišč v največji kliki izmed do sedaj odkritih klik in seznam klik.

        Vhodni podatki:
            klika ... klika, ki jo želimo dodati v seznam klik
            sez_klik ... do sedaj ustvarjeni seznam "maksimalnih" klik
            st_vozlisc_v_najvecji_kliki ... število vozlišč v trenutno največji kliki
    '''
    if samo_najvecje:
        st_eltov_v_kliki = len(klika)
        if st_eltov_v_kliki == st_vozlisc_v_najvecji_kliki:  # še ena klika, ki je potencialno maksimalna
            sez_klik.append(klika)
        elif st_eltov_v_kliki > st_vozlisc_v_najvecji_kliki:  # trenutna klika je do sedaj največja odkrita
            sez_klik = [klika]
            st_vozlisc_v_najvecji_kliki = st_eltov_v_kliki
    else:  # vse maksimalne klike - ne samo največje glede na število vsebovanih vozlišč
        sez_klik.append(klika)
    return st_vozlisc_v_najvecji_kliki, sez_klik


# Bron-Kerboschov algoritem --------------------------------------------------------------
def Bron_Kerbosch(R, P, X, sl_vozlisc, samo_najvecje):
    '''
        Algoritem vrne seznam vseh maksimalnih klik danega omrežja.

        Vhodni podtki:
            R ... množica, katere vsi elementi so vsebovani v kliki;
            P ... množica, katere nekateri elementi so vsebovani v kliki;
            X ... množica, katere noben element ni vsebovan v kliki;
            sl_vozlisc ... slovar vozlišč danega omrežja, katerega elementi so oblike
                `id_vozlišča: vozlišče`, pri čemer je `vozlišče` oblike `Vozlisce(id, sosedi, ime, vsebina, st_sosedov)`
    '''
    st_vozlisc_v_najvecji_kliki = 0
    seznam_klik = list()
    if not P and not X:  # `P` in `X` sta prazni
        # k `R` ne moremo dodati novega vozlišča
        # torej `R` zagotovo vsebuje maksimalno kliko danega grafa
        if R and (R not in seznam_klik):
            st_vozlisc_v_najvecji_kliki, seznam_klik = posodobi_seznam_maksimalnih_klik(R, seznam_klik, st_vozlisc_v_najvecji_kliki, samo_najvecje)
    
    else:
        for v in P:
            sosedi_v = set(sl_vozlisc[v].sosedi)

            R_copy = R.copy() 
            R_copy.add(v)
            P_copy = P.copy()
            P_copy = sosedi_v.intersection(P)
            X_copy = X.copy()
            X_copy = sosedi_v.intersection(X)

            # rekrzivno dodamo klike v seznam klik
            for klika in Bron_Kerbosch(R_copy, P_copy, X_copy, sl_vozlisc, samo_najvecje):
                if klika and (klika not in seznam_klik):
                    st_vozlisc_v_najvecji_kliki, seznam_klik = posodobi_seznam_maksimalnih_klik(klika, seznam_klik, st_vozlisc_v_najvecji_kliki, samo_najvecje)
            
            P = P.difference({v})
            X.add(v)

    return seznam_klik


# Bron-Kerboschov algoritem s pivotiranjem -------------------------------------------------
def Bron_Kerbosch_s_pivotiranjem(R, P, X, sl_vozlisc, samo_najvecje):
    return


# Bron-Kerboschov algoritem z urejanjem vozlišč ---------------------------------------------
def Bron_Kerbosch_z_urejanjem_vozlišč(R, P, X, sl_vozlisc, samo_najvecje):
    return


# Osnovna funkcija --------------------------------------------------------------------------
def Bron_Kerbosch_klic(omrezje, izbrani_algoritem, samo_najvecje=False):
    '''
        Algoritem vrne seznam maksimalnih klik za dano `omrezje`. Pri iskanju maksimalne klike uporabi
        algoritem na podlagi podanega parametra `izbrani_algoritem`:
            0 -> Bron_Kerboschov algoritem;
            1 -> Bron-Kerboschov algoritem s pivotiranjem;
            2 -> Bron-Kerboschov algoritem z urejanjem vozlišč.
        Algoritem vrne največje klike 
    '''
    if not isinstance(omrezje, Omrezje):
        raise TypeError("Podani parameter `omrezje` mora biti tipa `Omrezne`!")
    if not isinstance(izbrani_algoritem, int):
        raise TypeError("Podani parameter `izbrani_algoritem` mora biti celo število!")
    if izbrani_algoritem < 0 or 2 < izbrani_algoritem:
        raise ValueError("Podani parameter `izbrani_algoritem` mora biti celo število med vključno `0` in vključno `2`!")

    sl_vozlisc = omrezje.slovar_vozlisc

    R = set()
    P = set().union(elt for elt in list(sl_vozlisc.keys()))
    X = set()

    if izbrani_algoritem == 0:
        return Bron_Kerbosch(R, P, X, sl_vozlisc, samo_najvecje)
    elif izbrani_algoritem == 1:
        return Bron_Kerbosch_s_pivotiranjem(R, P, X, sl_vozlisc, samo_najvecje)
    elif izbrani_algoritem == 2:
        return Bron_Kerbosch_z_urejanjem_vozlišč(R, P, X, sl_vozlisc, samo_najvecje)


# TESTI -------------------------------------------------------------------------------------
if __name__ == '__main__':
    print('Začenjam testiranje ...')

    # (1.) preprosto omrežje -----------------------------------------------------------

    # (1.1) z enim vozliščem
    Omrezje.reset_nov_id()
    vozlisca_1_1 = [
        [1, ['Tina', 'Neki', 15, '030367945']],
    ]
    tabela_sosednosti_1_1 = dict()
    omrezje_1_1 = Omrezje(vozlisca=vozlisca_1_1, tabela_sosednosti=tabela_sosednosti_1_1)

    # (1.1.0) največje klike
    sez_klik_1_1_0 = Bron_Kerbosch_klic(omrezje_1_1, 0, False)
    rez = [{1}]
    if sez_klik_1_1_0 != rez:
        print(f"(1.1.0) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_1_1}, tabela_sosednosti={tabela_sosednosti_1_1}, 0)` vrne `{sez_klik_1_1_0}` namesto `{rez}`!")
    
    del sez_klik_1_1_0
    del rez

    # (1.1.1) Bron-Kerboschov algoritem
    sez_klik_1_1_1 = Bron_Kerbosch_klic(omrezje_1_1, 0, True)
    rez = [{1}]
    if sez_klik_1_1_1 != rez:
        print(f"(1.1.1) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_1_1}, tabela_sosednosti={tabela_sosednosti_1_1}, 0)` vrne `{sez_klik_1_1_1}` namesto `{rez}`!")
    
    del sez_klik_1_1_1

    # (1.1.2) Bron-Kerboschov algoritem s pivotiranjem
    #sez_klik_1_1_2 = Bron_Kerbosch_klic(omrezje_1_1, 1)

    # (1.1.3) Bron-Kerboschov algoritem z urejanjem vozlišč
    #sez_klik_1_1_3 = Bron_Kerbosch_klic(omrezje_1_1, 2)


    del vozlisca_1_1
    del tabela_sosednosti_1_1
    del omrezje_1_1
    del rez


    # (1.2) več med seboj nepovezanih vozlišč, nobenega povezanega
    Omrezje.reset_nov_id()
    vozlisca_1_2 = [
        [1, ['Tina', 'Neki', 15, '030367945']],
        [2, ['Miha', 'Blal', 21, '041123456']],
        [3, ['Klemen', 'Ble', 64, '031333444']],
        [4, ['Denis', 'Kmet', 59, '041556723']],
        [5, ['Niko', 'Mlad', 25, '030118789']],
        [6, ['Lea', 'Stoj', 90, '091999000']],
    ]
    tabela_sosednosti_1_2 = dict()
    omrezje_1_2 = Omrezje(vozlisca=vozlisca_1_2, tabela_sosednosti=tabela_sosednosti_1_2)

    # (1.2.0) največje klike
    sez_klik_1_2_0 = Bron_Kerbosch_klic(omrezje_1_2, 0, False)
    rez = [{1}, {2}, {3}, {4}, {5}, {6}]
    if sez_klik_1_2_0 != rez:
        print(f"(1.2.0) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_1_2}, tabela_sosednosti={tabela_sosednosti_1_2}, 0)` vrne `{sez_klik_1_2_0}` namesto `{rez}`!")

    del sez_klik_1_2_0
    del rez

    # (1.2.1) Bron-Kerboschov algoritem
    sez_klik_1_2_1 = Bron_Kerbosch_klic(omrezje_1_2, 0, True)
    rez = [{1}, {2}, {3}, {4}, {5}, {6}]
    if sez_klik_1_2_1 != rez:
        print(f"(1.2.1) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_1_2}, tabela_sosednosti={tabela_sosednosti_1_2}, 0)` vrne `{sez_klik_1_2_1}` namesto `{rez}`!")

    del sez_klik_1_2_1

    # (1.2.2) Bron-Kerboschov algoritem s pivotiranjem


    # (1.2.3) Bron-Kerboschov algoritem z urejanjem vozlišč



    del rez
    del vozlisca_1_2
    del tabela_sosednosti_1_2
    del omrezje_1_2


    # (1.3) majhno omrežje z eno povezavo
    Omrezje.reset_nov_id()
    vozlisca_1_3 = [
        [1, ['Tina', 'Neki', 15, '030367945']],
        [2, ['Miha', 'Blal', 21, '041123456']],
        [5, ['Klemen', 'Ble', 64, '031333444']],
    ]
    tabela_sosednosti_1_3 = {
        2: [5],
        5: [2],
    }
    omrezje_1_3 = Omrezje(vozlisca=vozlisca_1_3, tabela_sosednosti=tabela_sosednosti_1_3)

    # (1.3.0) največje klike
    sez_klik_1_3_0 = Bron_Kerbosch_klic(omrezje_1_3, 0, False)
    rez = [{1}, {2, 3}]
    if sez_klik_1_3_0 != rez:
        print(f"(1.3.0) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_1_3}, tabela_sosednosti={tabela_sosednosti_1_3}, 0)` vrne `{sez_klik_1_3_0}` namesto `{rez}`!")

    del sez_klik_1_3_0
    del rez

    # (1.3.1) Bron-Kerboschov algoritem
    sez_klik_1_3_1 = Bron_Kerbosch_klic(omrezje_1_3, 0, True)
    rez = [{2, 3}]
    if sez_klik_1_3_1 != rez:
        print(f"(1.3.1) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_1_3}, tabela_sosednosti={tabela_sosednosti_1_3}, 0)` vrne `{sez_klik_1_3_1}` namesto `{rez}`!")

    del sez_klik_1_3_1

    # (1.3.2) Bron-Kerboschov algoritem s pivotiranjem


    # (1.3.3) Bron-Kerboschov algoritem z urejanjem vozlišč


    del rez
    del vozlisca_1_3
    del tabela_sosednosti_1_3
    del omrezje_1_3


    # (2.) "kompleksno" omrežje ---------------------------------------------------------
    Omrezje.reset_nov_id()
    vozlisca_2 = [
        [1, ['Tina', 'Neki', 15, '030367945']],
        [2, ['Miha', 'Blal', 21, '041123456']],
        [3, ['Klemen', 'Ble', 64, '031333444']],
        [4, ['Denis', 'Kmet', 59, '041556723']],
        [5, ['Niko', 'Mlad', 25, '030118789']],
        [6, ['Lea', 'Stoj', 90, '091999000']],
    ]
    tabela_sosednosti_2 = {
        1: [2],
        2: [1, 3, 5],
        3: [2, 4, 5, 6],
        4: [3, 6],
        5: [2, 3, 6],
        6: [3, 4, 5],
    }
    omrezje_2 = Omrezje(vozlisca=vozlisca_2, tabela_sosednosti=tabela_sosednosti_2)

    # (2.0) največje klike
    sez_klik_2_0 = Bron_Kerbosch_klic(omrezje_2, 0, False)
    rez = [{1, 2}, {2, 3, 5}, {3, 4, 6}, {3, 5, 6}]
    if sez_klik_2_0 != rez:
        print(f"(2.0) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_2}, tabela_sosednosti={tabela_sosednosti_2}, 0)` vrne `{sez_klik_2_0}` namesto `{rez}`!")

    del sez_klik_2_0

    # (2.1) Bron-Kerboschov algoritem
    sez_klik_2_1 = Bron_Kerbosch_klic(omrezje_2, 0, True)
    rez = [{2, 3, 5}, {3, 4, 6}, {3, 5, 6}]
    if sez_klik_2_1 != rez:
        print(f"(2.1) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_2}, tabela_sosednosti={tabela_sosednosti_2}, 0)` vrne `{sez_klik_2_1}` namesto `{rez}`!")

    del sez_klik_2_1

    # (2.2) Bron-Kerboschov algoritem s pivotiranjem


    # (2.3) Bron-Kerboschov algoritem z urejanjem vozlišč


    

    del rez
    del vozlisca_2
    del tabela_sosednosti_2
    del omrezje_2


    # (3.) poln graf omrežja
    Omrezje.reset_nov_id()
    vozlisca_3 = [
        [1, ['Tina', 'Neki', 15, '030367945']],
        [2, ['Miha', 'Blal', 21, '041123456']],
        [3, ['Klemen', 'Ble', 64, '031333444']],
        [4, ['Denis', 'Kmet', 59, '041556723']],
        [5, ['Niko', 'Mlad', 25, '030118789']],
        [6, ['Lea', 'Stoj', 90, '091999000']],
    ]
    tabela_sosednosti_3 = {
        1: [2, 3, 4, 5, 6],
        2: [1, 3, 4, 5, 6],
        3: [1, 2, 4, 5, 6],
        4: [1, 2, 3, 5, 6],
        5: [1, 2, 3, 4, 6],
        6: [1, 2, 3, 4, 5],
    }
    omrezje_3 = Omrezje(vozlisca=vozlisca_3, tabela_sosednosti=tabela_sosednosti_3)
    
    #(3.0) največje klike
    sez_klik_3_0 = Bron_Kerbosch_klic(omrezje_3, 0, True)
    rez = [{1, 2, 3, 4, 5, 6}]
    if sez_klik_3_0 != rez:
        print(f"(2.1) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_3}, tabela_sosednosti={tabela_sosednosti_3}, 0)` vrne `{sez_klik_3_0}` namesto `{rez}`!")

    del sez_klik_3_0

    # (3.1) Bron-Kerboschov algoritem
    sez_klik_3_1 = Bron_Kerbosch_klic(omrezje_3, 0, False)
    rez = [{1, 2, 3, 4, 5, 6}]
    if sez_klik_3_1 != rez:
        print(f"(2.1) `Bron_Kerbosch_klic(Omrezje(vozlisca={vozlisca_3}, tabela_sosednosti={tabela_sosednosti_3}, 0)` vrne `{sez_klik_3_1}` namesto `{rez}`!")

    del sez_klik_3_1

    # (3.2) Bron-Kerboschov algoritem s pivotiranjem


    # (3.3) Bron-Kerboschov algoritem z urejanjem vozlišč


    

    del rez
    del vozlisca_3
    del tabela_sosednosti_3
    del omrezje_3




    print('Testiranje zaključeno.')