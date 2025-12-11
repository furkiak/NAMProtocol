# D.A.H.A. / N.A.M. Protokolü
**Doğal Aritmetik Haritalama Algoritması — Natural Arithmetic Mapping** 

**Kategori:** MRM — Mathematical Reversible Mapping

**Version:** 0.0.1 (Concept / Experimental)  

## 👨‍💻 Author / Yazar
**Furkan AKÇA** *Creator & Lead Researcher* Project Started: December 2025

**Collaborator:** Gemini AI (Concept Validation & Documentation)

## 📄 License
This project is licensed under the MIT License.
Copyright (c) 2025 Furkan AKÇA.

**Disclaimer / Sorumluluk Reddi:** This protocol is experimental. Use at your own risk for critical data. / Bu protokol deneyseldir. Kritik verilerinizde kullanırken dikkatli olun.

---

## 📌 1. Protokol Hakkında

**D.A.H.A. Protokolü** (Doğal Aritmetik Haritalama Algoritması); dosyaları şifrelemek, gizlemek, kimliksizleştirmek ve matematiksel olarak yok edilebilir hâle getirmek için geliştirilmiş yeni nesil bir veri dönüşüm sistemidir.

Klasik kriptografideki blok/bayt odaklı mimarilerin aksine **D.A.H.A.**, tüm dosyayı:
1.  **Tek ve devasa bir doğal sayı** olarak işler.
2.  Dosya bu işlem sonucunda iki bileşene ayrılır:
    * **MAP:** Matematiksel Ofset Adım Dizisi
    * **DEPTH:** Uygulanan toplam adım sayısı (maskeleme uygulanmış)

> ⚠️ **Not:** MAP + DEPTH olmadan orijinal dosyaya erişmek matematiksel olarak imkânsızdır.

---

## 📌 2. Matematiksel Çalışma Prensibi

Algoritmanın temel çalışma akışı şu şekildedir:

1.  Dosyanın ham bit karşılığı alınır.
2.  Bit dizisi tek bir büyük doğal sayı (**BigInt**) gibi ele alınır.
3.  Eğer doğal sayı **tek** ise sonuna "0" eklenerek **çift** yapılır.
4.  Süreç başlar:
    * **Çift ise:** 2’ye böl.
    * **Tek ise:**
        * Dinamik OFFSET pattern’e göre `+5` veya `–5` uygula.
        * Ardından 2’ye böl.
        * Bu adım **MAP**’e eklenir.
5.  Sayı `0` olana kadar devam eder.
6.  Tüm adımların toplamı → **RealDepth**

Sonuç olarak; **MAP + MaskedDepth + OFFSET** dizisi ile süreç ters yönlü çalıştırılarak orijinal dosya matematiksel olarak yeniden elde edilir.

---

## 🔍 Örnek Çalışma

Basit örnek (sabit +5/–5) üzerinden işleyiş:

* **Girdi (Bit Dizisi):** `1010`
* **Hazırlık:** Sonu `0` → direkt işlemler başlar.

| Adım | İşlem | Durum | MAP Kaydı |
| :---: | :--- | :--- | :--- |
| **1** | $1010 / 2 = 505$ | Tek | - |
| **2** | $505 \to \pm5 \to 250$ | Çift (İşlem sonrası) | **MAP: 2** |
| **3** | $250 / 2 = 125$ | Tek | - |
| **4** | $125 \to \pm5 \to 60$ | Çift (İşlem sonrası) | **MAP: 2, 4** |
| **5** | $60 / 2 = 30$ | Çift | - |
| **6** | $30 / 2 = 15$ | Tek | - |
| **7** | $15 \to \pm5 \to 5$ | Çift (İşlem sonrası) | **MAP: 2, 4, 7** |
| **8** | $5 \to \pm5 \to 0$ | Bitiş | **MAP: 2, 4, 7, 8** |

**Sonuç Çıktısı:**
* **DEPTH:** 8
* **MAP:** `[2, 4, 7, 8]`

> *MAP + DEPTH → ters çalıştırıldığında bit dizisi eksiksiz geri elde edilir.*

## 🛡️ 3. Güvenlik ve Optimizasyon Katmanları

Sistem, verimliliği artırmak ve veri bütünlüğünü korumak adına üç aşamalı bir katman mimarisi kullanır.

### 🔹 Optimizasyon-1: MAP Delta Compression
MAP dizisi, dosya boyutu büyüdükçe çok büyük sayı indeksleri içerebilir. Bu veriyi ham haliyle saklamak yerine **Delta (Fark)** yöntemi uygulanır:
* Sıra numaraları yerine, bir önceki sayı ile olan **farklar (delta)** saklanır.
* Bu sayede MAP boyutu ciddi düzeyde azaltılır.
* Daha küçük sayılarla çalışıldığı için sıkıştırma algoritmalarının verimliliği artar.

