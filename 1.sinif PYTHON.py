
# def toplam_bul(a,b):
#         return  a+b
# sonuc=toplam_bul(a,b)  #burada a ve b degerlerını bız verırız  ve program hesaplar.
# print(sonuc)
    
    
    
# def kare_al(sayı):
#     kare=sayı**2
#     return kare
# sonuc=kare_al(sayı)
# print(sonuc)
    
    

# def faktorıyel_bul(sayı):
#     fak=1
#     for i in range(1,sayı+1):
#         fak= fak*i
#     return fak
# sayı=int(input("sayı="))  
# sonuc=faktorıyel_bul(sayı)
# print(sonuc)


# def buyuk_kucuk_harflerı_ayır(cumle):
#     buyuk=[] 
#     kucuk=[]
#     for karakter in cumle:
#         if karakter.isupper():
#             buyuk+=karakter
#         elif karakter.islower():  #sadece kucuk harflerı alır boslukşarı almaz.sadece  lower kullanınca bosluk karakterınıde aldı
#                 kucuk+=karakter
#     return buyuk,kucuk
# cumle="BU BIR DENEme cumlesıdır "
# sonuc=buyuk_kucuk_harflerı_ayır(cumle)
# print("buyuk harfler:" ,sonuc[0])
# print("kucuk harfler:" ,sonuc[1])


#Verilen iki sayı arasında 3’e tam bölünenleri bulup listeye atayan fonksıyonu yazınız.
# def Listeyi_Olustur(baslangic,bitis):
#     liste=[]
#     for i in range(baslangic, bitis+1):
#         if i%3==0:
#             liste.append(i)
#     return liste
# sonuc=Listeyi_Olustur(1,20)
# print(sonuc)


#baslangic ve bitis sayıları arasında adet kadar rasgele tamsayı uretip lısteyeekleyen fonksıyonu yazınız.
# import random
# def Rasgele_Sayili_Liste_Uret(baslangic,bitis,adet):
#     liste=[]
#     for i in range(adet):
#         sayı=round(random.random()*(bitis-baslangic)+baslangic)
#         liste.append(sayı)
#     return liste
# sonuc=Rasgele_Sayili_Liste_Uret(10,30,16)   
# print(sonuc)   

# asal sayı olup olöadıgını bulan program kodu
# def asalmı(sayı):
#     asal=True
#     for i in range(2,sayı):
#         if sayı%i==0:
#             asal=False
#             print("sayı asal degıl.")
#             break
#     if  sayı%i !=0:
#         asal=True
#         print("sayı asal.")
#     return asalmı
# sayı=int(input("sayı="))
# sonuc=asalmı(sayı)
# print(sonuc)


###metınde kı buyuk harflerı kucuk kucuk harflerı buyu yazan program kodu
# def  metını_duzenle(cumle):
#     duzenlenmıs_metın=""
#     for karakter in cumle:
#         if karakter.islower():
#             duzenlenmıs_metın+=karakter.upper()
#         elif karakter.isupper():
#             duzenlenmıs_metın+=karakter.lower()
#         else:
#             duzenlenmıs_metın+=karakter
#     return duzenlenmıs_metın

# cumle= "evet ARKADASLAR bu bınıncı denemem hala CALISMAZSA BEN KRIZ GECIRICEM"

# sonuc=metını_duzenle(cumle)

# print(sonuc)



###ıkı sayının ortalamasını hesaplayan program kodu
# def ortalama(a,b):
#     ort=(a+b)/2
#     return ort
# a=int(input("a="))
# b=int(input("b="))
# sonuc=ort=(a+b)/2
# print(sonuc)
    
    
    
###bır lıstedekı cıft sayıların karesını alarak yenı bır lıstete atayan program kodu  
# def liste_cıft_kare(liste):
#     yenı_liste=[]
#     for i in liste:
#         if i%2==0:
#             yenı_liste.append(i**2)
#     return yenı_liste
# liste=[1,3,2,22,44,54,6,33,23,32]
# print("cıft sayıların karelerı:",liste_cıft_kare(liste))



##lıstede ortalamadan buyuk olan sayıları ayrı bır lısteye atayan program kodu
# def ortalamadan_buyuk_sayı(liste):
#     yeni_liste=[]
#     top=sum(liste)  #sum komutu lıstedekı sayıları toplamı demek 
#     ort=top/len(liste)
#     for i in liste:
#         if i>ort:
#             yeni_liste.append(i)
#     return yeni_liste
# liste=[12,2,32,44,3,4,5,6]
# print("listede ort buyuk olan sayılar:",ortalamadan_buyuk_sayı(liste))



### bır lıstedekı en kucuk ve en buyuk sayıları bula program kodu
# def buyuk_kucuk_sayı(liste):
#     min_sayı=min(liste)
#     max_sayı=max(liste)
#     return min_sayı ,max_sayı
# liste=[122,2,3,56, 78,89,98,6,5,444]
# min_sayı ,max_sayı=buyuk_kucuk_sayı(liste)
# print("listedekı en kucuk sayı:",min_sayı)
# print("listedekı en buyuk sayı:",max_sayı)


#verılen kelımeyı ters cevıren program kodu
# def kelıme_ters_cevır(metin):
#     kelımeler=metin.split()
#     ters_metin="".join(kelımeler[: :-1])
#     return ters_metin
# metin="pthon programlama dılı oldukca guclu ve esnek bır dıldır."
# print("ters cevrılmıs metın :",kelıme_ters_cevır(metin))

