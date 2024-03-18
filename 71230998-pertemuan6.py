#!/usr/bin/env python
# coding: utf-8

# In[7]:


#soal 6.1
def cariprima(prim):
    for p in range(2, prim):
        if prim % p == 0:
            return False 
    return True

def prima_deket(user):
    while user > 0:
        user -= 1
        if cariprima(user):
            return user
    return None

user = int(input("Silahkan input angka: "))
prima_yang_deket = prima_deket(user)

if prima_yang_deket:
    print(f"bilangan prima terdekat {user} adalah {prima_yang_deket}")


# In[27]:


def faktor(fak):
    if fak == 0 or fak == 1:
        return 1
    else:
        return fak * faktor(fak - 1)

def rinci(y):
    for f in range(y, 0, -1):
        print(faktor(f), end=" ")
        for a in range(f, 0, -1):
            print(a, end=" ")
        print()

cari = int(input("Masukkan nilai n: "))
rinci(cari)


# In[29]:


def inideret(tinggi,lebar):
    dari = 0
    for d in range(tinggi+1):
        for r in range(lebar+1):
            dari = dari + 1
            print(dari," ", end = "")
        print()
        
tinggi = int(input("masukan tingginya: "))
lebar = int(input("masukan lebarnya: "))

inideret(tinggi,lebar)


# In[ ]:




