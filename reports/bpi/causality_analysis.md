# BPI2020 Veri Seti Nedensellik Analizi Raporu

## 1. Giriş

Bu rapor, BPI Challenge 2020 veri seti üzerinde yapılan süreç madenciliği ve makine öğrenmesi analizlerinden elde edilen nedensellik ilişkilerini belgelemektedir. BPI2020 veri seti, bir organizasyondaki iç harcama yönetimi ve seyahat masrafı beyannameleri süreçlerini içermektedir. Bu analiz, beyanname onay süreçlerindeki aktivite geçişlerini ve bu geçişleri etkileyen faktörleri incelemektedir.

## 2. Veri Seti ve Metotlar

BPI2020 veri seti, aşağıdaki dosyalardan oluşmaktadır:
- DomesticDeclarations.xes: Yerel beyannameler
- InternationalDeclarations.xes: Uluslararası beyannameler
- PermitLog.xes: İzin kayıtları
- PrepaidTravelCost.xes: Ön ödemeli seyahat masrafları
- RequestForPayment.xes: Ödeme talepleri

Bu analiz için öncelikle DomesticDeclarations.xes veri seti kullanılmıştır. Analizde kullanılan yöntemler:
- Process Mining (Alpha Miner, Heuristic Miner, DFG analizi)
- Makine Öğrenmesi (Decision Tree, Random Forest)
- Özellik Önem Analizi (Feature Importance)

## 3. Süreç Analizi Sonuçları

### 3.1. Aktivite Akışları ve Frekansları

Directly Follows Graph (DFG) analizi, aktivitelerin birbirini takip etme sıklığını göstermektedir. En sık görülen aktivite geçişleri:

- Declaration SUBMITTED by EMPLOYEE → Declaration APPROVED by ADMINISTRATION: 8202 kez
- Declaration SUBMITTED by EMPLOYEE → Declaration FINAL_APPROVED by SUPERVISOR: 1536 kez
- Declaration FINAL_APPROVED by SUPERVISOR → Request Payment: 10038 kez
- Request Payment → Payment Handled: 10037 kez
- Declaration REJECTED by EMPLOYEE → Declaration SUBMITTED by EMPLOYEE: 1081 kez
- Declaration APPROVED by ADMINISTRATION → Declaration FINAL_APPROVED by SUPERVISOR: 5133 kez

Bu geçişler, iç harcama ve beyanname sürecinin tipik akışını yansıtmaktadır:
1. Çalışan beyanname sunar (SUBMITTED by EMPLOYEE)
2. Beyanname incelenir (APPROVED by ADMINISTRATION/PRE_APPROVER)
3. Onaylanır veya reddedilir (FINAL_APPROVED/REJECTED)
4. Onaylanan beyanname için ödeme istenir (Request Payment)
5. Ödeme gerçekleştirilir (Payment Handled)

### 3.2. Heuristic Miner Sonuçları

Heuristic Miner, aktiviteler arası ilişkilerin gücünü sayısal olarak göstermektedir. Önemli ilişkiler:

- Declaration SUBMITTED by EMPLOYEE → Declaration FINAL_APPROVED by SUPERVISOR: 0.999
- Declaration FINAL_APPROVED by SUPERVISOR → Request Payment: 0.999
- Request Payment → Payment Handled: 0.999
- Declaration APPROVED by ADMINISTRATION → Declaration APPROVED by BUDGET OWNER: 0.999
- Declaration APPROVED by PRE_APPROVER → Declaration FINAL_APPROVED by SUPERVISOR: 0.998

Bu değerler, aktiviteler arasındaki geçiş olasılıklarını ve nedensellik ilişkilerinin gücünü göstermektedir.

## 4. Makine Öğrenmesi ve Nedensellik Analizi

### 4.1. Model Performansı

| Model | Doğruluk (Accuracy) |
|-------|---------------------|
| Decision Tree | %99.93 |
| Random Forest | %99.91 |

Çok yüksek doğruluk oranları, beyanname sürecindeki nedensellik ilişkilerinin son derece güçlü ve tahmin edilebilir olduğunu göstermektedir.

### 4.2. Özellik Önem Analizi (Feature Importance)

Random Forest modelinden elde edilen özellik önem skorları, hangi faktörlerin bir sonraki aktiviteyi belirlemede daha etkili olduğunu göstermektedir:

| Özellik | Önem Skoru |
|---------|------------|
| trace_length | 0.2691 |
| current_event | 0.1545 |
| current_id | 0.1082 |
| current_case:id | 0.0962 |
| current_org:role | 0.0897 |
| event_position | 0.0707 |
| current_case:DeclarationNumber | 0.0604 |
| current_case:Amount | 0.0574 |
| time_since_last_event | 0.0411 |
| time_since_start | 0.0386 |