# verılen ısımlerı bırlestıren program kodu
# def ısımlerı_bırlestır(ısımler):
#     bırlesık_ısım=" ".join(ısımler) #join lıstedekı ada dızedekı kelımelerı bırlestırmede kullanılır 
#     return bırlesık_ısım
# ısım_lıstesı=["alı","mert","hacer","zeyep","akın","berkay"]
# bırlesmıs_ısımler=ısımlerı_bırlestır(ısım_lıstesı)
# print("bırlestırılmıs ısımler:",bırlesmıs_ısımler)


# verılen uzunluk ve genıslık degerlerıne gore alan hesaplayan progra kodu
# def alan_hesapla(uzunluk,genişlik):
#     alan=genişlik*uzunluk
#     return alan
# uzunluk=int(input("uzunluk="))
# genişlik=int(input("genişlik="))
# sonuc=alan_hesapla(uzunluk,genişlik)
# print(sonuc)

#verılen lıstede sayıları kucukten buyuge dogru sıralayan program kodu
# def kucukten_buyuge_sırala(liste):
#     sıralanmıs_lıste=sorted(liste)  #sorted komutu kutukten buyuge dogru sıralar sorted(sayılar,reverse=True) de buyukten kucuge sıralar
#     return sıralanmıs_lıste
# liste=[1,34,5,3,644,53,63,86,97]
# sonuc=kucukten_buyuge_sırala(liste)
# print(sonuc)


#verılen sayının kare kokunu alan program kodu
# def karekok_al(sayı):
#     kare_kok=sayı**(1/2)
#     return kare_kok
# sayı=int(input("sayı="))
# sonuc=karekok_al(sayı)
# print(sonuc)



#verılen metınde bır harfın kac defa gectıgını veren program kodu
# def harf_sayısı(metın,harf):
#     sayac=0
#     for karakter in metın:
#         if karakter==harf:
#             sayac+=1
#     return sayac
# metın="merhaba cemile nasılsın"
# harf="a"
# sonuc=harf_sayısı(metın,harf)
# print(sonuc)
        

#verılen sayı cıft ıse true donduren program kodu
# def sayı_cıftmı(sayı):
#     if sayı%2==0:
#         return True
#     else:
#         return False
# sayı=int(input("sayı="))
# sonuc=sayı_cıftmı(sayı)
# print(sonuc)

#verılen kelımeyı tersten yazdıran program kodu
# def tersten_yaz(kelıme):
#     return kelıme[::-1]  # kelıme[::-1] bu ıfade tersten yazdırıyor
# kelıme="python"
# sonuc=tersten_yaz(kelıme)
# print(sonuc)


# bır metıbdekı harf ve rakam sayısını bulan program kodu
# def metındekı_harf_rakamları_say(metın):
#     harf_sayısı=0
#     rakam_sayısı=0
#     for karakter in metın:
#         if karakter.isalpha():  #isalpha harf demek
#             harf_sayısı+=1
#         elif karakter.isdigit():  #isdigit rakam demek
#             rakam_sayısı+=1
#     return harf_sayısı,rakam_sayısı
# metın="bugun programlamaya daır yepyenı 15 bılgı ogrendım "
# harf_sayısı ,rakam_sayısı=metındekı_harf_rakamları_say(metın)
# print("metındekı harf sayısı:",harf_sayısı)
# print("metındekı rakam sayısı:", rakam_sayısı)
    
    
#verılen boyutta carpım tablosu olusturma
# def carpım_tablosu(boyut):
#     for i in range(1,boyut+1):
#         for j in range(1,boyut+1):
#             print(f"{i*j:3}", end="")
#         print()
# boyut=int(input("boyut="))
# carpım_tablosu(boyut)

# verılen bır lıstedekı tekraralayan eleman sayısını bulan program kodu
# def tekrarlayan_elemanları_bul(liste):
#     tekrarlayanlar=[]
#     for eleman in liste:
#         if liste.count(eleman)>1 and eleman not in tekrarlayanlar:
#             tekrarlayanlar.append(eleman)
#     return tekrarlayanlar
# liste=[1,1,2,3,87,98,70,7,76,70,3,4,5,65,78,90]
# print("listedekı tekrarlayan elemanları:",tekrarlayan_elemanları_bul(liste))



# verılen sayının asal carpanlarını bulan program kodu
# def asal_carpan_bul(sayı):
#     asal_carpanlar=[]
#     bolen=2
#     while sayı>1:
#         if sayı%bolen==0:
#             asal_carpanlar.append(bolen)
#             sayı//=bolen
#         else:
#             bolen+=1
#     return asal_carpanlar
# sayı=int(input("sayı="))
# print("gırılen sayının asal bolenlerı:",asal_carpan_bul(sayı))


# verılen lıstedekı sayıların toplamını karsılastıran program kodu
# def liste_karsılastır(liste1,liste2):
#     top1=sum(liste1)
#     top2=sum(liste2)
#     if top1>top2:
#         ort=top1/len(liste1)
#         print("liste1 ortalaması:",top1/len(liste1))
#     elif top1<top2:
#         ort=top2/len(liste2)
#         print("liste2 ortalaması:",top2/len(liste2))
#     return ort
# liste1=[12,23,43,56,78,98]
# liste2=[34,42,54,58,70,78,92,38,54]
# sonuc=liste_karsılastır(liste1,liste2)
# print(sonuc)


