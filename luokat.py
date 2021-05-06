# Tässä modulissa määritellään luokat painonhallintasovellukseen

# Modulien ja kirjastojen lataukset


# Henkilö-luokka

class Henkilo:
    """Yliluokka kaikille henkilötyypeille"""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):
        # Kenttien / ominaisuuksien asetukset
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli

    # Metodi painoindeksin laskentaan olion painon ja pituuden perusteella, huom. self-argumentti
    def painoindeksi(self):
        bmi = self.paino / (self.pituus / 100) ** 2
        return bmi

    # Vaihtoehtona staattinen metodi, jolla painoindeksi lasketaan suoraan luokasta, huon. ei self-argumenttia
    @staticmethod
    def bmi(pituus, paino):
        bmi = paino / (pituus/100)**2
        return bmi

# Aliluokka aikuiselle henkilölle, perii Henkilö-luokan
class Aikuinen(Henkilo):
    """Aliluokka aikuiselle henkilölle, perii Henkilo-luokan ominaisuudet
    ja metodit
    """
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
        super().__init__(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        self.tavoitepaino = tavoitepaino

    def rasvaprosentti(self):
        rasvaprosentti = 1.2 * self.painoindeksi() + 0.23 * self.ika - 10.8 * self.sukupuoli - 5.4
        return rasvaprosentti
# Aliluokka lapselle, perii Henkilö-luokan 
class Lapsi(Henkilo):
    """Henkilöluokan aliluokka lapsille."""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):
        super().__init__(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        
    def rasvaprosentti(self):
        rasvaprosentti = 1.51 * self.painoindeksi() - 0.70 * self.ika - 3.6 * self.sukupuoli + 1.4
        return rasvaprosentti    

# Tässä tiedostossa tehtävät testit
if __name__ == "__main__":
    mikaV = Henkilo('Mika', 'Vainio', 171, 74, 59, 1)
    print('Henkilö painaa', mikaV.paino)

    mikaV.painoindeksi()

    mikaV2 = Aikuinen('Mika', 'Vainio', 171, 74, 59, 1, 70)
    print(mikaV2.etunimi, 'painoindeksi', mikaV2.painoindeksi())
    print(mikaV2.etunimi, 'rasvaprosentti', mikaV2.rasvaprosentti())

    # Lasketaan painoindeksi staattisella metodilla
    pituus = 171
    paino = 75

    print('Paino indeksi on ', Henkilo.bmi(pituus, paino))


    
        

