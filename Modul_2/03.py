class Mahasiswa(object):
    """Class mahasiswa dengan berbagai metode"""
    def __init__(self, nama, nim, kota,us):
        self.nama = nama
        self.NIM = nim
        self.kotaTinggal = kota
        self.uangSaku = us
        
    def __str__(self):
        s = self.nama + ", NIM ", + str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uang saku Rp. " + str(self.uangSaku) \
            + " tiap bulannya"
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s," Sambil velajar.")
        self.keadaan= "kenyang"

#   (a)
    def ambilKotaTinggal(self):
        return self.kotaTinggal

#   (b)
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru

#   (c)
    def tambahUangSaku(self, tambah):
        self.tambahSaku = tambah
        self.uangSaku += tambah