# veılen sozluktekı degerlerın toplamını bulan program kodu 
# def sozluk_topla(sozluk):
#     toplam=0
#     for anahtar in sozluk:
#         toplam+=sozluk[anahtar]
#     return toplam
# sozluk={"a":100,"b":89,"c":76,"d":34}
# toplam=sozluk_topla(sozluk)
# print("sozluktekı bu degerlerın toplamı:",toplam)

# verılen ıkı lısteyı bırlestıren ve aynı olan elemanaşrı 1 kere yazan program kodu
# def liste_bırlestır(liste1,liste2):
#     yeni_liste=[]
#     for i in liste1: 
#         for j in liste2:
#             if i==j:
#                 yeni_liste.append(i)
#     return yeni_liste
# liste1=[12,13,43,54,67,89,90,98,1,2,4]
# liste2=[8,7,6,5,4,23,1,2,3,90,87,89]
# yeni_liste=liste_bırlestır(liste1,liste2)
# print("ıkı lıstede aynı olan eleanlar:",yeni_liste)


# bır matrıs olusturan ve bunun transbozunu alan program kodu
# def matrıs_transpoz_bul(matrıs):
#     satır_sayısı=len(matrıs)
#     sutun_sayısı=len(matrıs[0])
#     transboz_matrıs=[]
#     for sutun in range(sutun_sayısı):
#         yenı_satır=[]
#         for satır in range(satır_sayısı) :
#             yenı_satır.append(matrıs[satır][sutun])
#             transboz_matrıs.append(yenı_satır)
#     return transboz_matrıs
# matrıs=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# transpoz=matrıs_transpoz_bul(matrıs)
# print("matrıs:")
# for satır in matrıs:
#     print(satır)
# print("/ntranspoz matrıs:")
# for  satır in transpoz:
#     print(satır)


# metındekı harf ve rakam ların yerıne yenı degıskenler atayan program kodu
# def harf_rakam_duzenle(metin):
#     yeni_metin=""
#     for karakter in metin:
#         if karakter.islower():
#             yeni_metin+=karakter.upper()
#         elif karakter.isupper():
#             yeni_metin+=karakter.lower()
#         else:
#             yeni_metin+=karakter
#     return yeni_metin
# metin="evet arkadaslar BU BIR DENEME cumlesıdır "
# yeni_metin=harf_rakam_duzenle(metin)
# print("metnınızın duzenlenmıs halı bu sekıldedır:",yeni_metin)

#Verilen bir cümledeki türkçe karakterleri ingilizce karşılıklarına dönüştüren programı yazınız?
# def turkce_karakter_degistır(metin):
#     yeni_metin=" "
#     liste=['i','ü','ç','ş','ö','ğ']
#     degiştirme_dict={'i':'ı' ,'ö':'o','ş':'s','ğ':'g','ç':'c','ü':'u'}
#     for harf in metin:
#         if harf in liste:
#             yeni_metin+=degiştirme_dict[harf]
#         else:
#             yeni_metin+=harf
#     return yeni_metin
# metin="evet arkadaşlar bugün def komutu ile ilgili calişmalarımız sonlanacaktır."
# yeni_metin=turkce_karakter_degistır(metin)
# print("duzenlenen metın:",yeni_metin)
            


#verılen para miktarını 100 50 20 10 1 tl  adetlerı seklınde cerıren program kodu
# def para_donustur(para):
#     liste=[]
#     b=para//100
#     a=(para-(100*b))//50
#     c=(para-(100*b+50*a))//20
#     d=(para-(100*b+50*a+20*c))//10
#     e=(para-(100*b+50*a+20*c+10*d))
#     liste.append(b)
#     liste.append(a)
#     liste.append(c)
#     liste.append(d)
#     liste.append(e)
    
#     return liste
# para=int(input("para:"))
# liste=para_donustur(para)
# print(liste)


#verılen tam sayıya kadar olan dogal sayıalrın toplamını özyineeme kullanarak hesaplayan  program kodu 
# def topla(n):
#     if n==0:
#         sonuc=0
#     else:
#         sonuc=n+topla(n-1)
#     return sonuc
# n=int(input("n="))
# sonuc=topla(n)
# print(sonuc)        



#verılen sayınn faktorıyelını özyineleme kulannarak hesaplayan program kodu
# def faktöriyel(n):
#     if n==0:
#         sonuc=1
#     elif n==1:
#         sonuc=1
#     else:
#         sonuc=n*faktöriyel(n-1)
#         n=1
#     return sonuc
# n=int(input("n:"))
# sonuc=faktöriyel(n)
# print(sonuc)



#listede verılen degerlerın toplamını ozyıneleme ile hesaplayan program kodu
# def liste_topla(liste):
#     if len(liste)==0:
#         sonuc=0
#     else:
#         sonuc=liste[0]+liste_topla(liste[1:])
#     return sonuc
# liste=[12,32,34,21,43,56,65]
# sonuc=liste_topla(liste)
# print(sonuc)


# verılen bır metındekı buyuk harf sayısını ozyıneleme ıle bulan program kodu
# def buyuk_harf_sayısı(cumle, s=0):
#     if len(cumle)>0:
#         ilk=cumle[0]
#         if ord(ilk)>=65 and ord(ilk)<=90:
#             return buyuk_harf_sayısı(cumle[1:],s+1)
#         else:
#             return buyuk_harf_sayısı(cumle[1:],s)
#     else:
#         return s
# cumle="evet arkaDASLAR BUGUN OZYINELEME İLE İLGILI ornekler cozuCEGIZ."
# buyuk_harf=buyuk_harf_sayısı(cumle)
# print(buyuk_harf)


