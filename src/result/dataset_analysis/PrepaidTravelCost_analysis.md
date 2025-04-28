# PrepaidTravelCost Analiz Sonuçları

## Log Yükleme
dataset/PrepaidTravelCost.xes dosyası başarıyla yüklendi.

## Alpha Miner Sonuçları
Alpha Miner ile süreç modeli oluşturuldu.

(<pm4py.objects.petri.petrinet.PetriNet object at 0x12e7e4890>, ['start:1'], ['end:1'])

## Heuristic Miner Sonuçları
{'Permit SUBMITTED by EMPLOYEE': (node:Permit SUBMITTED by EMPLOYEE connections:{Permit FINAL_APPROVED by SUPERVISOR:[0.9907407407407407], Permit APPROVED by SUPERVISOR:[0.9807692307692307], Permit APPROVED by PRE_APPROVER:[0.9936305732484076], Permit REJECTED by PRE_APPROVER:[0.9411764705882353], Permit REJECTED by SUPERVISOR:[0.8], Permit APPROVED by ADMINISTRATION:[0.9993765586034913], Permit REJECTED by ADMINISTRATION:[0.9375]}), 'Permit FINAL_APPROVED by SUPERVISOR': (node:Permit FINAL_APPROVED by SUPERVISOR connections:{Request For Payment SUBMITTED by EMPLOYEE:[0.9992295839753467], Request For Payment FINAL_APPROVED by SUPERVISOR:[0.989010989010989], Request For Payment SAVED by EMPLOYEE:[0.9], Permit REJECTED by MISSING:[0.5]}), 'Permit APPROVED by SUPERVISOR': (node:Permit APPROVED by SUPERVISOR connections:{Permit FINAL_APPROVED by DIRECTOR:[0.9972222222222222], Request For Payment APPROVED by SUPERVISOR:[0.6666666666666666], Request For Payment REJECTED by SUPERVISOR:[0.5]}), 'Permit APPROVED by PRE_APPROVER': (node:Permit APPROVED by PRE_APPROVER connections:{Permit FINAL_APPROVED by SUPERVISOR:[0.9924242424242424], Request For Payment SUBMITTED by EMPLOYEE:[0.9090909090909091], Permit APPROVED by SUPERVISOR:[0.9411764705882353]}), 'Permit REJECTED by PRE_APPROVER': (node:Permit REJECTED by PRE_APPROVER connections:{Permit REJECTED by EMPLOYEE:[0.9411764705882353]}), 'Permit REJECTED by SUPERVISOR': (node:Permit REJECTED by SUPERVISOR connections:{Permit REJECTED by EMPLOYEE:[0.967741935483871], Request For Payment REJECTED by SUPERVISOR:[0.5]}), 'Permit APPROVED by ADMINISTRATION': (node:Permit APPROVED by ADMINISTRATION connections:{Permit APPROVED by BUDGET OWNER:[0.9981481481481481], Request For Payment SUBMITTED by EMPLOYEE:[0.9939024390243902], Permit FINAL_APPROVED by SUPERVISOR:[0.9985443959243085], Permit APPROVED by SUPERVISOR:[0.9940476190476191], Permit REJECTED by SUPERVISOR:[0.9565217391304348], Permit REJECTED by BUDGET OWNER:[0.9411764705882353], Request For Payment SAVED by EMPLOYEE:[0.8], Request For Payment REJECTED by SUPERVISOR:[0.5]}), 'Permit REJECTED by ADMINISTRATION': (node:Permit REJECTED by ADMINISTRATION connections:{Permit REJECTED by EMPLOYEE:[0.9230769230769231], Request For Payment SUBMITTED by EMPLOYEE:[0.75]}), 'Request For Payment SUBMITTED by EMPLOYEE': (node:Request For Payment SUBMITTED by EMPLOYEE connections:{Request For Payment FINAL_APPROVED by SUPERVISOR:[0.9926470588235294], Request For Payment APPROVED by PRE_APPROVER:[0.9937888198757764], Request For Payment REJECTED by PRE_APPROVER:[0.9473684210526315], Request For Payment APPROVED by SUPERVISOR:[0.8571428571428571], Request For Payment APPROVED by ADMINISTRATION:[0.9994182664339732], Request For Payment REJECTED by ADMINISTRATION:[0.9955156950672646]}), 'Request For Payment FINAL_APPROVED by SUPERVISOR': (node:Request For Payment FINAL_APPROVED by SUPERVISOR connections:{Request For Payment REJECTED by MISSING:[0.875], Request Payment:[0.9994753410283316], Permit REJECTED by MISSING:[0.5]}), 'Request For Payment SAVED by EMPLOYEE': (node:Request For Payment SAVED by EMPLOYEE connections:{Permit APPROVED by BUDGET OWNER:[0.75], Permit APPROVED by SUPERVISOR:[0.5]}), 'Permit REJECTED by MISSING': (node:Permit REJECTED by MISSING connections:{Permit SUBMITTED by EMPLOYEE:[0.9166666666666666], Request Payment:[0.5]}), 'Request For Payment APPROVED by PRE_APPROVER': (node:Request For Payment APPROVED by PRE_APPROVER connections:{Request For Payment FINAL_APPROVED by SUPERVISOR:[0.9933774834437086], Request For Payment APPROVED by SUPERVISOR:[0.75], Request For Payment REJECTED by SUPERVISOR:[0.5]}), 'Request For Payment REJECTED by PRE_APPROVER': (node:Request For Payment REJECTED by PRE_APPROVER connections:{Request For Payment REJECTED by EMPLOYEE:[0.9473684210526315]}), 'Request For Payment APPROVED by SUPERVISOR': (node:Request For Payment APPROVED by SUPERVISOR connections:{Request For Payment FINAL_APPROVED by DIRECTOR:[0.9743589743589743], Permit FINAL_APPROVED by DIRECTOR:[0.6666666666666666]}), 'Request For Payment APPROVED by ADMINISTRATION': (node:Request For Payment APPROVED by ADMINISTRATION connections:{Request For Payment FINAL_APPROVED by SUPERVISOR:[0.9989270386266095], Request For Payment APPROVED by BUDGET OWNER:[0.9984615384615385], Permit APPROVED by BUDGET OWNER:[0.9791666666666666], Request For Payment REJECTED by SUPERVISOR:[0.9], Request For Payment APPROVED by SUPERVISOR:[0.9411764705882353], Request For Payment REJECTED by BUDGET OWNER:[0.875]}), 'Request For Payment REJECTED by ADMINISTRATION': (node:Request For Payment REJECTED by ADMINISTRATION connections:{Request For Payment REJECTED by EMPLOYEE:[0.9952153110047847], Permit REJECTED by SUPERVISOR:[0.6666666666666666]}), 'Request For Payment REJECTED by MISSING': (node:Request For Payment REJECTED by MISSING connections:{Permit REJECTED by MISSING:[0.6666666666666666]}), 'Request Payment': (node:Request Payment connections:{Payment Handled:[0.999492385786802], Request For Payment REJECTED by MISSING:[0.5]}), 'Payment Handled': (node:Payment Handled connections:{Permit REJECTED by MISSING:[0.9285714285714286]}), 'Permit FINAL_APPROVED by DIRECTOR': (node:Permit FINAL_APPROVED by DIRECTOR connections:{Request For Payment SUBMITTED by EMPLOYEE:[0.9970760233918129], Permit REJECTED by MISSING:[0.8333333333333334], Request For Payment SAVED by EMPLOYEE:[0.6666666666666666], Request For Payment FINAL_APPROVED by DIRECTOR:[0.6666666666666666]}), 'Request For Payment REJECTED by SUPERVISOR': (node:Request For Payment REJECTED by SUPERVISOR connections:{Request For Payment REJECTED by EMPLOYEE:[0.9523809523809523], Permit FINAL_APPROVED by DIRECTOR:[0.5]}), 'Request For Payment FINAL_APPROVED by DIRECTOR': (node:Request For Payment FINAL_APPROVED by DIRECTOR connections:{Request Payment:[0.9743589743589743], Request For Payment REJECTED by MISSING:[0.5]}), 'Request For Payment REJECTED by EMPLOYEE': (node:Request For Payment REJECTED by EMPLOYEE connections:{Request For Payment SUBMITTED by EMPLOYEE:[0.9947643979057592], Request For Payment SAVED by EMPLOYEE:[0.6666666666666666]}), 'Permit REJECTED by EMPLOYEE': (node:Permit REJECTED by EMPLOYEE connections:{Permit SUBMITTED by EMPLOYEE:[0.9876543209876543]}), 'Request For Payment APPROVED by BUDGET OWNER': (node:Request For Payment APPROVED by BUDGET OWNER connections:{Request For Payment FINAL_APPROVED by SUPERVISOR:[0.9984051036682615], Permit FINAL_APPROVED by SUPERVISOR:[0.9743589743589743], Request For Payment APPROVED by SUPERVISOR:[0.9333333333333333], Request For Payment REJECTED by SUPERVISOR:[0.8]}), 'Permit APPROVED by BUDGET OWNER': (node:Permit APPROVED by BUDGET OWNER connections:{Permit FINAL_APPROVED by SUPERVISOR:[0.9975062344139651], Request For Payment APPROVED by BUDGET OWNER:[0.9761904761904762], Permit APPROVED by SUPERVISOR:[0.9921875], Permit REJECTED by SUPERVISOR:[0.75]}), 'Request For Payment REJECTED by BUDGET OWNER': (node:Request For Payment REJECTED by BUDGET OWNER connections:{Permit APPROVED by BUDGET OWNER:[0.5], Request For Payment REJECTED by EMPLOYEE:[0.8], Request For Payment SUBMITTED by EMPLOYEE:[0.6666666666666666]}), 'Permit REJECTED by BUDGET OWNER': (node:Permit REJECTED by BUDGET OWNER connections:{Permit REJECTED by EMPLOYEE:[0.9411764705882353]})}

