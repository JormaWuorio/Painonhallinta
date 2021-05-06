# Konsolisovelluksen lopullinen pääohjelma

# Modulien ja kirjastojen lataukset
import kanta # Tietokannan käsittelyssä tarvittavat komponentit
import kysymys # Tietojen syöttämiseen liittyvät kysymisrutiinit
import luokat # Henkilö, Aikuinen ja Lapsi -luokkien määrittelyt

tiedosto = 'painonhallinta.db' # Tietokantatiedoston määrittely
# Varsinainen ohjema
while True:
    
    # Silmukka henkilötietojen kyselemiseen
    lisaa_henkiloita = input('Lisätäänkö uusia henkilöitä? K/e')
    if lisaa_henkiloita.upper() != 'E':
        lisaa_henkiloita = 'K'

    while lisaa_henkiloita.upper() == 'K':

        # Kysytään henkilötiedot
        etunimi = input('etunimi: ')
        sukunimi = input('sukunimi: ')
        sukupuoli = kysymys.kysy_liukuluku('Sukupuoli nainen 0, mies 1: ', 0, 1)
        syntyma_aika = input('Syntymäaika (VVVV-KK-PP): ') 

        # Lisätään henkilö tietokantaan
        try:
            kanta.lisaa_henkilo(tiedosto, etunimi, sukunimi, sukupuoli, syntyma_aika)
        except:
            print("Tietokantaan tallennuksessa tapahtui virhe")    

        lisaa_henkiloita = input('Lisätäänkö uusia henkilöitä? K/e')
        if lisaa_henkiloita.upper() == 'E':
            break
        else:
            lisaa_henkiloita = 'K'

        

    # Silmukka mittaustietojen kyselemiseen
    lisaa_mittauksia = input('Lisätäänkö uusia mittaustuloksia? k/E')
    while lisaa_mittauksia.upper() == 'K':
        henkilo_id = input("Anna henkilön id: ")
        pituus = kysymys.kysy_liukuluku('Pituus (cm): ', 100, 250)
        paino = kysymys.kysy_liukuluku('Paino (kg): ', 30, 200)
        try:
            kanta.lisaa_mittaus(tiedosto, henkilo_id, pituus, paino)
        except:
            print("Tietokantaan tallennuksessa tapahtui virhe")    
        lisaa_mittauksia = input('Lisätäänkö uusia mittaustuloksia? k/E')
        if lisaa_mittauksia.upper() == 'E':
            break
        else:
            lisaa_henkiloita = 'K'

    # Silmukka olioiden luomiseen ja tulosten näyttämiseen
    lisaa_tuloksia = input('Lasketaanko uusia tuloksia? k/E')
    while lisaa_tuloksia.upper() == 'K':
        henkilo_id = input("Anna henkilön id: ")
        # Haetaan henkilö- ja mittaustiedot tietokannan henkilon_viimeiset_tiedot-näkymästä
        tapahtui_virhe = False
        try:
            tietue = kanta.lue_viimeiset_tiedot(tiedosto, henkilo_id)
        except:
            print("Tietokantaan lukemisessa tapahtui virhe")
            tapahtui_virhe = True     
        
        if tapahtui_virhe == False:
            etunimi = tietue[0][1]
            sukunimi = tietue[0][2]
            sukupuoli = tietue[0][3]
            pituus = tietue[0][4]
            paino = tietue[0][5]
            ika = round(tietue[0][6])

        if ika < 18:
            lapsi = luokat.Lapsi(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
            print("Painoindeksi on:", lapsi.painoindeksi())
            print("Rasvaprosentti on:", lapsi.rasvaprosentti())
        else:
            tavoitepaino = float(input("Anna tavoitepaino: "))
            aikuinen = luokat.Aikuinen(etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino)
            print("Painoindeksi on:", aikuinen.painoindeksi())
            print("Rasvaprosentti on:", aikuinen.rasvaprosentti())

        lisaa_tuloksia = input('Lasketaanko uusia tuloksia? k/E')
        if lisaa_tuloksia.upper() == 'E':
            break
        else:
            lisaa_tuloksia = 'K'