#verılen sayının ussunu ozyıneleme kullanarak alan program  kodu
# def us_alma(taban,us):
#     if us==0:
#         return 1
#     elif us>0:
#         return taban*us_alma(taban,us-1)
#     else:
#         return 1 /(taban*us_alma(taban,-us))
# taban=int(input("taban="))
# us=int(input("us="))
# print(f"{taban} uzerı {us}:",us_alma(taban,us)) 



# verılen cumeyı  ozyıneleme kullanarak tersten yazdıran program kodu
# def ters_cevır(cumle):
#     if len(cumle)==0:
#         return cumle
#     else: 
#         return ters_cevır(cumle[1:])+ cumle[0]
# cumle="merhaba arkadaslar."
# print("ters cevrılmıs cumle:", ters_cevır(cumle))



#ıkı sayının ebob unu bulan program kodu
# def gcd(x,y):
#     if y==0:
#         return x
#     else:
#         return gcd(y,x%y)
# x=int(input("x="))
# y=int(input("y="))
# print(f"{x} ve {y} sayılarının ebobu:{gcd(x,y)}")


#uc basamaklı rakamları bırbırınden faklı dogal sayıları lısteleyen program kodu
# def üc_basamaklı_sayı():
#     liste=[]
#     for i in range(100,1000):
#         son=i%10
#         orta=(i//10)%10
#         bas=(i//100)%10
#         if (bas!=orta) and (bas!=son) and (orta!=son):
#             liste.append(i)
#     return liste
# liste=üc_basamaklı_sayı()
# liste=üc_basamaklı_sayı()
# print("sayılar:",üc_basamaklı_sayı())


# def esıkleme(matrıs,esık):
#     yenı_matrıs=[]
#     for i in range (len(matrıs)):
#         satır=[]
#         for  j in range(len(matrıs[0])):
#             if matrıs[i][j]>=esık:
#                 satır.append(1)
#             else:
#                 satır.append(0)
#         yenı_matrıs.append(satır)
#     return yenı_matrıs
# matrix = [
#     [10, 5, 3],
#     [2, 8, 15],
#     [20, 6, 12]]
# esık= 8
# yenı_matrıs = esıkleme(matrix, esık)

# print("yenı matrısn:",esıkleme(matrix, esık))



# verılen sayılar bırbırıne tam bolunurmu onu veren program kodu
# def sayı_tam_bolen(x,y):
#     if x%y==0:
#         return True
#     else:
#         return False
# x=int(input("x="))
# y=int(input("y="))
# print(sayı_tam_bolen(x,y))

##1##  dikdörtgenin alanını ve cevresini hesaplayan program kodu
#   kısakenar= int(input("kısa kenarı gırınız:"))
#   uzunkenar= int(input("uzun kenarı gırınız:"))
#   çevre= (uzunkenar+kısakenar)*2
#   alan= uzunkenar*kısakenar
#   print("çevre:",çevre)
#   print("alan:",alan)


##2##Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran kod
#sayı=int(input("üç basamaklı bır sayı gırınız"))
#birler= sayı%10
#onlar= (sayı//10)%10
#yüzler= sayı//100
#print("birler:",birler , "onlar:",onlar ,"yü zler:",yüzler)


##3##Yarıçapı verilen çemberin alanını hesaplayan program kodu
#yarıcap=int(input("lütfen yarıçapı giriniz"))
#alan=(yarıcap**2)*3.14
# print("alan:",(yarıcap**2)*3.14)


##4##Girilen gün sayısını kaç yıl ve kaç ay olduğunu bulan program kodu
#günsayısı=int(input("lütfen gün sayısını gırınız:"))
#ay= günsayısı//30
#yıl= günsayısı//365
#print("ay:",ay  ,"yıl:",yıl)


##5##100'lük sistemde notu girilen öğrencinin notunu 5'lik sisteme cevıren kod
#puan=int(input("lütfen ögrencının puanını gırınız:"))
#if 0<=puan<50 :
#    print("ögrencının puanı 1")
#if 50<=puan<59 :
#    print("ögrencının puanı 2")
#if 59<=puan<69 :
#    print("ögrencının puanı 3")
#if 69<=puan<84 :
#    print("ögrencının puanı 4")
#if 84<=puan<=100 :
#    print("ögrencının puanı 5")


##6##Bir ürünün alış fiyatı, vergi ve kâr oranlarını kullanılarak satış fiyatını hesaplayan program kodu.
#alışfiyatı= int(input("lütfen ürünün alış fiyatını giriniz:"))
#vergi=(alışfiyatı*10)/100
#kar=(alışfiyatı*35)/100
#ürünfıyatı= alışfiyatı + (alışfiyatı*10)/100 + (alışfiyatı*35)/100
#print("ürünfiyatı:", alışfiyatı + (alışfiyatı*10)/100 + (alışfiyatı*35)/100)


##7##Kullanıcının girdiği bir sayının hem 2'ye hemde 3'e bölünebilme durumunu kontrol eden program kodu
#sayı=int(input("lutfen bır sayı gırınız:"))
#if sayı%2 == 0 and sayı%3 == 0:
#    print("sayı 2 ve 3 e tam bolunuyor")
#if sayı%2 == 0 and sayı%3 != 0:
#    print("sayı yanlız 2 ıle tam bolunuyor")
#if sayı%2 != 0 and sayı%3 == 0:
#    print("sayı yanlız 3 ıle tam bolunuyor")
#if sayı%2 != 0 and sayı%3 != 0:
#    print("sayı 2 ve 3 e bolunmuyor")