### 🔹 Optimizasyon-2: MAP Compression
Delta dönüşümü sonrası elde edilen MAP dizisi, matematiksel olarak yüksek oranda tekrarlı veya tahmin edilebilir bir yapıya bürünür. Bu dizi aşağıdaki yöntemlerle orijinal dosyadan çok daha küçük boyutlara indirilir:
* `Gzip`
* `Brotli`
* `Arithmetic Coding`
* *Veya özel geliştirilmiş compressor algoritmaları.*

### 🔐 Optimizasyon-3: Integrity Hash (Bütünlük Kontrolü)
İşlem tamamlandığında, tüm veri yapısının (**HEADER + BODY**) kriptografik özeti alınır.
* **Algoritmalar:** `SHA-256` veya `SHA3-512` kullanılır.

**Geri dönüş işleminde Hash uyuşmazlığı yaşanırsa, bu durum şu hatalardan birine işaret eder:**
1.  Yanlış **Salt** kullanımı.
2.  Bozuk veya değiştirilmiş **MAP** verisi.
3.  Hatalı **Depth Maskesi**.
4.  Yanlış **Offset Listesi**.
5.  Eksik veya bozuk **Header** bilgisi.

## 🔑 4. Anahtar Setleri (MRK — Mathematical Reversible Keys)

Protokol, güvenliği katmanlandırmak adına çoklu anahtar mimarisini kullanır.

### 🗝️ Anahtar-1: HEADER MASK
* **Amaç:** Dosya formatı tespitini (Magic Bytes detection) engellemek.
* **Yöntem:** Dosyanın ilk byte’ları (magic header) ana gövdeden ayrılır.
* Bu parça **Şifre-1** olarak saklanır.
* ⚠️ *Geri dönüş işlemi için zorunludur.*

### 🧂 Anahtar-2: SALT (High Entropy Injection)
* **Amaç:** Frekans ve veri analizlerini imkânsız hâle getirmek.
* **Yöntem:** Yüksek entropili bir bit bloğu üretilir. Orijinal bit dizisine rastgele bir konumdan enjekte edilir:
    * Sol baştan toplama
    * Sağ başa toplama
    * Veya belirli bir ofset sonrasına toplama
* **Sonuç:** Enjeksiyon konumu bilinmediği sürece analitik geri mühendislik engellenir.

### 📉 Anahtar-3: OFFSET PATTERN LIST
Sabit `+5` / `–5` işlemleri yerine; anahtar tabanlı, döngüsüz ve tahmin edilemez diziler kullanılır.

Örnek Pattern:
[+5, +5, -5, -5, +5, -5, ...]
### 🎭 Anahtar-4: DEPTH Mask
Toplam adım sayısı (Derinlik) gizlenir.

**Formül:**
MaskedDepth = RealDepth \oplus DepthKey
Ayrıca:
* Dummy (geçersiz) adımlar
* Gürültü derinliği

eklenebilir.

---

## 📌 5. Kriptografik Konumlandırma

**D.A.H.A.**, hiçbir mevcut kategoriye tam olarak oturmadığı için yeni bir sınıf tanımlar:

### 🛡️ MRM — Mathematical Reversible Mapping

Bu sınıf:
* Şifreleme
* Gizleme
* Format kaldırma
* Kimliksizleştirme
* Veri yok etme (geri çağırmalı)
* BigInt matematiği
* Çoklu anahtar modeli
* Oracle saldırılarına kapalı yapı

gibi özellikleri birlikte sunar.

---

## 📌 6. Kullanım Alanları

* 🏛️ Devlet sırrı arşivleme
* 🔐 Yüksek güvenlikli anahtar depolama
* ♻️ Veri yok etme (geri getirilebilir)
* 🛡️ Bilgi savaşı / siber savunma
* ❄️ Cold storage data encryption
* 💾 Donanım tabanlı güvenlik modülleri
* 🔑 Key escrow sistemleri

## 📊 7. Özellik Tablosu

| Özellik | Durum | Açıklama |
| :--- | :---: | :--- |
| Geri dönüşümlü matematiksel dönüşüm | ✔️ | Kayıpsız |
| Çoklu anahtar seti | ✔️ | `HEADER` + `SALT` + `OFFSET` + `DEPTH` |
| Format gizleme | ✔️ | `HEADER MASK` |
| Veri analizi engelleme | ✔️ | `SALT` + `OFFSET` |
| MAP sıkıştırma | ✔️ | Delta + Compression |
| Bütünlük kontrolü | ✔️ | `SHA-256` / `SHA3-512` |
| Oracle saldırı koruması | ✔️ | Sabit ofset yok |
| Donanımsal uygulama | ✔️ | FPGA/ASIC’e uygun |

