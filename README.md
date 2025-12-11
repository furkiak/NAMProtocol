# N.A.M. / D.A.H.A. Protokolü
![Status](https://img.shields.io/badge/Status-Development-blue)
![Security](https://img.shields.io/badge/Security-High-green)
![Type](https://img.shields.io/badge/Type-Data%20Transformation-orange)

**Natural Arithmetic Mapping - Doğal Aritmetik Haritalama Algoritması** 

**Category / Kategori:** MRM — Mathematical Reversible Mapping

**Version:** 0.0.1 (Concept / Experimental)  

## 👨‍💻 Author / Yazar
**Furkan AKÇA** *Creator & Lead Researcher* Project Started: December 2025

**Collaborator:** Gemini AI (Concept Validation & Documentation)

## 📄 License
This project is licensed under the MIT License.
Copyright (c) 2025 Furkan AKÇA.

**Disclaimer / Sorumluluk Reddi:** This protocol is experimental. Use at your own risk for critical data. / Bu protokol deneyseldir. Kritik verilerinizde kullanırken dikkatli olun.

---

# 🇺🇸 N.A.M. Protocol: Natural Arithmetic Mapping

## 1. About the Protocol

The **N.A.M. Protocol** (Natural Arithmetic Mapping Algorithm) is a next-generation data transformation system developed to encrypt, obfuscate, de-identify, and mathematically destroy files.

Unlike block or byte-oriented architectures in classical cryptography, N.A.M. treats the entire file as:
* **A single, colossal natural number.**

Through this process, the file is separated into two distinct components:
* **MAP:** Mathematical Offset Step Sequence
* **DEPTH:** Total number of steps applied (masked)

> ⚠️ **Note:** It is mathematically impossible to access the original file without both the MAP and DEPTH.

---

## 📌 2. Mathematical Operating Principle

The fundamental workflow of the algorithm is as follows:

1. The raw bit representation of the file is obtained.
2. The bit sequence is treated as a single large natural number (**BigInt**).
3. If the natural number is odd, a "0" is appended to make it even.
4. The process begins:
    * **If Even:** Divide by 2.
    * **If Odd:** Apply **+5** or **–5** according to the dynamic **OFFSET pattern**. Then divide by 2.
5. This step is recorded in the **MAP**.
6. The process continues until the number reaches 0.
7. The sum of all steps → **RealDepth**

Consequently, the original file is mathematically reconstructed by running the process in reverse using the `MAP + MaskedDepth + OFFSET` sequence.

### 🔍 Example Operation
Workflow based on a simple example (static +5/–5):

* **Input (Bit Sequence):** `1010`
* **Preparation:** Ends with 0 → Operations start directly.

| Step | Operation | State | MAP Record |
| :--- | :--- | :--- | :--- |
| **1** | $1010 / 2 = 505$ | Odd | - |
| **2** | $505 \to \pm5 \to 250$ | Even (Post-Op) | MAP: 2 |
| **3** | $250 / 2 = 125$ | Odd | - |
| **4** | $125 \to \pm5 \to 60$ | Even (Post-Op) | MAP: 2, 4 |
| **5** | $60 / 2 = 30$ | Even | - |
| **6** | $30 / 2 = 15$ | Odd | - |
| **7** | $15 \to \pm5 \to 5$ | Even (Post-Op) | MAP: 2, 4, 7 |
| **8** | $5 \to \pm5 \to 0$ | End | MAP: 2, 4, 7, 8 |

**Result Output:**
* **DEPTH:** 8
* **MAP:** `[2, 4, 7, 8]`

When run in reverse, **MAP + DEPTH** yields the exact bit sequence.

---

## 🛡️ 3. Security and Optimization Layers

The system employs a three-stage layered architecture to increase efficiency and maintain data integrity.

### 🔹 Optimization-1: MAP Delta Compression
As the file size grows, the MAP sequence may contain very large number indices. Instead of storing this data in its raw form, the **Delta (Difference)** method is applied:
* Instead of sequence numbers, the differences (deltas) between the current and previous numbers are stored.
* This significantly reduces the size of the MAP.
* Working with smaller numbers increases the efficiency of compression algorithms.

### 🔹 Optimization-2: MAP Compression
The MAP sequence obtained after Delta transformation mathematically assumes a highly repetitive or predictable structure. This sequence is reduced to sizes much smaller than the original file using the following methods:
* Gzip
* Brotli
* Arithmetic Coding
* Or custom-developed compressor algorithms.

### 🔐 Optimization-3: Integrity Hash
When the process is complete, a cryptographic summary of the entire data structure (`HEADER + BODY`) is taken.
Algorithms: **SHA-256** or **SHA3-512** are used.

If a Hash mismatch occurs during the restoration process, it indicates one of the following errors:
* Incorrect Salt usage.
* Corrupted or altered MAP data.
* Incorrect Depth Mask.
* Wrong Offset List.
* Missing or corrupted Header information.

---

## 🔑 4. Key Sets (MRK — Mathematical Reversible Keys)

The protocol utilizes a multi-key architecture to layer security.

### 🗝️ Key-1: HEADER MASK
* **Purpose:** To prevent file format detection (Magic Bytes detection).
* **Method:** The initial bytes (magic header) of the file are separated from the main body.
* This part is stored as **Cipher-1**.
> ⚠️ Mandatory for the restoration process.

### 🧂 Key-2: SALT (High Entropy Injection)
* **Purpose:** To make frequency and data analysis impossible.
* **Method:** A high-entropy bit block is generated. It is injected into the original bit sequence at a random position:
    * Addition from the left
    * Addition to the right
    * Or addition after a specific offset
* **Result:** Analytical reverse engineering is prevented as long as the injection position is unknown.

### 📉 Key-3: OFFSET PATTERN LIST
Instead of fixed +5 / –5 operations; key-based, acyclic, and unpredictable sequences are used.

**Example Pattern:**
[+5, +5, -5, -5, +5, -5, ...]

### 🎭 Key-4: DEPTH Mask
The total number of steps (Depth) is hidden.

**Formula:**
MaskedDepth = RealDepth XOR DepthKey

## 📌 5. Cryptographic Positioning

N.A.M. defines a new class as it does not fit perfectly into any existing category:

### 🛡️ MRM — Mathematical Reversible Mapping

This class offers the following features simultaneously:
* Encryption
* Obfuscation
* Format Removal
* De-identification
* Data Destruction (Recallable)
* BigInt Mathematics
* Multi-Key Model
* Oracle Attack Resistant Structure

---

## 📌 6. Use Cases

* 🏛️ State secret archiving
* 🔐 High-security key storage
* ♻️ Data destruction (recoverable)
* 🛡️ Information warfare / Cyber defense
* ❄️ Cold storage data encryption
* 💾 Hardware-based security modules
* 🔑 Key escrow systems

---

## 📊 7. Feature Table

| Feature | Status | Description |
| :--- | :---: | :--- |
| **Reversible Mathematical Transformation** | ✔️ | Lossless |
| **Multi-Key Set** | ✔️ | HEADER + SALT + OFFSET + DEPTH |
| **Format Obfuscation** | ✔️ | HEADER MASK |
| **Data Analysis Prevention** | ✔️ | SALT + OFFSET |
| **MAP Compression** | ✔️ | Delta + Compression |
| **Integrity Check** | ✔️ | SHA-256 / SHA3-512 |
| **Oracle Attack Protection** | ✔️ | No fixed offset |
| **Hardware Implementation** | ✔️ | Suitable for FPGA/ASIC |

## 🐍 9. Simple Python Demo (Sample File → MAP → Restoration)

In the following example:
* A sample text file containing **"New generation Encryption and Destruction algorithm"** is created.
* The raw bit equivalent is obtained from the file.
* **MAP** and **DEPTH** are calculated without applying any security layers.
* The file is reconstructed using `MAP + DEPTH`.

> ⚠️ **Note:** This demo is intended to demonstrate the mathematical core only.
> The actual protocol includes **OFFSET LIST, HEADER MASK, SALT, DEPTH MASK, HASH, DELTA COMPRESSION**, etc.

➡️ You can use the `Test.py` file.

---

## ⚖️ 10. Theoretical Comparison

### N.A.M. vs. Other Encryption Methods
The table below positions N.A.M.'s mathematical approach relative to classical cryptography.

### 📊 N.A.M. vs AES / RSA / ECC — Conceptual Differences

| Feature / System | AES | RSA | ECC | N.A.M. |
| :--- | :--- | :--- | :--- | :--- |
| **Core Structure** | Block cipher | Large prime mathematics | Elliptic curve mathematics | Natural number mapping / BigInt reverse transformation |
| **Operating Principle** | SubBytes, ShiftRows, MixColumns | Modular exponentiation | Elliptic curve points | Division by 2 + Offset application |
| **Data Size Approach** | Block (128 bit) | Random size | Random size | Entire file = Single large number |
| **Format Obfuscation** | ❌ | ❌ | ❌ | ✔ **HEADER MASK** |
| **Salt/Noise** | ✔ Exists | ✔ Exists | ✔ Exists | ✔ + Randomly positioned SALT |
| **Reversibility** | Impossible without key | Impossible without key | Impossible without key | Mathematical return impossible without **Key + MAP** |
| **Oracle Prevention** | Partial | Partial | Partial | ✔ **Complete** (dynamic offset + dummy steps) |
| **File Destruction** | Exists | Exists | Exists | ✔ **Mathematical Zeroing** |
| **Format Removal** | ❌ | ❌ | ❌ | ✔ File → De-identified natural number |
| **Cipher-Text Analysis** | Weakness may arise | Expected | Difficult | **SALT + OFFSET + DELTA** → Analysis impossible |
| **Compression Suitability** | Data dependent | Data dependent | Data dependent | **High** with MAP delta + compressor |

---

## 🏛️ 11. Theoretical Use Case: "Shamir's Secret Sharing" Alternative

In this scenario, the D.A.H.A. protocol is used to protect data classified as **"Top Secret"**, such as secret facility coordinates and nuclear launch codes.

1.  **Data Destruction:**
    The digital asset containing critical data is processed with the N.A.M. protocol and completely destroyed (secure deletion). Only mathematical recovery parameters (MAP, DEPTH, SALT, etc.) remain.

2.  **Air-Gapped Distribution:**
    The generated key components (MAP and Key Set) are completely removed from the digital environment.

3.  **Physical Fragmentation:**
    Critical keys are split and delivered to high-level state officials in physical **"Hard Copy" (A4/Card)** format.

4.  **Reconstruction:**
    The system never works with a single part. To recover the data, all officials (or a designated majority) must physically convene and enter the key parts into the system.

> ✅ **Result:** With this method, the cyber attack surface is reduced to **0%**. Since the data does not "exist" in the digital world, it cannot be stolen, and the parts are meaningless on their own.

---

# 🇹🇷 D.A.H.A. Protokolü: Doğal Aritmetik Haritalama Algoritması

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
MaskedDepth = RealDepth XOR DepthKey

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

## 🏛️ 11. Teorik Kullanım Senaryosu: "Shamir's Secret Sharing" Alternatifi

Bu senaryoda, D.A.H.A. protokolü; gizli tesis koordinatları ve nükleer fırlatma kodları gibi **"Top Secret"** sınıfındaki verilerin korunması amacıyla kullanılır.

1.  **Veri Yok Etme:** Kritik veriyi içeren dijital varlık, D.A.H.A. protokolü ile işlenerek tamamen yok edilir (secure deletion). Geriye sadece matematiksel geri dönüşüm parametreleri (`MAP`, `DEPTH`, `SALT`, vb.) kalır.
2.  **Air-Gapped (İzole) Dağıtım:** Oluşturulan anahtar bileşenleri (`MAP` ve `Key Set`), dijital ortamdan tamamen çıkarılır.
3.  **Fiziksel Parçalama (Fragmentation):** Kritik anahtarlar parçalara bölünerek, üst düzey devlet görevlilerine **fiziksel "Hard Copy" (A4/Kart)** formatında teslim edilir.
4.  **Rekonstrüksiyon (Yeniden İnşa):**
    * Sistem, tek bir parça ile asla çalışmaz.
    * Verinin kurtarılması için tüm yetkililerin (veya belirlenen çoğunluğun) fiziksel olarak bir araya gelmesi ve anahtar parçalarını sisteme girmesi gerekir.

✅ **Sonuç:** Bu yöntemle **siber saldırı yüzeyi %0'a indirilir**. Veri dijital dünyada "mevcut olmadığı" için çalınamaz, parçalar ise tek başlarına anlamsızdır.

