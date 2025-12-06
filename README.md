# N.A.M. Protocol (Natural Arithmetic Mapping)
### (D.A.H.A. Protokolü - Doğal Aritmetik Haritalama Algoritması)

**Version:** 1.0.0 (Concept / Experimental)  

## 👨‍💻 Author / Yazar

**[Furkan AKÇA]** *Creator & Lead Researcher* Project Started: December 2025

**Collaborator:** Gemini AI (Concept Validation & Documentation)

## 📄 License

This project is licensed under the MIT License.
Copyright (c) 2025 [Furkan AKÇA].

**Disclaimer / Sorumluluk Reddi:** This protocol is experimental. Use at your own risk for critical data. / Bu protokol deneyseldir. Kritik verilerinizde kullanırken dikkatli olun.


---

## 🌍 [English] N.A.M. Protocol Whitepaper

### 📋 Abstract
The **N.A.M. Protocol (Natural Arithmetic Mapping)** is a next-generation "Split-Key" encryption and obfuscation architecture designed for extreme data security. Unlike standard encryption methods (AES, RSA) that treat data as blocks of bits, N.A.M. treats the entire data stream as a single, massive **Natural Number**.

By separating the file's format signature (Header), statistical structure (Salt), and magnitude (Depth), the protocol renders the encrypted data (Map) mathematically meaningless and unsolvable without all three keys. The goal is not compression, but absolute privacy through arithmetic transformation.

### 1. Philosophy: Oracle-less Encryption
Traditional encryption often leaves traces (file headers, patterns) that allow attackers to verify if a brute-force attempt was successful (Oracle).

**N.A.M. operates on this premise:**
*"If the format (Header), the starting point (Salt), and the magnitude (Depth) of data are unknown, the map leading to that data is mathematically useless."*

### 2. System Architecture: The Trinity Keys
The security relies on three independent parameters. The stored `MAP` file on the disk is just noise without these keys.

#### 🔑 Key 1: HEADER (Format Signature)
* **Function:** The file header (e.g., `ftyp` for MP4, `%PDF` for PDF) is stripped before processing.
* **Security:** Without this key, even if the data is decrypted, the operating system cannot recognize or open the file. It eliminates the "success verification" for attackers.

#### 🧂 Key 2: SALT (Entropy Injection)
* **Function:** A high-entropy random number added to the beginning of the headless body.
* **Security:** It destroys the statistical frequency of the file. The same file produces a completely different Map with a different Salt (Avalanche Effect).

#### 📏 Key 3: DEPTH (Step Count)
* **Function:** The exact number of arithmetic steps performed.
* **Security:** It determines the bit-alignment. A single digit error in Depth results in a complete bit-shift error, corrupting the entire dataset.

### 3. The Algorithm

#### 3.1. Encryption
1.  **Stripping:** Remove the `Header` (Save as Key-1).
2.  **Salting:** Prepend `Salt` to the remaining body (Save as Key-2).
3.  **Conversion:** Treat the data chunk ($Salt + Body$) as a massive Natural Number ($N$).
4.  **Mapping Loop:**
    * Divide $N$ by 2.
    * If $N$ is Odd (decimal ends in 5): Record the step index to `MAP` and subtract 5 (or apply algorithmic equivalent).
    * Repeat until $N$ becomes 0.
5.  **Output:** Save the total step count as **Key-3 (Depth)** and the list of indices as the `MAP` file.

#### 3.2. Decryption
1.  **Initialization:** Start with number $0$ and the `MAP` list.
2.  **Reconstruction:**
    * Loop backwards from **Key-3 (Depth)** down to 1.
    * Operation: $N = N \times 2$ (Left Bit Shift).
    * If the current step index exists in `MAP`: $N = N + 5$.
3.  **Finalization:**
    * Subtract/Remove **Key-2 (Salt)**.
    * Prepend **Key-1 (Header)**.
    * **Result:** Original file is restored.

### 4. Security & Trade-offs
* **Impossibility of Brute-Force:** An attacker must guess the Header, the Salt, and the exact Depth simultaneously. Since the file has no header, there is no way to verify if a guess is correct.
* **Data Expansion:** The `MAP` file stores addresses of bits rather than bits themselves. The file size will increase significantly (estimated 3x - 10x).
* **Performance:** Requires BigInt arithmetic, making it slower than hardware-accelerated AES.

### 5. Use Cases
* **Cold Storage:** Securing archives where size is irrelevant, but security is paramount.
* **Deep Obfuscation:** Hiding critical text or keys within massive numeric maps.
* **State-Level Secrecy:** Scenarios requiring physically separated keys.

---
---

## 🇹🇷 [Türkçe] D.A.H.A. Protokolü Whitepaper

### 📋 Özet
**D.A.H.A. Protokolü (Doğal Aritmetik Haritalama Algoritması)**, yüksek veri güvenliği için tasarlanmış, **"Parçalı Anahtar" (Split-Key)** mimarisine dayanan yeni nesil bir şifreleme ve gizleme protokolüdür. Veriyi bloklar halinde işleyen standart yöntemlerin (AES, RSA) aksine, D.A.H.A. verinin tamamını tek ve devasa bir **Doğal Sayı** olarak kabul eder.