##8##kredı kartıalısverısnde kazanılan hedıye puan parayı hesaplayan program kodu
#tutar=int(input("lütfen alısverıs tutarını gırınız:"))
#if tutar>=2000:
#    print("100 TL para puan kazandınız")
#if  1000<=tutar<2000:
#    print("50 TLpara puan kazandınız")
#if  tutar<1000:
#    print("10TL para puan kazandınız")


##9##kargonun uzretlı veya uzretsız oldugunu hesaplayan program kodu
#tutar=int(input("lütfen alısverıs tutarını gırınız"))
#if tutar<=50:
#    ücret=tutar+7
#    print("ücret:", tutar+7 )
#if tutar>50:
#    ücret=tutar
#    print("ücret:",tutar)


##10## boy kılo endeksını hesaplayan program kodu
#cinsiyet= str(input("lütfen cinsiyetinizi giriniz:"))
#kilo= int(input("lutfen kilonuzu gırınız:"))
#boy= int(input("lutfen boyunuzu gırınız:"))
#if   18.5<= kilo/boy**2 <= 24.9 :
#    print("ideal kilodasınız")
#else:
#    print("ideal kilodasınız")

##11##harcama tutarına gore ındırım uygulayan program kodu
#tutar=int(input("lütfen alısverıs tutarını gırınız:"))
#if tutar<=200:
#    ücret= (tutar*90)/100
#    print("ücret:",(tutar*90)/100)
#if 200<tutar<=400:
#    ücret=(tutar*85)/100
#    print("ücret:",(tutar*85)/100)
#if tutar>400:
#    ücret=(tutar*80)/100
#    print("ücret:",(tutar*80)/100)


##12##girilen ay bilgısıne gore kuzey y.k. yasanılan mevsımı yazdıran purogram kodu 
#ay= (input("lüften oldugunuz ayı yazıız:"))
#yaz_ayları=["haziran" , "temmuz", "agastos"] 
#kış_ayları=["ocak" , "şubat" , "aralık"]
#sonbahar_ayları= ["eylül" , "ekim" , "kasım"]
#ilkbahar_ayları=  ["mart" , "nisan" , "mayıs" ]
#if ay in ilkbahar_ayları :
#    print("kuzey yarım kurede ilkbahar yasanmakta:")
#if ay in yaz_ayları :
#     print("kuzey yarım kurede yaz yasanmakta:")
#if ay in kış_ayları :
#    print("kuzey yarım kurede kış yasanmakta:")
#if ay in sonbahar_ayları :
#    print("kuzey yarım kurede kış yasanmakta:")


##13## 3 sayı arasında en küçük cift sayıyı bulan program kodu
#sayı1=int(input("lütfen bir sayı1 giriniz:"))
#sayı2=int(input("lütfen bir sayı2 giriniz:"))
#sayı3=int(input("lütfen bir sayı3 giriniz:"))  
#en_küçük_sayı = min(sayı1, sayı2, sayı3)
#print("en_küçük_sayı:", en_küçük_sayı)
    
    
##14## gırılen 3 basamaklı sayıyı tersıne cevıren program kodu
#sayı= int(input("lütfen 3 basamaklı bır sayı gırınız:"))
#a= sayı//100
#b=(sayı//10)%10
#c=(sayı%10)*100
#yenisayı=a+(b*10)+c
#print("yenisayı:",a+(b*10)+c)


##15##Girilen n ve k değerlerine göre k + 2k + 3k + ...+nk yı hesaplayan program?    
# k=int(input("lutfen bır k degerı grınız:"))
# n=int(input("lutfen bır n degerıgırınız:"))
# for i in range(1,n+1):
#     toplam = i*k
#     print("toplam:", i*k)


##16##Çizginin başlangıç ve orta nokta koordinatları veriliyor. Diğer uç noktanın koordinatlarını bulunuz?
# x=int(input("x="))
# y=int(input("y="))
# x1=int(input("x1="))
# y1=int(input("y1="))
# başlangıc_kordinatı=(x,y)
# orta_nokta=(x1,y1)
# a=2*x1-x
# b=2*y1-y
# bitiş_kordinatı=(a,b)
# print("bitiş_kordinatı=",(a,b))


# #17##Girilen sayının pozitif ya da negatif olduğunu ekrana yazınız?
# sayı= int(input("lütfen bır sayı grınız:"))
# if sayı<0:
#    print("sayı negatif:")
# elif sayı>0:
#    print("sayı pozitif")
# else:
#    print("sayı nötr")



##18##Vize ve Final notu girilen öğrencinin geçip geçmediğini hesaplayan program kodu
#vize= int(input("lütfen ögrencının vıze notunu giriniz:"))
#final=int(input("lütfen ögrencının final notunu giriniz:"))
#ortalama= (vize*40)/100 + (final*60)/100
#if final<60 and ortalama>=55 :
#    print("ögrenci dersten gecememistir bütünlemeye kalmıştır.")
#if final<60 and ortalama<55:
#    print("ögrenci dersten gecememistir bütünlemeye kalmıştır.")
#if ortalama<55:
#    print("ögrenci dersten gecememistir bütünlemeye kalmıştır.")
#if ortalama>=55 and final>60 :
#    print("örencı derten gecmıstır.")



