#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:30:18 2022

@author: iremcinar
"""
#Telefon numarası hangi ülke, şehire ait?
!pip install phonenumbers
import phonenumbers
from phonenumbers import geocoder

number1='+905333371000'
number3='+902125121278'
number4='+903122441245'
number5='+902164414512'
number9='+14103333344'

#numarayı parse ile bölüyoruz.
number18 = phonenumbers.parse(number1) 
#numaranın hangi bölgeye ait olduğunu ve hangi dilde sonuç vermesini istediğimizi belirtiyoruz.
print(geocoder.description_for_number(number18,'tr')) 

number19 = phonenumbers.parse(number3)
print(geocoder.description_for_number(number19,'tr'))

number20 = phonenumbers.parse(number4)
print(geocoder.description_for_number(number20,'tr'))

number21 = phonenumbers.parse(number5)
print(geocoder.description_for_number(number21,'tr'))

number26 = phonenumbers.parse(number9)
print(geocoder.description_for_number(number26,'tr'))

#Telefon numarası hangi operatöre ait?
from phonenumbers import carrier

number2='+905354321938'
number6='+905353415643'
number7='+905422388080'
number8='+905444321939'
#numarayı parse ile bölüyoruz
number18 = phonenumbers.parse(number2)
#numaranın hangi operatöre ait olduğunu buluyoruz.
print(carrier.name_for_number(number18,'tr'))

number23 = phonenumbers.parse(number7)
print(carrier.name_for_number(number23,'tr'))

#Metin içerisinden telefon numarasını nasıl alırız?
from phonenumbers import phonenumbermatcher

text = "Beni lütfen öğlen 1'den sonra 05412009999 numarasından arayın"
for match in phonenumbers.PhoneNumberMatcher(text, "TR"):
    print(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat))

#Telefon numarası hangi zaman dilimine ait?
from phonenumbers import timezone

gb_number = phonenumbers.parse("+447986123456", "TR")
timezone.time_zones_for_number(gb_number)
