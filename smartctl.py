#!/usr/bin/python

from os import system as ss
from time import sleep as sl
from os import popen as pop
import os












while True:

 passs1 = list(pop('smartctl -H /dev/sda1').read())
 os.system('smartctl -H /dev/sda1')
 sl(1)
 passs2 = list(pop('smartctl -H /dev/sda2').read())
 os.system('smartctl -H /dev/sda2')
 sl(1)
 passs3 = list(pop('smartctl -H /dev/sda5').read())
 os.system('smartctl -H /dev/sda5')
 sl(1)
 passs4 = list(pop('smartctl -H /dev/sda6').read())
 os.system('smartctl -H /dev/sda6')
 sl(1)

 oke1 = []
 oke2 = []
 oke3 = []
 oke4 = []



 oke1.append(passs1[-8])
 oke1.append(passs1[-7])
 oke1.append(passs1[-6])
 oke1.append(passs1[-5])
 oke1.append(passs1[-4])
 oke1.append(passs1[-3])

 oke2.append(passs2[-8])
 oke2.append(passs2[-7])
 oke2.append(passs2[-6])
 oke2.append(passs2[-5])
 oke2.append(passs2[-4])
 oke2.append(passs2[-3])

 oke3.append(passs3[-8])
 oke3.append(passs3[-7])
 oke3.append(passs3[-6])
 oke3.append(passs3[-5])
 oke3.append(passs3[-4])
 oke3.append(passs3[-3])

 oke4.append(passs4[-8])
 oke4.append(passs4[-7])
 oke4.append(passs4[-6])
 oke4.append(passs4[-5])
 oke4.append(passs4[-4])
 oke4.append(passs4[-3])
  

 
 if ('P' and 'A' and 'S' and 'S' and 'E' and 'D') not in oke1:
  break
  os.system("""zenity --error --text="coba cek dulu" --title='kayaknya ada yang ga passs'""")
  exit()
 if ('P' and 'A' and 'S' and 'S' and 'E' and 'D') not in oke2:
  break
  os.system("""zenity --error --text="coba cek dulu" --title='kayaknya ada yang ga passs'""")
  exit()
 if ('P' and 'A' and 'S' and 'S' and 'E' and 'D') not in oke3:
  break
  os.system("""zenity --error --text="coba cek dulu" --title='kayaknya ada yang ga passs'""")
  exit()
 if ('P' and 'A' and 'S' and 'S' and 'E' and 'D') not in oke4:
  break
  os.system("""zenity --error --text="coba cek dulu" --title='kayaknya ada yang ga passs'""")
  exit()


 oke1.clear()
 oke2.clear()
 oke3.clear()
 oke4.clear()

