#Rendra Rizki Kurniawan
#L200170027

#Nomor 1
import re
f=open('Indonesia.txt','r', encoding='latin1')
teks = f.read()
f.close()
p=r'me\w+'
string = re.findall(p,teks)
print(string)

    
#Nomor 2
import re
f=open('Indonesia.txt','r', encoding='latin1')
teks2 = f.read()
f.close()
pola2 = r"di\w+"
tampilan2 = re.findall(pola2,teks2)
print(tampilan2)

    
#Nomor 3
import re
f=open('Indonesia.txt','r', encoding='latin1')
teks3 = f.read()
f.close()
pola3 = r"di \w+"
tampilan3 = re.findall(pola3,teks3)
print(tampilan3)

#Nomor 4a
import re
f=open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
p4=r'([\w+]+)</a></td>'
string=re.findall(p4,teks4)
print(string)

#Nomor 4b
f=open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
string=re.findall(r'title="([\w+]+)">',teks4)
string=re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks4)
a=[]
for i in string:
    a.append((i[0], float(i[1])))
print(a)

#INDONESIA
#Republik Indonesia (RI) atau Negara Kesatuan Republik Indonesia (NKRI), atau lebih umum disebut Indonesia, adalah negara di Asia Tenggara yang dilintasi garis khatulistiwa dan berada di antara daratan benua Asia dan Australia, serta antara Samudra Pasifik dan Samudra Hindia. Indonesia adalah negara kepulauan terbesar di dunia yang terdiri dari 17.504 pulau.[11] Nama alternatif yang biasa dipakai adalah Nusantara.[12] Dengan populasi Hampir 270.054.853 jiwa pada tahun 2018,[13] Indonesia adalah negara berpenduduk terbesar keempat di dunia dan negara yang berpenduduk Muslim terbesar di dunia, dengan lebih dari 230 juta jiwa.[14][15]

#Bentuk negara Indonesia adalah negara kesatuan dan bentuk pemerintahan Indonesia adalah republik, dengan Dewan Perwakilan Rakyat, Dewan Perwakilan Daerah dan Presiden yang dipilih secara langsung.

#Ibu kota negara Indonesia adalah Jakarta. Indonesia berbatasan darat dengan Malaysia di Pulau Kalimantan, dengan Papua Nugini di Pulau Papua dan dengan Timor Leste di Pulau Timor. Negara tetangga lainnya adalah Singapura, Filipina, Australia, dan wilayah persatuan Kepulauan Andaman dan Nikobar di India.

#Sejarah Indonesia banyak dipengaruhi oleh bangsa lainnya. Kepulauan Indonesia menjadi wilayah perdagangan penting sejak abad ke-7, yaitu sejak berdirinya Kerajaan Sriwijaya, sebuah kemaharajaan Hindu-Buddha yang berpusat di Palembang. Kerajaan Sriwijaya ini menjalin hubungan agama dan perdagangan dengan Tiongkok dan India, juga dengan bangsa Arab. Kerajaan-kerajaan beragama Hindu dan/atau Buddha mulai tumbuh pada awal abad ke-4 hingga abad ke-13 Masehi, diikuti para pedagang dan ulama dari jazirah Arab yang membawa agama Islam sekitar abad ke-8 hingga abad ke-16, serta kedatangan bangsa Eropa pada akhir abad ke-15 yang saling bertempur untuk memonopoli perdagangan rempah-rempah Maluku semasa era penjelajahan samudra. Setelah berada di bawah penjajahan Belanda selama hampir 3 abad, Indonesia yang saat itu bernama Hindia Belanda menyatakan kemerdekaannya di akhir Perang Dunia II, tepatnya tanggal 17 Agustus 1945. Selanjutnya, Indonesia mendapat berbagai tantangan dan persoalan berat, mulai dari seringnya terjadi bencana alam, praktik korupsi yang masif, konflik sosial, gerakan separatisme, proses demokratisasi, dan periode pembangunan, perubahan dan perkembangan sosial-ekonomi-politik, serta modernisasi yang pesat.

#Dari Sabang di ujung Aceh sampai Merauke di tanah Papua, Indonesia terdiri dari berbagai suku bangsa, bahasa, dan agama. Berdasarkan rumpun bangsa (ras), Indonesia terdiri atas bangsa asli pribumi yakni Mongoloid Selatan/Austronesia dan Melanesia di mana bangsa Austronesia yang terbesar jumlahnya dan lebih banyak mendiami Indonesia bagian barat. Secara lebih spesifik, suku bangsa Jawa adalah suku bangsa terbesar dengan populasi mencapai 41,7% dari seluruh penduduk Indonesia.[16] Semboyan nasional Indonesia, "Bhinneka tunggal ika" ("Berbeda-beda namun tetap satu"), bermakna keberagaman sosial-budaya yang membentuk satu kesatuan/negara. Selain memiliki populasi penduduk yang padat dan wilayah yang luas, Indonesia memiliki wilayah alam yang mendukung tingkat keanekaragaman hayati terbesar kedua di dunia.

#Indonesia merupakan anggota dari PBB dan satu-satunya anggota yang pernah keluar dari PBB, yaitu pada tanggal 7 Januari 1965, dan bergabung kembali pada tanggal 28 September 1966 dan Indonesia tetap dinyatakan sebagai anggota yang ke-60, keanggotaan yang sama sejak bergabungnya Indonesia pada tanggal 28 September 1950. Selain PBB, Indonesia juga negara anggota dari organisasi ASEAN, KAA, APEC, OKI, G-20 dan sebentar lagi akan menjadi anggota OECD. 
#wamena
