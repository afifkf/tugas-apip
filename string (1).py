#!/usr/bin/env python
# coding: utf-8

# In[4]:


nama_lengkap = input ("Masukkan Nama Anda : ")

# Menghitung jumlah huruf dari nama lengkap
jmlh_huruf = len(nama_lengkap.replace(" ", ""))

# Menghitung jumlah huruf vokal dari nama lengkap
huruf_vokal = "aiueoAIUEO"
jmlh_vokal = len([char for char in nama_lengkap if char in huruf_vokal])

# Menghitung jumlah huruf konsonan dari nama lengkap
jmlh_konsonan = jmlh_huruf - jmlh_vokal

print("Jumlah huruf dari nama lengkap Anda adalah:", jmlh_huruf)
print("Jumlah huruf vokal dari nama lengkap Anda adalah:", jmlh_vokal)
print("Jumlah huruf konsonan dari nama lengkap Anda adalah:", jmlh_konsonan)


# In[ ]:




