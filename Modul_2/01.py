class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep class dan object
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print self.teks
    def cetakPakaiHurufKapital(self):
        print str.upper(self.teks)
    def cetakPakaiHurufKecil(self):
        print str.lower(self.teks)
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print "Kalimatku memiliki", len(self.teks), "karakter"
    def perbarui(self, stringBaru):
        self.teks = stringBaru

#   (a)
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else:
            return False

#   (b)
    def hitungKonsonan(self):
        a = 0
        vokal = "AaIiUuEeOo"
        for i in self.teks:
            if i not in vokal:
                a += 1
        return a

#   (c)
    def hitungVokal(self):
        a = 0
        vokal = "AaIiUuEeOo"
        for i in self.teks:
            if i in vokal:
                a += 1
        return a
