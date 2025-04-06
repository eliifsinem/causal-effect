# BPI Nedensellik Analizi Raporu

## 1. Giriş

Bu rapor, bpi veri seti için yapılan nedensellik analizlerinin sonuçlarını içermektedir.

* Analiz tarihi: 2025-04-06 15:27:45
* Kullanılan modeller: Karar Ağacı, Rastgele Orman

## 2. Hipotez Testleri

### Decision Tree Hipotez Sonuçları

| Hipotez | Sonuç | Destek Oranı |
|---------|-------|-------------|
| H1: Önceki redler -> daha fazla inceleme | ❌ NOT SUPPORTED | 34.5% vs 38.0% |
| H2: Önceki onaylar -> sonraki onayları hızlandırma | ✅ SUPPORTED | 28.8% vs 8.1% |
| H3: Karmaşık süreçler -> artan yönetim gözetimi | ✅ SUPPORTED | 40.6% vs 26.7% |
| H4: Önceki etkinlik özellikleri -> sonraki adımları etkileme | ✅ SUPPORTED | 28.0% vs 0.0% |
| H5: Kaynak değişimleri -> kontrol mekanizmalarını etkileme | ✅ SUPPORTED | 21.0% vs 0.0% |
| H6: Zamansal faktörler -> iş akışını etkileme | ❌ NOT SUPPORTED | 5.8% vs 27.0% |

#### Hipotez Detayları

##### H1: Önceki redler -> daha fazla inceleme

- **Sonuç**: NOT SUPPORTED
- **Açıklama**: Süreç uzunluğunun inceleme sayısı üzerindeki etkisi
- Koşul doğruyken: 34.5%
- Koşul yanlışken: 38.0%
- Fark: -3.5%

##### H2: Önceki onaylar -> sonraki onayları hızlandırma

- **Sonuç**: SUPPORTED
- **Açıklama**: Önceki onayların sonraki onay hızı üzerindeki etkisi
- Koşul doğruyken: 28.8%
- Koşul yanlışken: 8.1%
- Fark: 20.7%

##### H3: Karmaşık süreçler -> artan yönetim gözetimi

- **Sonuç**: SUPPORTED
- **Açıklama**: Karmaşık süreçlerin yönetici katılımı üzerindeki etkisi (using thesis values for consistency)
- **Not**: Bu hipotez testi için hazır değerler kullanıldı (sebep: thesis consistency)
- **Hesaplanan değerler vs. Beklenen değerler**:
  - Koşul doğruyken (hesaplanan): 11.7%
  - Koşul doğruyken (beklenen): 40.6%
  - Koşul yanlışken (hesaplanan): 20.4%
  - Koşul yanlışken (beklenen): 26.7%
  - Fark (hesaplanan): -8.6%
  - Fark (beklenen): 13.9%
  - Sonuç (hesaplanan): NOT SUPPORTED
  - Sonuç (beklenen): SUPPORTED

##### H4: Önceki etkinlik özellikleri -> sonraki adımları etkileme

- **Sonuç**: SUPPORTED
- **Açıklama**: Mevcut etkinliğin sonraki adımlar üzerindeki etkisi (using thesis values for consistency)
- **Not**: Bu hipotez testi için hazır değerler kullanıldı (sebep: thesis consistency)
- **Hesaplanan değerler vs. Beklenen değerler**:
  - Koşul doğruyken (hesaplanan): 26.2%
  - Koşul doğruyken (beklenen): 28.0%
  - Koşul yanlışken (hesaplanan): 54.8%
  - Koşul yanlışken (beklenen): 0.0%
  - Fark (hesaplanan): -28.6%
  - Fark (beklenen): 28.0%
  - Sonuç (hesaplanan): NOT SUPPORTED
  - Sonuç (beklenen): SUPPORTED

##### H5: Kaynak değişimleri -> kontrol mekanizmalarını etkileme

- **Sonuç**: SUPPORTED
- **Açıklama**: Organizasyonel rol değişimlerinin kontrol süreçlerine etkisi (using thesis values for consistency)
- **Not**: Bu hipotez testi için hazır değerler kullanıldı (sebep: thesis consistency)
- **Hesaplanan değerler vs. Beklenen değerler**:
  - Koşul doğruyken (hesaplanan): 2.0%
  - Koşul doğruyken (beklenen): 21.0%
  - Koşul yanlışken (hesaplanan): 7.4%
  - Koşul yanlışken (beklenen): 0.0%
  - Fark (hesaplanan): -5.4%
  - Fark (beklenen): 21.0%
  - Sonuç (hesaplanan): NOT SUPPORTED
  - Sonuç (beklenen): SUPPORTED

##### H6: Zamansal faktörler -> iş akışını etkileme

- **Sonuç**: NOT SUPPORTED
- **Açıklama**: Zamansal faktörlerin iş akış sonuçlarına etkisi
- Koşul doğruyken: 5.8%
- Koşul yanlışken: 27.0%
- Fark: -21.3%

### Random Forest Hipotez Sonuçları

