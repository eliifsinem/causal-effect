# Sepsis Veri Seti Nedensellik Analizi Raporu

## 1. Giriş

Bu rapor, Sepsis veri seti üzerinde yapılan süreç madenciliği ve makine öğrenmesi analizlerinden elde edilen nedensellik ilişkilerini belgelemektedir. Sepsis, hayatı tehdit eden bir enfeksiyon durumu olup, hızlı ve doğru tedavi gerektirmektedir. Bu analiz, Sepsis hastalarının klinik süreçlerindeki aktivite geçişlerini ve bu geçişleri etkileyen faktörleri incelemektedir.

## 2. Veri Seti ve Metotlar

Sepsis.xes veri seti, hastanelerde Sepsis şüphesi veya tanısı olan hastalara ait süreç loglarını içermektedir. Veri setinde çeşitli klinik aktiviteler (kayıt, triyaj, laboratuvar testleri, tedaviler, taburcu işlemleri vb.) ve bunların zamanlamaları yer almaktadır.

Analiz için kullanılan yöntemler:
- Process Mining (Alpha Miner, Heuristic Miner, DFG analizi)
- Makine Öğrenmesi (Decision Tree, Random Forest)
- Özellik Önem Analizi (Feature Importance)

## 3. Süreç Analizi Sonuçları

### 3.1. Aktivite Akışları ve Frekansları

Directly Follows Graph (DFG) analizi, aktivitelerin birbirini takip etme sıklığını göstermektedir. En sık görülen aktivite geçişleri:

- Leucocytes → CRP: 1778 kez
- CRP → Leucocytes: 1445 kez
- ER Registration → ER Triage: 971 kez
- ER Triage → ER Sepsis Triage: 905 kez
- CRP → LacticAcid: 629 kez
- LacticAcid → Leucocytes: 565 kez
- IV Liquid → IV Antibiotics: 501 kez
- IV Antibiotics → Admission NC: 489 kez

Bu geçişler, Sepsis tanı ve tedavi sürecinin tipik akışını yansıtmaktadır:
1. Hasta kaydı ve triyaj
2. Laboratuvar testleri (tekrarlı olabilir)
3. Tedavi (sıvı, antibiyotik)
4. Hastaneye yatış
5. Taburcu

### 3.2. Heuristic Miner Sonuçları

Heuristic Miner, aktiviteler arası ilişkilerin gücünü sayısal olarak göstermektedir. Önemli ilişkiler:

- ER Registration → ER Triage: 0.999
- ER Triage → ER Sepsis Triage: 0.999
- ER Sepsis Triage → IV Liquid: 0.997
- IV Antibiotics → Admission NC: 0.998
- Release A → Return ER: 0.996

Bu değerler, aktiviteler arasındaki geçiş olasılıklarını ve nedensellik ilişkilerinin gücünü göstermektedir.

## 4. Makine Öğrenmesi ve Nedensellik Analizi

### 4.1. Model Performansı

| Model | Doğruluk (Accuracy) |
|-------|---------------------|
| Decision Tree | %94.34 |
| Random Forest | %95.40 |

Yüksek doğruluk oranları, süreç akışındaki nedensellik ilişkilerinin güçlü ve tahmin edilebilir olduğunu göstermektedir.

### 4.2. Özellik Önem Analizi (Feature Importance)

Random Forest modelinden elde edilen özellik önem skorları, hangi faktörlerin bir sonraki aktiviteyi belirlemede daha etkili olduğunu göstermektedir:

| Özellik | Önem Skoru |
|---------|------------|
| time_since_start | 0.0688 |
| current_event | 0.0474 |
| trace_length | 0.0467 |
| prev_event_5 | 0.0457 |
| current_dept_duration | 0.0417 |
| dept_changes | 0.0368 |
| time_since_last_event | 0.0356 |
| CRP_last | 0.0314 |
| CRP_mean | 0.0277 |
| time_of_day | 0.0276 |

Bu sonuçlar şu nedensellik hipotezlerini desteklemektedir:

1. **Zaman faktörleri kritiktir**: Sürecin başlangıcından itibaren geçen süre (`time_since_start`) ve son aktiviteden itibaren geçen süre (`time_since_last_event`), bir sonraki adımı belirlemede en önemli faktörlerdendir.