Heuristic Miner ile heuristik ağ (heu_net) elde edildi.

## Directly Follows Graph (DFG)
Directly Follows Graph elde edildi.

### Start Activities:
- Permit SUBMITTED by EMPLOYEE: 1859
- Request For Payment SUBMITTED by EMPLOYEE: 233
- Request For Payment SAVED by EMPLOYEE: 7

### End Activities:
- Permit REJECTED by MISSING: 10
- Payment Handled: 1970
- Request For Payment REJECTED by MISSING: 7
- Request For Payment REJECTED by EMPLOYEE: 72
- Request For Payment SAVED by EMPLOYEE: 20
- Permit FINAL_APPROVED by DIRECTOR: 6
- Permit FINAL_APPROVED by SUPERVISOR: 12
- Request For Payment REJECTED by ADMINISTRATION: 1
- Request Payment: 1

### DFG Kenarları:
- ('Permit SUBMITTED by EMPLOYEE', 'Permit FINAL_APPROVED by SUPERVISOR') -> 107 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Request For Payment SUBMITTED by EMPLOYEE') -> 1297 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 135 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Request For Payment REJECTED by MISSING') -> 7 kez gözlenmiş
- ('Request For Payment REJECTED by MISSING', 'Permit REJECTED by MISSING') -> 2 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Request Payment') -> 1905 kez gözlenmiş
- ('Request Payment', 'Payment Handled') -> 1969 kez gözlenmiş
- ('Payment Handled', 'Permit REJECTED by MISSING') -> 13 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit APPROVED by SUPERVISOR') -> 51 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Permit FINAL_APPROVED by DIRECTOR') -> 359 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Request For Payment SUBMITTED by EMPLOYEE') -> 341 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment APPROVED by PRE_APPROVER') -> 160 kez gözlenmiş
- ('Request For Payment APPROVED by PRE_APPROVER', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 150 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit APPROVED by PRE_APPROVER') -> 156 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'Permit FINAL_APPROVED by SUPERVISOR') -> 131 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment REJECTED by PRE_APPROVER') -> 18 kez gözlenmiş
- ('Request For Payment REJECTED by PRE_APPROVER', 'Request For Payment REJECTED by EMPLOYEE') -> 18 kez gözlenmiş
- ('Request For Payment REJECTED by EMPLOYEE', 'Request For Payment SUBMITTED by EMPLOYEE') -> 190 kez gözlenmiş
- ('Request For Payment APPROVED by PRE_APPROVER', 'Request For Payment APPROVED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Request For Payment APPROVED by SUPERVISOR', 'Request For Payment FINAL_APPROVED by DIRECTOR') -> 38 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by DIRECTOR', 'Request Payment') -> 38 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Permit APPROVED by PRE_APPROVER') -> 2 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'Request For Payment SUBMITTED by EMPLOYEE') -> 10 kez gözlenmiş
- ('Request Payment', 'Request For Payment REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit REJECTED by PRE_APPROVER') -> 16 kez gözlenmiş
- ('Permit REJECTED by PRE_APPROVER', 'Permit REJECTED by EMPLOYEE') -> 16 kez gözlenmiş
- ('Permit REJECTED by EMPLOYEE', 'Permit SUBMITTED by EMPLOYEE') -> 80 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'Permit APPROVED by SUPERVISOR') -> 16 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment REJECTED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Request For Payment REJECTED by SUPERVISOR', 'Request For Payment REJECTED by EMPLOYEE') -> 20 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit REJECTED by SUPERVISOR') -> 4 kez gözlenmiş
- ('Permit REJECTED by SUPERVISOR', 'Permit REJECTED by EMPLOYEE') -> 30 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment APPROVED by SUPERVISOR') -> 6 kez gözlenmiş
- ('Request For Payment APPROVED by PRE_APPROVER', 'Permit FINAL_APPROVED by SUPERVISOR') -> 6 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 90 kez gözlenmiş
- ('Request For Payment APPROVED by PRE_APPROVER', 'Request For Payment REJECTED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'Permit REJECTED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Request For Payment SUBMITTED by EMPLOYEE') -> 10 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Permit FINAL_APPROVED by DIRECTOR') -> 14 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Request Payment') -> 16 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Permit REJECTED by MISSING') -> 5 kez gözlenmiş
- ('Permit REJECTED by MISSING', 'Permit SUBMITTED by EMPLOYEE') -> 11 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by DIRECTOR', 'Request For Payment REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Request For Payment SAVED by EMPLOYEE') -> 9 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Permit REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Permit REJECTED by MISSING', 'Request Payment') -> 1 kez gözlenmiş
- ('Payment Handled', 'Permit SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Request For Payment SAVED by EMPLOYEE') -> 2 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Permit REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Permit FINAL_APPROVED by SUPERVISOR') -> 26 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Request Payment') -> 26 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment APPROVED by ADMINISTRATION') -> 1718 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 931 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment APPROVED by BUDGET OWNER') -> 649 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 626 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment REJECTED by ADMINISTRATION') -> 222 kez gözlenmiş
- ('Request For Payment REJECTED by ADMINISTRATION', 'Request For Payment REJECTED by EMPLOYEE') -> 208 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit APPROVED by ADMINISTRATION') -> 1603 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit APPROVED by BUDGET OWNER') -> 539 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Permit FINAL_APPROVED by SUPERVISOR') -> 400 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Request For Payment SUBMITTED by EMPLOYEE') -> 22 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Permit FINAL_APPROVED by SUPERVISOR') -> 38 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Request For Payment SUBMITTED by EMPLOYEE') -> 163 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Permit APPROVED by BUDGET OWNER') -> 47 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Request For Payment APPROVED by BUDGET OWNER') -> 41 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Permit APPROVED by BUDGET OWNER') -> 4 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Request For Payment REJECTED by ADMINISTRATION') -> 7 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Request For Payment APPROVED by SUPERVISOR') -> 14 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit FINAL_APPROVED by SUPERVISOR') -> 686 kez gözlenmiş
- ('Request For Payment APPROVED by SUPERVISOR', 'Permit APPROVED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Request For Payment FINAL_APPROVED by DIRECTOR') -> 1 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by DIRECTOR', 'Permit FINAL_APPROVED by DIRECTOR') -> 1 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit APPROVED by SUPERVISOR') -> 167 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Permit APPROVED by SUPERVISOR') -> 127 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Permit APPROVED by SUPERVISOR') -> 10 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 15 kez gözlenmiş
- ('Request Payment', 'Permit FINAL_APPROVED by DIRECTOR') -> 10 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Payment Handled') -> 11 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Permit FINAL_APPROVED by SUPERVISOR') -> 54 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment REJECTED by SUPERVISOR') -> 9 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit REJECTED by ADMINISTRATION') -> 15 kez gözlenmiş
- ('Permit REJECTED by ADMINISTRATION', 'Permit REJECTED by EMPLOYEE') -> 12 kez gözlenmiş
- ('Request Payment', 'Permit FINAL_APPROVED by SUPERVISOR') -> 4 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Payment Handled') -> 5 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Request For Payment APPROVED by BUDGET OWNER') -> 14 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Permit APPROVED by SUPERVISOR') -> 10 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Permit FINAL_APPROVED by DIRECTOR') -> 1 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Request For Payment APPROVED by BUDGET OWNER') -> 1 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment APPROVED by SUPERVISOR') -> 16 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 8 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Permit FINAL_APPROVED by DIRECTOR') -> 2 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Permit APPROVED by SUPERVISOR') -> 2 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Permit FINAL_APPROVED by SUPERVISOR') -> 7 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Request For Payment APPROVED by ADMINISTRATION') -> 4 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment REJECTED by BUDGET OWNER') -> 7 kez gözlenmiş
- ('Request For Payment REJECTED by BUDGET OWNER', 'Permit APPROVED by BUDGET OWNER') -> 1 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Request For Payment REJECTED by EMPLOYEE') -> 5 kez gözlenmiş
- ('Request For Payment REJECTED by EMPLOYEE', 'Permit FINAL_APPROVED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Permit APPROVED by BUDGET OWNER') -> 10 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit REJECTED by SUPERVISOR') -> 22 kez gözlenmiş
- ('Permit REJECTED by ADMINISTRATION', 'Request For Payment SUBMITTED by EMPLOYEE') -> 3 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Permit REJECTED by EMPLOYEE') -> 2 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Request For Payment APPROVED by ADMINISTRATION') -> 1 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Request For Payment REJECTED by SUPERVISOR') -> 4 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit REJECTED by BUDGET OWNER') -> 16 kez gözlenmiş
- ('Permit REJECTED by BUDGET OWNER', 'Permit REJECTED by EMPLOYEE') -> 16 kez gözlenmiş
- ('Request For Payment REJECTED by BUDGET OWNER', 'Request For Payment REJECTED by EMPLOYEE') -> 4 kez gözlenmiş
- ('Request For Payment REJECTED by EMPLOYEE', 'Request For Payment SAVED by EMPLOYEE') -> 2 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Permit APPROVED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Request Payment') -> 2 kez gözlenmiş
- ('Request Payment', 'Permit APPROVED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Request For Payment APPROVED by ADMINISTRATION') -> 1 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Permit REJECTED by BUDGET OWNER') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by ADMINISTRATION', 'Permit FINAL_APPROVED by SUPERVISOR') -> 10 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Request For Payment REJECTED by EMPLOYEE') -> 10 kez gözlenmiş
- ('Request For Payment REJECTED by ADMINISTRATION', 'Permit APPROVED by BUDGET OWNER') -> 4 kez gözlenmiş
- ('Payment Handled', 'Permit FINAL_APPROVED by SUPERVISOR') -> 5 kez gözlenmiş
- ('Request For Payment REJECTED by SUPERVISOR', 'Request For Payment SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Request For Payment SAVED by EMPLOYEE') -> 4 kez gözlenmiş
- ('Request For Payment SAVED by EMPLOYEE', 'Permit APPROVED by BUDGET OWNER') -> 3 kez gözlenmiş
- ('Request For Payment REJECTED by ADMINISTRATION', 'Request For Payment SUBMITTED by EMPLOYEE') -> 4 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Permit REJECTED by SUPERVISOR') -> 2 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Request For Payment REJECTED by ADMINISTRATION') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by EMPLOYEE', 'Permit APPROVED by BUDGET OWNER') -> 1 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Request For Payment APPROVED by SUPERVISOR') -> 2 kez gözlenmiş
- ('Request For Payment APPROVED by SUPERVISOR', 'Permit FINAL_APPROVED by DIRECTOR') -> 2 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Request For Payment FINAL_APPROVED by DIRECTOR') -> 2 kez gözlenmiş
- ('Request Payment', 'Permit REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Payment Handled') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by ADMINISTRATION', 'Permit REJECTED by SUPERVISOR') -> 2 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Request For Payment REJECTED by EMPLOYEE') -> 2 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Permit REJECTED by SUPERVISOR') -> 2 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Request For Payment REJECTED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by SUPERVISOR', 'Permit FINAL_APPROVED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Request For Payment REJECTED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by SUPERVISOR', 'Permit FINAL_APPROVED by DIRECTOR') -> 1 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Request For Payment REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Request For Payment SAVED by EMPLOYEE', 'Permit APPROVED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Permit REJECTED by SUPERVISOR', 'Request For Payment SUBMITTED by EMPLOYEE') -> 2 kez gözlenmiş
- ('Request For Payment REJECTED by ADMINISTRATION', 'Permit REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by EMPLOYEE', 'Permit APPROVED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Request Payment', 'Permit APPROVED by BUDGET OWNER') -> 3 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Payment Handled') -> 2 kez gözlenmiş
- ('Permit REJECTED by SUPERVISOR', 'Request For Payment REJECTED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by SUPERVISOR', 'Permit REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Permit REJECTED by EMPLOYEE', 'Request For Payment REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by EMPLOYEE', 'Permit SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Permit REJECTED by SUPERVISOR', 'Request For Payment REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by EMPLOYEE', 'Permit REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Permit REJECTED by BUDGET OWNER', 'Request For Payment SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Permit REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Request Payment') -> 1 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by DIRECTOR', 'Payment Handled') -> 1 kez gözlenmiş
- ('Payment Handled', 'Request Payment') -> 1 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Permit REJECTED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Permit REJECTED by EMPLOYEE') -> 3 kez gözlenmiş
- ('Permit REJECTED by EMPLOYEE', 'Request For Payment REJECTED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Permit REJECTED by SUPERVISOR', 'Request For Payment APPROVED by ADMINISTRATION') -> 2 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Request For Payment REJECTED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by BUDGET OWNER', 'Request For Payment SUBMITTED by EMPLOYEE') -> 2 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Payment Handled') -> 1 kez gözlenmiş