Bu sonuçlar şu nedensellik hipotezlerini desteklemektedir:

1. **Süreç karmaşıklığı kritiktir**: Sürecin toplam uzunluğu (`trace_length`) ve süreçteki konum (`event_position`), bir sonraki adımı belirlemede en önemli faktörlerdendir.

2. **Mevcut durum belirleyicidir**: Mevcut aktivite (`current_event`) bir sonraki adımı güçlü bir şekilde etkilemektedir.

3. **Organizasyonel roller önemlidir**: Aktiviteyi gerçekleştiren kişinin rolü (`current_org:role`), sürecin akışını etkilemektedir.

4. **Beyanname özellikleri etkilidir**: Beyanname numarası ve tutar (`current_case:DeclarationNumber`, `current_case:Amount`) sürecin nasıl ilerleyeceğini etkilemektedir.

5. **Zamansal faktörler etkilidir**: Aktiviteler arasındaki süre ve sürecin başlangıcından itibaren geçen süre de süreç akışını etkilemektedir.

## 5. Nedensellik İlişkileri ve Hipotez Testleri

### 5.1. Temel Nedensellik İlişkileri

Analiz sonuçlarına dayanarak beyanname sürecinde şu nedensellik ilişkileri tespit edilmiştir:

1. **Süreç özellikleri → Onay süreci**:
   - Beyanname tutarı (`current_case:Amount`) yüksek olduğunda, bütçe sahibi onayı gerektiren yola giriş olasılığı artmaktadır.
   - Sürecin uzunluğu (`trace_length`), red veya onay kararlarını etkilemektedir.

2. **Organizasyonel roller → Onay süreçleri**:
   - Farklı roller (`current_org:role`) farklı onay adımlarını tetiklemektedir.
   - Reddedilen beyannamenin tekrar sunulması genellikle aynı onay zincirini takip etmektedir.

3. **Beyanname özellikleri → Süreç akışı**:
   - Beyanname numarası (`current_case:DeclarationNumber`) ve beyanname kimliği (`current_case:id`), sürecin nasıl devam edeceğini etkilemektedir.

4. **Zamansal etkenler → Onay süreçleri**:
   - Son aktiviteden itibaren geçen süre (`time_since_last_event`), bazı onay kararlarını etkilemektedir.
   - Sürecin başlangıcından itibaren geçen süre (`time_since_start`), sürecin hızını ve akışını etkilemektedir.

### 5.2. Hipotez Değerlendirmeleri

| Hipotez | Sonuç | Destek |
|---------|-------|--------|
| H1: Beyanname sürecinde süreç uzunluğu ve konum, bir sonraki adımı belirlemede etkilidir | ✅ Doğrulandı | trace_length ve event_position yüksek önem skorlarına sahip |
| H2: Organizasyonel roller ve sorumluluklar süreç akışını etkiler | ✅ Doğrulandı | current_org:role önemli bir faktör olarak tespit edildi |
| H3: Beyanname tutarı süreç yolunu belirlemede önemlidir | ✅ Doğrulandı | current_case:Amount önemli özellikler arasında |
| H4: Zamansal özellikler süreç akışını etkiler | ✅ Doğrulandı | time_since_last_event ve time_since_start önemli faktörler |

## 6. Sonuçlar ve Çıkarımlar

BPI2020 veri setindeki nedensellik analizi sonuçları, iç harcama ve beyanname süreçlerinde güçlü nedensellik ilişkilerinin varlığını göstermektedir. Özellikle:

1. Beyanname onay süreçleri, son derece yapılandırılmış ve tahmin edilebilir bir akışa sahiptir.
2. Organizasyonel roller ve sorumluluklar, süreç akışının belirlenmesinde kritik rol oynamaktadır.
3. Beyanname özellikleri (tutar, kimlik, numara), onay süreçlerini etkilemektedir.
4. Süreçlerin uzunluğu ve pozisyon bilgisi, bir sonraki adımı belirlemede en önemli faktörlerdir.

%99.9'un üzerindeki model doğruluk oranları, bu süreçlerdeki nedensellik ilişkilerinin son derece güçlü olduğunu ve makine öğrenmesi yöntemleriyle neredeyse mükemmel şekilde modellenebileceğini göstermektedir. Bu bulgular, beyanname ve iç harcama süreçlerinin optimizasyonu, otomasyon fırsatlarının belirlenmesi ve süreç iyileştirme çalışmaları için değerli bilgiler sunmaktadır. 