---

## 🐍 9. Basit Python Demo (Örnek Dosya → MAP → Geri Yükleme)

Aşağıdaki örnekte:

1. "Yeni nesil Şifreleme ve Yok etme algoritması" içeriğine sahip örnek bir metin dosyası oluşturulur.
2. Dosyadan ham bit karşılığı alınır.
3. Hiçbir güvenlik katmanı uygulanmadan `MAP` ve `DEPTH` hesaplanır.
4. `MAP` + `DEPTH` kullanılarak dosya yeniden oluşturulur.

> ⚠️ **Not:** Bu demo yalnızca matematik çekirdeğini göstermek içindir.
>
> Gerçek protokol; `OFFSET LIST`, `HEADER MASK`, `SALT`, `DEPTH MASK`, `HASH`, `DELTA COMPRESSION` vb. içerir.

➡️ `Test.py` dosyasını kullanabilirsiniz.

---

## ⚖️ 10. Teorik Karşılaştırma

### D.A.H.A. vs. Diğer Şifreleme Yöntemleri

Aşağıdaki tablo, **D.A.H.A.**’nın matematiksel yaklaşımını klasik kriptografiye göre konumlandırır.

#### 📊 D.A.H.A. vs AES / RSA / ECC — Kavramsal Farklar

| Özellik / Sistem | AES | RSA | ECC | D.A.H.A. |
| :--- | :--- | :--- | :--- | :--- |
| **Temel Yapı** | Blok şifreleme | Büyük asal matematiği | Eliptik eğri matematiği | Doğal sayı haritalama / BigInt yönlü ters dönüşüm |
| **İşlem Prensibi** | `SubBytes`, `ShiftRows`, `MixColumns` | Modüler üs alma | Eliptik eğri noktaları | 2’ye bölme + ofset uygulama |
| **Veri Boyutu Yaklaşımı** | Blok (128 bit) | Rastgele boyut | Rastgele boyut | Tüm dosya = tek büyük sayı |
| **Format Gizleme** | ❌ | ❌ | ❌ | ✔ `HEADER MASK` |
| **Salt/Noise** | ✔ Var | ✔ Var | ✔ Var | ✔ + rastgele konumlu `SALT` |
| **Geri Dönüş** | Anahtar olmadan mümkün değil | Anahtar olmadan mümkün değil | Anahtar olmadan mümkün değil | Anahtar + `MAP` olmadan matematiksel geri dönüş imkânsız |
| **Oracle Engelleme** | Kısmen | Kısmen | Kısmen | ✔ Tamamen (dinamik offset + dummy steps) |
| **Dosya Yok Etme** | Var | Var | Var | ✔ Matematiksel sıfırlama |
| **Format Kaldırma** | ❌ | ❌ | ❌ | ✔ Dosya → kimliksiz doğal sayı |
| **Şifre-Metin Analizi** | Zayıflık doğabilir | Beklenir | Zor | `SALT` + `OFFSET` + `DELTA` → analiz yapılamaz |
| **Sıkıştırma Uygunluğu** | Veri bağımlı | Veri bağımlı | Veri bağımlı | `MAP` delta + compressor ile yüksek |

---

### 🚀 D.A.H.A.’nın Avantajlı Olduğu Teorik Alanlar

#### ✔ 1. BigInt tabanlı matematiksel yok etme
* **Diğer algoritmalar:** Veriyi şifreler.
* **D.A.H.A.:** Veriyi 0’a indirip yeniden oluşturur.

#### ✔ 2. Çoklu anahtar modeli
* **AES:** Tek anahtar.
* **RSA/ECC:** Tek private key.
* **D.A.H.A.:** `HEADER` + `SALT` + `OFFSET` + `DEPTH` + `HASH`.

#### ✔ 3. Format analizini engeller
* **AES:** Şifrelenmiş çıktı analiz edilebilir.
* **D.A.H.A.:** `header mask` + `salt` ile şunlar çıkarılamaz:
  * Dosya tipi
  * Boyut
  * İçerik paterni

#### ✔ 4. Oracle saldırılarına direnç
* Her adımın ofset işlemi kurala bağlı değildir → **key pattern** tabanlıdır.

### ⚠️ D.A.H.A.’nın Sınırlı Olduğu Teorik Alanlar

#### ❗ 1. Matematiksel maliyet (çok büyük BigInt işlemleri)
* **AES:** Hardware’de çok hızlıdır.
* **D.A.H.A.:** Devasa `BigInt` üzerinde çalışır → **CPU yoğun**.

#### ❗ 2. Standartlaşmamış yapı
* **AES/NIST:** Standart.
* **RSA/ECC:** Dünya standardı.
* **D.A.H.A.:** Yeni bir kategori, uzun test süreçleri gerekir.