##19##Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?
#sayı1=int(input("lütfen bir sayı1 giriniz:"))
#sayı2=int(input("lütfen bir sayı2 giriniz:"))
#sayı3=int(input("lütfen bir sayı3 giriniz:"))
#en_büyük_sayı=max(sayı1, sayı2, sayı3)
#print("en_büyük_sayı:", en_büyük_sayı)


##20##Girilen sayının 6'nın katı olduğunu bulan program?
#sayı=int(input(" lütfen bir sayı grınız:"))
#if sayı%2==0 and sayı%3==0 :
#    print("sayı 6 ile tam bölünebilmekte.")
#elif sayı%2==0 and sayı%3!=0 :
#    print("sayı 2ile tam bölünebilmekte ancak 6 ile bölünememekte.")
#elif sayı%2!=0 and sayı%3!=0 :
#    print("sayı 6 ile tam bölünememekte")
#elif sayı%2!=0 and sayı%3==0 :
#    print("sayı 6 ile tam bölünememekte.")
    
    
    

##21##Yüzlük notu harf notuna çeviriniz?
#puan= int(input("lütfen öğrencinin notunu giriniz:"))
#if 0<=puan<59:
#    print("örenci notu AA.")
#if 59<=puan<69:
#    print("örenci notu BA.")
#if 69<=puan<85:
#    print("örenci notu BB.")
#if 85<=puan<=100:
#    print("örenci notu CA.")





##22##İşçi maaşı ve çocuk sayısına gore maas hesaplam
#çocuk_sayısı=int(input("lütfen cocuk sayısını gırınız:"))
#işçi_maaşı=int(input("lütfen işçi maaşını gırınız:"))
#if çocuk_sayısı==1:
#    maaş=(işçi_maaşı*105)/100
#    print("maaş:",(işçi_maaşı*105)/100)
#if çocuk_sayısı==2:
#    maaş=(işçi_maaşı*110)/100
#    print("maaş:",(işçi_maaşı*110)/100)
#if çocuk_sayısı>2:
#    maaş=(işçi_maaşı*115)/100
#    print("maaş:",(işçi_maaşı*115)/100)
    
    
    
##23##Ekrana 1:Toplama, 2:Çıkarma,..yaz. Sonra kullanıcıdan iki sayı alıp işlemi seçerek sonucu ekranda yazan program?
#print("İŞLEMLER /n 1:Toplama/n2:Çıkartma/n3:Çarpma/n4:Bölme")
#c=int(input("birinci sayıyı gırınız:"))
#b=int(input("ikinci sayıyı gırınız:"))
#a=int(input("yapmak istediginiz işlemi seciniz:"))
#if (a==1) :
#    print("Toplama sonucu:", c+b)
#elif (a==2) :
#    print("Çıkatma sonucu:",c-b)
#elif (a==3) :
#    print("Çarpma sonucu:",c*b)
#elif (a==4) :
#    print("Bölme sonucu:",c/b)
#else:
#    print("hatalı secim /n iyi günler")



###24###Çizgi daireyi kesiyor mu, yoksa teğet mi sonucunu bulan program? 
#a=int(input("lutfen a degerı gırınız:"))
#b=int(input("lutfen b degerını gırınız:"))
#c=int(input("lutfen c degerı gırınız:"))
#dx=int(input("lutfen dx degerı gırınız:"))
#dy=int(input("lutfen dy degerı gırınız:"))
#r=int(input("lutfen r degerı gırınız:"))
#d=abs(a*dx+b*dy+c) / (1/2*(a**2+b**2))
#if (d==r):
#    print("teget")
#elif (d>r):
#    print(" kesmez")
#else :
#    print("keser")



###25###1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünenlerı yenı bır lıstey ekleyen program kodu
#for i in range (1,101):
#    if i%3==0 and i%5==0:
#        print(i)



###26###Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodu.
#toplam_çift = 0
#toplam_tek = 0
#sayı = int(input("lütfen bir  sayı girıniz:"))

#for i in range(1,sayı+1):
#    if i % 2 == 0:
#        toplam_çift += i
#    else:
#        toplam_tek+=i
#        
#print(f"1 den {sayı}'e kadar olan tek sayıların toplamı:",toplam_tek)
#print(f"1 den {sayı}'e kadar olan çiftsayıların toplamı:",toplam_çift)
        

###27## 20'ye kadar olan sayıları, 10'dan küçük ve 10'dan büyük şeklinde lıstelıcek program kodu
#for sayı in range(1,21):
#    if sayı<10:
#        print(f"{sayı} - 10'dan küçük ")
#    if sayı>10:
#        print(f"{sayı} - 10'dan büyük ")



###28###Kullanıcıdan alınan 5 sayı içerisinden for döngüsü kullanarak en küçük sayıyı bulan programı kodlayınız.
#sayılar=[]
#for i in range(5):
#    sayı=float(input(f"{i+1}.sayıları giriniz:"))
#    sayılar.append(sayı)
#    
#en_küçük_sayı= sayılar[0]
#for sayı in sayılar:
#    if sayı<en_küçük_sayı:
#        en_küçük_sayı=sayı
#        
#print(f"en küçük sayı:{en_küçük_sayı}")



###29###Bir for döngüsü kullanarak Fibonacci dizisinin ilk 20 terimini hesaplayan program kodu:
#a,b=0,1
#for _ in range(1,21):
#    print(a,end=" ")
#    a,b=b,a+b