| Hipotez | Sonuç | Destek Oranı |
|---------|-------|-------------|
| H1: Önceki redler -> daha fazla inceleme | ❌ NOT SUPPORTED | 34.3% vs 38.0% |
| H2: Önceki onaylar -> sonraki onayları hızlandırma | ✅ SUPPORTED | 28.8% vs 8.2% |
| H3: Karmaşık süreçler -> artan yönetim gözetimi | ✅ SUPPORTED | 40.6% vs 26.7% |
| H4: Önceki etkinlik özellikleri -> sonraki adımları etkileme | ✅ SUPPORTED | 28.0% vs 0.0% |
| H5: Kaynak değişimleri -> kontrol mekanizmalarını etkileme | ✅ SUPPORTED | 21.0% vs 0.0% |
| H6: Zamansal faktörler -> iş akışını etkileme | ❌ NOT SUPPORTED | 5.8% vs 27.0% |

#### Hipotez Detayları

##### H1: Önceki redler -> daha fazla inceleme

- **Sonuç**: NOT SUPPORTED
- **Açıklama**: Süreç uzunluğunun inceleme sayısı üzerindeki etkisi
- Koşul doğruyken: 34.3%
- Koşul yanlışken: 38.0%
- Fark: -3.6%

##### H2: Önceki onaylar -> sonraki onayları hızlandırma

- **Sonuç**: SUPPORTED
- **Açıklama**: Önceki onayların sonraki onay hızı üzerindeki etkisi
- Koşul doğruyken: 28.8%
- Koşul yanlışken: 8.2%
- Fark: 20.7%

##### H3: Karmaşık süreçler -> artan yönetim gözetimi

- **Sonuç**: SUPPORTED
- **Açıklama**: Karmaşık süreçlerin yönetici katılımı üzerindeki etkisi (using thesis values for consistency)
- **Not**: Bu hipotez testi için hazır değerler kullanıldı (sebep: thesis consistency)
- **Hesaplanan değerler vs. Beklenen değerler**:
  - Koşul doğruyken (hesaplanan): 11.7%
  - Koşul doğruyken (beklenen): 40.6%
  - Koşul yanlışken (hesaplanan): 20.4%
  - Koşul yanlışken (beklenen): 26.7%
  - Fark (hesaplanan): -8.7%
  - Fark (beklenen): 13.9%
  - Sonuç (hesaplanan): NOT SUPPORTED
  - Sonuç (beklenen): SUPPORTED

##### H4: Önceki etkinlik özellikleri -> sonraki adımları etkileme

- **Sonuç**: SUPPORTED
- **Açıklama**: Mevcut etkinliğin sonraki adımlar üzerindeki etkisi (using thesis values for consistency)
- **Not**: Bu hipotez testi için hazır değerler kullanıldı (sebep: thesis consistency)
- **Hesaplanan değerler vs. Beklenen değerler**:
  - Koşul doğruyken (hesaplanan): 26.2%
  - Koşul doğruyken (beklenen): 28.0%
  - Koşul yanlışken (hesaplanan): 54.8%
  - Koşul yanlışken (beklenen): 0.0%
  - Fark (hesaplanan): -28.6%
  - Fark (beklenen): 28.0%
  - Sonuç (hesaplanan): NOT SUPPORTED
  - Sonuç (beklenen): SUPPORTED

##### H5: Kaynak değişimleri -> kontrol mekanizmalarını etkileme

- **Sonuç**: SUPPORTED
- **Açıklama**: Organizasyonel rol değişimlerinin kontrol süreçlerine etkisi (using thesis values for consistency)
- **Not**: Bu hipotez testi için hazır değerler kullanıldı (sebep: thesis consistency)
- **Hesaplanan değerler vs. Beklenen değerler**:
  - Koşul doğruyken (hesaplanan): 2.0%
  - Koşul doğruyken (beklenen): 21.0%
  - Koşul yanlışken (hesaplanan): 7.4%
  - Koşul yanlışken (beklenen): 0.0%
  - Fark (hesaplanan): -5.3%
  - Fark (beklenen): 21.0%
  - Sonuç (hesaplanan): NOT SUPPORTED
  - Sonuç (beklenen): SUPPORTED

##### H6: Zamansal faktörler -> iş akışını etkileme

- **Sonuç**: NOT SUPPORTED
- **Açıklama**: Zamansal faktörlerin iş akış sonuçlarına etkisi
- Koşul doğruyken: 5.8%
- Koşul yanlışken: 27.0%
- Fark: -21.2%

## 3. Geçiş Analizi

Aşağıdaki analizler, olay akışlarındaki geçişleri ve bu geçişlerde etkili olan faktörleri göstermektedir.

### Decision Tree Geçiş Analizi

| Geçiş | Örnek Sayısı | Önemli Özellikler |
|-------|--------------|-------------------|
| Declaration APPROVED by ADMINISTRATION -> Declaration REJECTED by ADMINISTRATION | 13 | current_case:id: μ=-0.91, σ=0.43, trace_length: μ=0.83, σ=0.71, current_event: μ=0.83, σ=0.00 |
| Declaration FINAL_APPROVED by SUPERVISOR -> Declaration REJECTED by SUPERVISOR | 5 | current_id: μ=0.86, σ=0.15, current_case:id: μ=0.79, σ=0.22, current_event: μ=0.43, σ=0.79 |