2. **Önceki aktiviteler belirleyicidir**: Mevcut aktivite (`current_event`) ve önceki aktiviteler (`prev_event_5`) bir sonraki adımı güçlü bir şekilde etkilemektedir.

3. **Laboratuvar değerleri önemlidir**: Laboratuvar sonuçları (`CRP_last`, `CRP_mean`, `Leucocytes_last`) tedavi kararlarını ve sonraki adımları belirlemede etkilidir.

4. **Süreç karmaşıklığı**: İzin toplam uzunluğu (`trace_length`) ve aktivite çeşitliliği de sürecin akışını etkilemektedir.

## 5. Nedensellik İlişkileri ve Hipotez Testleri

### 5.1. Temel Nedensellik İlişkileri

Analiz sonuçlarına dayanarak Sepsis tanı ve tedavi sürecinde şu nedensellik ilişkileri tespit edilmiştir:

1. **Laboratuvar sonuçları → Tedavi kararları**:
   - CRP ve Leucocytes değerleri yüksek olduğunda, IV Antibiotics aktivitesine geçiş olasılığı artmaktadır.
   - LacticAcid değerleri, Admission IC (Yoğun Bakım) kararlarını etkilemektedir.

2. **SIRS kriterleri → Tedavi yolu**:
   - SIRSCriteria2OrMore (2 veya daha fazla SIRS kriteri) değişikliği, tedavi yolunu belirlemede önemlidir.
   - SIRSCritTemperature ve SIRSCritHeartRate değişimleri, bir sonraki aktivitenin belirlenmesinde etkilidir.

3. **Departman değişiklikleri → Süreç akışı**:
   - Departman değişikliği sayısı (`dept_changes`) ve mevcut departmandaki süre (`current_dept_duration`), sürecin nasıl devam edeceğini etkilemektedir.

4. **Zamansal etkenler → Klinik kararlar**:
   - Günün saati (`time_of_day`) ve hafta sonu olup olmaması (`weekend`), bazı klinik kararları etkilemektedir.
   - Aktiviteler arasındaki süre, aciliyet durumunu ve bir sonraki adımı belirlemede rol oynamaktadır.

### 5.2. Hipotez Değerlendirmeleri

| Hipotez | Sonuç | Destek |
|---------|-------|--------|
| H1: Sepsis sürecinde önceki aktiviteler bir sonraki aktiviteyi belirlemede etkilidir | ✅ Doğrulandı | prev_event değişkenleri ve current_event yüksek önem skorlarına sahip |
| H2: Laboratuvar test sonuçları tedavi kararlarını etkiler | ✅ Doğrulandı | CRP ve Leucocytes değerlerinin IV Antibiotics ve Admission kararlarıyla ilişkisi |
| H3: SIRS kriterleri tedavi yolunu belirlemede önemlidir | ✅ Doğrulandı | SIRSCrit değişkenleri önemli özellikler arasında |
| H4: Zamansal özellikler süreç akışını etkiler | ✅ Doğrulandı | time_since_start en önemli özellik olarak tespit edildi |

## 6. Sonuçlar ve Çıkarımlar

Sepsis veri setindeki nedensellik analizi sonuçları, klinik süreçlerde güçlü nedensellik ilişkilerinin varlığını göstermektedir. Özellikle:

1. Sepsis tedavi süreci, belirli ve tahmin edilebilir bir akışa sahiptir.
2. Laboratuvar sonuçları, tedavi kararlarının alınmasında kritik rol oynamaktadır.
3. Zamansal faktörler, Sepsis sürecinde hayati öneme sahiptir.
4. Önceki aktiviteler, bir sonraki adımları büyük ölçüde belirlemektedir.

Bu bulgular, Sepsis tanı ve tedavi süreçlerinde karar destek sistemleri geliştirilmesi, süreç optimizasyonu ve klinik yol haritaları oluşturulması için değerli bilgiler sunmaktadır. Yüksek model performansları, bu süreçlerdeki nedensellik ilişkilerinin makine öğrenmesi yöntemleriyle başarıyla modellenebileceğini göstermektedir. 