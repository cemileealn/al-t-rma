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



























    











        




    
































        
        















    
    
    
    
    
    
    
    
    
    
    
    
    
    







            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
       
        
    










        