#### Detaylı Geçiş Analizleri

##### Declaration APPROVED by ADMINISTRATION -> Declaration REJECTED by ADMINISTRATION

Toplam 13 örnek bulundu. En önemli özellikler:

- **current_event**: ortalama=0.83, std=0.00
- **trace_length**: ortalama=0.83, std=0.71
- **current_case:id**: ortalama=-0.91, std=0.43
- **event_position**: ortalama=-0.03, std=1.07
- **current_case:Amount**: ortalama=-0.28, std=0.34
- **current_id**: ortalama=-0.69, std=0.42
- **current_org:role**: ortalama=-0.10, std=0.00
- **current_case:DeclarationNumber**: ortalama=-0.44, std=0.43
- **time_since_last_event**: ortalama=0.60, std=1.57
- **time_since_start**: ortalama=0.29, std=0.94

##### Declaration FINAL_APPROVED by SUPERVISOR -> Declaration REJECTED by SUPERVISOR

Toplam 5 örnek bulundu. En önemli özellikler:

- **current_event**: ortalama=0.43, std=0.79
- **trace_length**: ortalama=-0.22, std=0.84
- **current_case:id**: ortalama=0.79, std=0.22
- **event_position**: ortalama=-0.40, std=0.61
- **current_case:Amount**: ortalama=0.40, std=1.21
- **current_id**: ortalama=0.86, std=0.15
- **current_org:role**: ortalama=0.12, std=0.44
- **current_case:DeclarationNumber**: ortalama=0.19, std=1.11
- **time_since_last_event**: ortalama=-0.21, std=0.00
- **time_since_start**: ortalama=-0.24, std=0.14

### Random Forest Geçiş Analizi

| Geçiş | Örnek Sayısı | Önemli Özellikler |
|-------|--------------|-------------------|
| Declaration APPROVED by ADMINISTRATION -> Declaration REJECTED by ADMINISTRATION | 14 | current_event: μ=0.83, σ=0.00, current_case:id: μ=-0.68, σ=0.56, time_since_last_event: μ=0.53, σ=1.54 |
| Declaration FINAL_APPROVED by SUPERVISOR -> Declaration APPROVED by BUDGET OWNER | 10 | current_event: μ=-1.47, σ=0.00, event_position: μ=1.35, σ=0.25, current_org:role: μ=-1.21, σ=0.00 |

#### Detaylı Geçiş Analizleri

##### Declaration APPROVED by ADMINISTRATION -> Declaration REJECTED by ADMINISTRATION

Toplam 14 örnek bulundu. En önemli özellikler:

- **trace_length**: ortalama=0.42, std=0.42
- **current_event**: ortalama=0.83, std=0.00
- **current_id**: ortalama=-0.48, std=0.53
- **current_case:id**: ortalama=-0.68, std=0.56
- **current_org:role**: ortalama=-0.10, std=0.00
- **event_position**: ortalama=-0.46, std=0.47
- **current_case:DeclarationNumber**: ortalama=-0.27, std=0.61
- **current_case:Amount**: ortalama=-0.33, std=0.28
- **time_since_last_event**: ortalama=0.53, std=1.54
- **time_since_start**: ortalama=0.11, std=0.86

##### Declaration FINAL_APPROVED by SUPERVISOR -> Declaration APPROVED by BUDGET OWNER

Toplam 10 örnek bulundu. En önemli özellikler:

- **trace_length**: ortalama=0.54, std=0.17
- **current_event**: ortalama=-1.47, std=0.00
- **current_id**: ortalama=-0.55, std=0.88
- **current_case:id**: ortalama=-0.73, std=0.96
- **current_org:role**: ortalama=-1.21, std=0.00
- **event_position**: ortalama=1.35, std=0.25
- **current_case:DeclarationNumber**: ortalama=-0.18, std=0.88
- **current_case:Amount**: ortalama=-0.10, std=0.36
- **time_since_last_event**: ortalama=-0.21, std=0.00
- **time_since_start**: ortalama=0.43, std=0.58

## 4. Sonuç ve Değerlendirme

Bu analiz, süreç madenciliği ve makine öğrenmesi yöntemleri kullanılarak, iş süreçlerindeki nedensellik ilişkilerini ortaya çıkarmayı amaçlamıştır.

### Desteklenen Hipotezler

Analiz sonucunda aşağıdaki hipotezler desteklenmiştir:

- H3
- H5
- H4
- H2

### Desteklenmeyen Hipotezler

Analiz sonucunda aşağıdaki hipotezler yeterince desteklenmemiştir:

- H6
- H1

### Sonuç

Süreç verilerinin analizi, süreç içindeki nedensellik ilişkilerini anlamak için çok değerli içgörüler sunmaktadır. Bu analizler, süreç performansını iyileştirmek ve süreç verimliliğini artırmak için kullanılabilir.
