# Auto-luokkien määritykset

class Auto():
    # Olionmuodostin eli konstruktori yliluokalle Auto
    def __init__(self, rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot, s_tilavuus, hinta):
        """Auto-luokka malline auto-olioille yliluokka eri autotyypeille

        Args:
            rek (string): Auton rekisterinumero esim. CPM-186
            merkki (string): Auton valmistaja
            malli (string): Tyyppimerkintä
            vm (integer): Vuosimalli
            km (integer): Ajetut kilometrit
            kvoima (string): Käyttövoima; diesel, bensiini, hybridi, sähkö, kaasu, vety
            vaihteisto (string): Vaihteiston tyyppi; käsi, automaatti
            vari (string): Auton pääväri
            paastot (integer): Hiilidioksidipäästö g/km
            s_tilavuus (float): Sylinteritilavuus l
            hinta (float): Auton myyntihinta Eur
        """
        self.rek = rek
        self.merkki = merkki
        self.malli = malli
        self.vm = vm
        self.km = km
        self.kvoima = kvoima
        self.vaihteisto = vaihteisto
        self.vari = vari
        self.paastot = paastot
        self.s_tilavuus = s_tilavuus
        self.hinta = hinta

    # Metodi jäjellä olevien kilometrien arviointiin
    def km_jaljella(self):
        kilometreja = self.s_tilavuus * 100000 - self.km
        return kilometreja

    # Metodi jäljellä olien kilometrien kustannusten arviointiin
    def km_jaljella_hinta(self):
        km_hinta = self.hinta / (self.s_tilavuus * 100000 - self.km) 
        return km_hinta

    # Metodi, jolla voi laskea korjatun jäljellä olevan kilometrimäärän
    def korjatut_kilometrit(self, kerroin):
        """Mahdollistaa korjatun jäljellä olevien kilometrien laskennan

        Args:
            kerroin (float): Korjauskerroin hybrideillä 1.5, dieseleillä 2

        Returns:
            float: Arvio jäljellä olevista ajokilometreistä
        """
        jaljella_km = (self.s_tilavuus * kerroin * 100000 - self.km) 
        return jaljella_km

    # Staattinen metodi jäljellä olevien kilometrien laskemiseen
    @staticmethod
    def arvioi_kilometrit(sylinteritilavuus, mittarilukema, korjauskerroin):
        """Laskee arvion jäljellä olevista ajokilometeistä

        Args:
            sylinteritilavuus (float): Sylinteritilavuus litroina
            mittarilukema (integer): Matkamittarin lukema
            korjauskerroin (float): Korjauskerroin Diesel 2.0, Hybridi 1.3, Bensiini 1.0

        Returns:
            float: Arvio auton jäjljellä olevasta kilometrimäärästä
        """
        jaljella_km = sylinteritilavuus * korjauskerroin * 100000 - mittarilukema
        return jaljella_km

    # Henkilöauton aliluokka, yliluokkana Auto, perii kaikki Auto-luokan ominaisuudet
class Henkiloauto(Auto):
        # Henkiloauto-objektien konstruktori
    def __init__(self,  rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot, s_tilavuus, hinta, istuimet, ovet, korimalli, tavaratila, lisavarusteet):
        super().__init__(rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot, s_tilavuus, hinta)
        """Henkilöaoutoluokka, yliluokkana Auto-luokka

        Args:
            istuimet (integer): Penkkien määrä
            ovet (integer): Ovien määrä
            korimalli (string): Mallit; porrasperä, viistoperä, farmari, tila-auto
            tavaratila (integer): Tavaratilan tilavuus litroina
            lisavarusteet (list): Lista lisävarusteista
        """
        self.istuimet = istuimet
        self.ovet = ovet
        self.korimalli = korimalli
        self.tavaratila = tavaratila
        self.lisavarusteet = lisavarusteet

if __name__ == "__main__":
    henkiloauto1 = Henkiloauto('CYF-67','Land-Rover','Discovery 3 HS',2008, 242558, 'diesel', 'automaatti', 'vihreä', 270, 2.8, 5000, 7, 5, 'tila-auto', 300,['vakionopeuden säädin', 'peruutuskamera'])
    print('Rekisterinumero:', henkiloauto1.rek, 'istumapaikkoja:', henkiloauto1.istuimet)

# Lasketaan jäljelläolevien kilometrien hinta 

print('Jäljellä olevat kilometrit:', henkiloauto1.km_jaljella())

print('Jäljellä olevien kilometrien hinta on', henkiloauto1.km_jaljella_hinta())

print('Korjatut kilometrit on:', henkiloauto1.korjatut_kilometrit(2))

kilometreja_jaljella = Auto.arvioi_kilometrit(2.8, 364800, 2)

print('Laskettu staattisella metodilla:', kilometreja_jaljella)