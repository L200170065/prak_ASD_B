class MhsTIF(object):
    def __init__(self, nama, NIM, alamat,us):
        self.nama = nama
        self.NIM = NIM
        self.alamat = alamat
        self.us = us

    def __str__(self):
        s = self.nama + "NIM" + str(self.NIM)\
            + ". Tinggal di " + self.alamat\
            + ". Uang Saku Rp. " + str(self.us)\
            + " Tiap Bulannya."
        
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
#Nomor1    
Daftar = [MhsTIF('Anom', "L200170071", 'Sukoharjo', 150000),
          MhsTIF('Lutfi', "L200170048", 'Karanganyar', 125000),
          MhsTIF('Gentur', "L200170085", 'Surakarta', 20500),
          MhsTIF('Alvicky', "L200170065", 'Sragen', 350000),
          MhsTIF('Bayu', "L200170052", 'Sragen', 500000),
          MhsTIF('Kori', "L200170053", 'Surakarta', 430000),
          MhsTIF('Susi', "L200170047", 'Bojonegoro', 450000),
          MhsTIF('Rima', "L200170044", 'Klaten', 430000),
          MhsTIF('Sidiq', "L200170058", 'Klaten', 235000),
          MhsTIF('Yoga', "L200170034", 'Karanganyar', 350000)]

def cekNIM(object):
    for i in object:
        print (i.NIM)
         
          
def urutNIM(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].NIM > object[j+1].NIM:
                swap(object,j,j+1)