Dosyanın format imzasını (Header), istatistiksel yapısını (Salt) ve büyüklüğünü (Depth) birbirinden ayırarak, şifreli veriyi (Map) bu üç anahtar olmadan matematiksel olarak çözülemez hale getirir. Amaç sıkıştırma değil, aritmetik dönüşüm yoluyla mutlak gizliliktir.

### 1. Felsefe: Doğrulayıcısız (Oracle-less) Şifreleme
Geleneksel şifreleme, saldırganların deneme-yanılma yaparken başarılı olup olmadıklarını anlamalarına yarayan izler (dosya başlıkları vb.) bırakabilir.

**D.A.H.A. şu varsayımla çalışır:**
*"Bir verinin formatı (Header), başlangıç noktası (Salt) ve derinliği (Depth) bilinmiyorsa; o veriye giden yol haritası matematiksel olarak hiçbir anlam ifade etmez."*

### 2. Sistem Mimarisi: 3-Anahtarlı Yapı
Sistem güvenliği birbirinden bağımsız 3 parametreye dayanır. Diskteki `MAP` dosyası, bu anahtarlar olmadan sadece gürültüdür.

#### 🔑 Anahtar 1: HEADER (Format İmzası)
* **İşlevi:** Dosya başlığı (Örn: MP4 için `ftyp`, PDF için `%PDF`) işlemden önce kesilir.
* **Güvenlik:** Bu anahtar olmadan, veri çözülse bile işletim sistemi dosyayı tanıyamaz ve açamaz. Saldırgan için "başarı doğrulamasını" yok eder.

#### 🧂 Anahtar 2: SALT (Tuzlama)
* **İşlevi:** Başlıksız gövdenin en başına eklenen yüksek entropili rastgele sayıdır.
* **Güvenlik:** Dosyanın istatistiksel frekansını bozar. Aynı dosya, farklı Salt ile tamamen farklı bir Harita üretir.

#### 📏 Anahtar 3: DEPTH (Basamak/Adım Sayısı)
* **İşlevi:** Yapılan aritmetik işlemin toplam adım sayısıdır.
* **Güvenlik:** Bit hizalamasını belirler. Depth değerindeki tek bir rakam hatası, tüm veride bit kayması (bit-shift) hatasına neden olur ve veriyi bozar.

### 3. Algoritma

#### 3.1. Şifreleme
1.  **Ayrıştırma:** Dosyanın `Header` kısmı kesilir ve **Anahtar-1** olarak saklanır.
2.  **Tuzlama:** Kalan gövdenin başına `Salt` eklenir ve **Anahtar-2** olarak saklanır.
3.  **Dönüşüm:** Veri yığını ($Salt + Body$) devasa bir Doğal Sayı ($N$) olarak işlenir.
4.  **Haritalama Döngüsü:**
    * $N$ sayısı 2'ye bölünür.
    * Sayı Tek ise (Onluk tabanda sonu 5): Adım sırası `MAP` listesine kaydedilir ve 5 çıkarılır.
    * Sayı 0 olana kadar devam eder.
5.  **Çıktı:** Toplam adım sayısı **Anahtar-3 (Depth)** ve oluşan liste `MAP` dosyası olarak kaydedilir.

#### 3.2. Deşifreleme
1.  **Başlangıç:** $0$ sayısı ve `MAP` listesi ile başlanır.
2.  **Geri Sarma:**
    * **Anahtar-3 (Depth)** sayısından geriye doğru döngü kurulur.
    * İşlem: $N = N \times 2$ (Sola Bit Kaydırma).
    * Eğer o anki adım `MAP` listesinde varsa: $N = N + 5$.
3.  **Sonlandırma:**
    * Oluşan sayıdan **Anahtar-2 (Salt)** çıkarılır.
    * Başına **Anahtar-1 (Header)** eklenir.
    * **Sonuç:** Orijinal dosya geri yüklenir.

### 4. Güvenlik ve Kısıtlar
* **Brute-Force İmkansızlığı:** Saldırgan Header, Salt ve Depth değerlerini aynı anda doğru tahmin etmek zorundadır. Header olmadığı için tahminin doğruluğunu test edemez.
* **Veri Genişlemesi:** `MAP` dosyası bitlerin kendisini değil adreslerini tuttuğu için dosya boyutu artar (Tahmini 3x - 10x).
* **Performans:** Büyük sayı (BigInt) aritmetiği gerektirdiği için donanım tabanlı şifrelemelerden daha yavaştır.

### 5. Kullanım Alanları
* **Cold Storage (Soğuk Depolama):** Boyutun önemsiz olduğu ama güvenliğin kritik olduğu arşivler.
* **Derin Gizleme (Obfuscation):** Kritik metin veya anahtarların devasa sayısal haritalar içinde saklanması.
* **Devlet Düzeyinde Gizlilik:** Anahtarların fiziksel olarak ayrı yerlerde tutulması gereken senaryolar.

---