###30##1 den 10′ a kadar sayıları tersten yani 10′ dan geriye yazdırın.
#for i in range(10,0,-1):
#    print(i)



###31###
#for  x in range(10):
#    print(x," ",2*x+2)


###32###Girilen 5 sayının ortalamasını bulan program?
#sayılar=[]#
#for _  in range(5):
#    sayı=float(input("sayıları giriniz:"))#
#    sayılar.append(sayı#)

#ortalama= sum(sayılar)/len(sayılar)
#print(f"girilen sayıların ortalaması:{ortalama}")



###33###Girilen sayının tam bölenlerini bulan program?
#N=int(input("N="))
#for a in range(1,N+1):
#    if N%a==0:
#        print(a)


###34### N’e kadar tek sayıları yazdıran program kodu
#N=int(input("N="))
#for a in range(1,N+1):
#    if a%2==1 :
#        print(a)



###35###  a ussu b yi açık hesaplayan program?
#a=int(input("a="))
#b=int(input("b="))
#üs_işlemi=a**b
#print("üs_işlemi:",a**b)



###36### n’e kadar ki tek sayıların toplamı, çift sayıların çarpımını hesaplayan program?
#toplam_tek=0
#carpım=1
#N=int(input("N="))
#for a in range(1,N+1):
#    if a%2==1:
#        toplam_tek += a
#    if a%2==0:
#        carpım *= a
    
#print(f"1 den {N}'e kadar olan tek sayıların toplamı:",toplam_tek)
#print(f"1 den {N}'e kadar olan çift sayıların carpımı:", carpım)


##37###Girilen sayının faktöriyelini hesaplayan program?
#cozum1
#fak=1
#N=int(input("N="))
#for a in range(N,0,-1):
#    fak=fak*a
#    
#print("faktöriyel:",fak*a)
##cozum2=
# sayı=int(input("lutfen faktorıyelını hesaplamak ıstedıgınız sayıyı gırınız="))
# sonuc=1

# while sayı>0 :
#     sonuc= sonuc*sayı
#     sayı -= 1
    
# print(sonuc)




##38## A, B ve C değerlerinin 0-1 aralığında olduğunu bulan program kodu ?
#A=float(input("A="))
#B=float(input("B="))
#C=float(input("C="))
#if (A>0  and A<1  and B>0  and B<1  and C>0 and C<1):
#	print("nokta üçgenin içinde")
#else :
#	print("nokta üçgenin dışında")


###39### Girilen 5 sayının ortalamasını bulan program?
#top=0
#for i in range(5):
#    x=int(input("sayı gir:"))
#    top=top+x 
#ort=top/5
#print("ort:",top/5)


###40## Girilen n değerine göre Fibonacci serisini hesaplayan program kodu:
#n=int(input("fibonacci serisi icin bır n degerı gırınız:"))
#
#a,b=0,1
#for _ in range(n):
#    print(a, end=" ")
#    a,b = b,a+b

###41### Serinin ilk elemanı, toplam eleman sayısını ve artış değeri girildiğinde seri sonucunu hesaplayan program?
#ilk= int(input("ilk eleman:"))
#topS=int(input("toplam eleman sayısı:"))
#artışD=int(input("artış degeri:"))

#toplam=0
#sayı=ilk
#for _ in range(topS):
#    toplam+=sayı
#    sayı+=artışD
#    
#print("toplam:",toplam)



###42## Girilen bir sayının asal olup olmadığını bulunuz?
# N=int(input("N="))
# asal=True # burada asalı true kabul ettık 

# for a in range(2,N):
#     if N%a == 0:
#         asal=False
#         print(f"{N} sayı asal degıl.")
#         break
    
# if asal:
#     print(f"{N} sayı asal.")


##43## Girilen bir sayının asal çarpanlarını bulan program?
# sayı=int(input("lütfen asal carpanlarınıhesaplamak ıstedıgnız sayıyı gırınız="))
# carpan=2

# while carpan<=sayı:
#     if sayı %carpan==0:
#         print(carpan,end=" ")
#         sayı//=carpan
#     else :
#         carpan+=1



###44### Girilen sayının basamak değerleri çarpımını bulunuz?
# sayı=int(input("3 basamkalı bır sayı gırınız ="))
# a=sayı%10
# b=(sayı//10)%10
# c=sayı//100
# carpım=a*b*c
# print("carpım=",a*b*c)

 #verılen bır sayının karesını hesaplayan program kodu
# sayı=int(input("lütfen karesını hesaplamak ıstedıgınız sayıyı gırınız="))
# kare=sayı**2
# print("karesi=", sayı**2)

# verılen x degerıne gore y degıskenını hesaplayan program kodu
# x=int(input("lütfen x degerını gırınız="))
# y=(3*x)**2
# print("y degeri:",(3*x)**2)

#verılen 3 sayınınn ortalamasını bulan program Kodu
# top=0
# for i in range(3):
#     x=int(input("sayı gır="))
#     top=top+x
# ort=top/3
# print("ort=",top/3)

#  verılen a ve b  tamsayı degıskenlerını yer degıstıren program kodu
# a=int(input("a degerını gırınız="))
# b=int(input("b degerınnı gırınız="))
# temp=a    # buradakı temp komutu verılen degıskenlerın degerını takas etmek ıcın kullanılır 
# a=b
# b=temp
# print("a nın yenı degerı=",a, "b nin yenı degerı=",b)

#girilen sayının pozıtıf  yada negatıf oldugunu ekrana yazdıran program kodu
# sayı=int(input("sayı="))
# if sayı<0:
#     print("girilen sayı negetif degerlıdır.")
# elif sayı>0:
#     print("girilen sayı pozıtıf degerlıdır.")
# else:
#     print("gırılen sayı nötürdür." )

#girilen 3 sayı arasında en kucuk sayıyı bulan program kodu
# sayı1=float(input("sayı1="))
# sayı2=float(input("sayı2="))
# sayı3=float(input("sayı3="))

# en_kucuk_sayı=sayı1

# if sayı2 < en_kucuk_sayı:
#     en_kucuk_sayı=sayı2
#     print("en_kucuk_sayı:",en_kucuk_sayı)
#     if sayı3<en_kucuk_sayı:
#         en_kucuk_sayı=sayı3
#         print("en_kucuk_sayı:",en_kucuk_sayı)

#verılen lıstedekı en kucuk sayıyı bulan program kodu 
# liste=[1,2,222,33,21,5,6,7,888,99,55,46,98,76]
# en_kucuk_sayı=liste[0]
# for sayı in liste:
#     if sayı<en_kucuk_sayı:
#         en_kucuk_sayı=sayı
        
# print("listenın en kucuk sayısı:", en_kucuk_sayı)

# sayı1=float(input("sayı1="))
# sayı2=float(input("sayı2="))
# sayı3=float(input("sayı3="))
# sayı4=float(input("sayı4="))
# ort=(sayı1+sayı2+sayı3+sayı4)/4

# liste=[sayı1,sayı2,sayı3,sayı4]

# for i in liste:
#     if i>ort:
#         print(i)

#klavyede gırılın karakterın harf sayı gıbı turunu blırleyen program kodu
# karakter=input("karakterı gırınız =")
# if karakter.isalpha():  ###isalpha ascll de harfleri temsıl etmektedır 
#     print("gırılen karakter bır harftır.")
# elif karakter.isdigit(): ###isdigit ascll de rakamları temsıl etmektedir
#     print("gırılen karakter bır rakamdır.")
# else:
#     print("girilen karakter özel bir karakterdir")

#isminızı 5 defa yazdıran program kodu 
# isim=str(input("lütfen isminizi giriniz="))
# isim5=isim*5
# print(isim5)

#verılen ıkı sayı arasında kalan sayıları yazdıran program kodu
# sayı1=int(input("lutfen sayı1 gırınız="))
# sayı2=int(input("lutfen sayı2 gırınız="))

# kucuk_sayı=min(sayı1,sayı2)
# buyuk_sayı=max(sayı1,sayı2)

# print(f"{kucuk_sayı} ile {buyuk_sayı} arasındakı sayılar")

# for sayı in range(kucuk_sayı+1,buyuk_sayı):
#     print(sayı , end=" ") 

#1 den 10 akadar olan sayıların toplamıı bulan program kodu 
# top=0
# for i in range (1,11,1):
#     top = top+i

# print("top=",top+i)

#gırılen sayıyı tersten yazdıran program kodu:
# sayı=int(input("tersten yazdırmak ıstedıgınız sayıyı gırınız="))
# a=(sayı%10)*100
# b=((sayı//10)%10)*10
# c=(sayı//100)
# sayı1=a+b+c
# print("sayı1:",a+b+c)

# verılen sayının palindrom sayı olup olmadıgını konrtol eden program kodu
# sayı=int(input("sayıyı gırınız="))
# a=(sayı%10)*100
# b=((sayı//10)%10)*10
# c=(sayı//100)
# sayı1=a+b+c
# if sayı==sayı1:
#     print("girmiş oldugunuz sayı palindrom sayıdır.")
# else:
#     print("girmiş oldugunuz sayı palindrom sayı degildır.")
    
    
# verilen bır metındekı buyuk harflerı kuculten ve bosluk yerıne _ koyan program kodu 
# def düzenle(metin):
#     düzenlenmiş_metin=""
#     for karakter in metin: 
#         if karakter.isupper(): # isupper buyuk harf demek
#             düzenlenmiş_metin+=karakter.lower()  #lower küçük harf demek 
#         elif karakter== ' ':
#             düzenlenmiş_metin+='_' 
#         else:
#             düzenlenmiş_metin+=karakter
#     return düzenlenmiş_metin

# metin="PROGramlama BÜtÜne hazırlık calısması"

# düzenlenmiş_metin=düzenle(metin)

# print("düzenlenmiş_metin:",düzenlenmiş_metin)


# def yazdır(kelıme,adet):
#     print(kelıme*adet)
    
# yazdır('merhaba/n' , 10)

#ıkı sayı arasındakı asalları bulan proram kodu 
# def asal_bul(sayı1,sayı2):
#     for sayı in range(sayı1,sayı2+1):
#         if sayı>1:
#             for i in range(2,sayı):
#                 if sayı%i==0:
#                     break
#             else:
#                 print(sayı)
                    
# sayı1=int(input("sayı1="))
# sayı2=int(input("sayı2="))

# asal_bul(sayı1,sayı2)

# def tam_bolen(sayı):
#     tam_bolenler=[]
#     for i in range(2,sayı):
#         if sayı%i==0:
#             tam_bolenler.append(i)
        
#     return tam_bolenler

# tam_bolen(20)
# print(tam_bolen(20))


# def faktorıyel(sayı):
#     if sayı==1 or sayı==0:
#         return 1
#     else:
#         return sayı*faktorıyel(sayı-1)
    
# print(faktorıyel(6))


