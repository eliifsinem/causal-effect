# RequestForPayment Analiz Sonuçları

## Log Yükleme
dataset/RequestForPayment.xes dosyası başarıyla yüklendi.

## Alpha Miner Sonuçları
Alpha Miner ile süreç modeli oluşturuldu.

(<pm4py.objects.petri.petrinet.PetriNet object at 0x139d91e90>, ['start:1'], ['end:1'])

## Heuristic Miner Sonuçları
{'Request For Payment SUBMITTED by EMPLOYEE': (node:Request For Payment SUBMITTED by EMPLOYEE connections:{Request For Payment FINAL_APPROVED by SUPERVISOR:[0.9984779299847792], Request For Payment APPROVED by PRE_APPROVER:[0.9975845410628019], Request For Payment REJECTED by SUPERVISOR:[0.9772727272727273], Request For Payment APPROVED by SUPERVISOR:[0.9230769230769231], Request For Payment REJECTED by PRE_APPROVER:[0.9807692307692307], Request For Payment REJECTED by ADMINISTRATION:[0.998805256869773], Request For Payment APPROVED by ADMINISTRATION:[0.9998178506375228], Request For Payment FOR_APPROVAL by ADMINISTRATION:[0]}), 'Request For Payment FINAL_APPROVED by SUPERVISOR': (node:Request For Payment FINAL_APPROVED by SUPERVISOR connections:{Request For Payment REJECTED by MISSING:[0.9848484848484849], Request Payment:[0.9998403066113063]}), 'Request For Payment APPROVED by PRE_APPROVER': (node:Request For Payment APPROVED by PRE_APPROVER connections:{Request For Payment FINAL_APPROVED by SUPERVISOR:[0.9975609756097561]}), 'Request For Payment REJECTED by SUPERVISOR': (node:Request For Payment REJECTED by SUPERVISOR connections:{Request For Payment REJECTED by EMPLOYEE:[0.9942528735632183]}), 'Request For Payment APPROVED by SUPERVISOR': (node:Request For Payment APPROVED by SUPERVISOR connections:{Request For Payment FINAL_APPROVED by DIRECTOR:[0.975609756097561]}), 'Request For Payment REJECTED by PRE_APPROVER': (node:Request For Payment REJECTED by PRE_APPROVER connections:{Request For Payment REJECTED by EMPLOYEE:[0.9807692307692307]}), 'Request For Payment REJECTED by ADMINISTRATION': (node:Request For Payment REJECTED by ADMINISTRATION connections:{Request For Payment REJECTED by EMPLOYEE:[0.9987684729064039]}), 'Request For Payment APPROVED by ADMINISTRATION': (node:Request For Payment APPROVED by ADMINISTRATION connections:{Request For Payment FINAL_APPROVED by SUPERVISOR:[0.9996981587684878], Request For Payment APPROVED by BUDGET OWNER:[0.9995037220843672], Request For Payment REJECTED by SUPERVISOR:[0.9895833333333334], Request For Payment REJECTED by BUDGET OWNER:[0.9791666666666666], Request For Payment APPROVED by SUPERVISOR:[0.95], Request For Payment FINAL_APPROVED by BUDGET OWNER:[0.5], Request For Payment FOR_APPROVAL by SUPERVISOR:[0.5]}), 'Request For Payment REJECTED by MISSING': (node:Request For Payment REJECTED by MISSING connections:{Request For Payment SUBMITTED by EMPLOYEE:[0.9615384615384616]}), 'Request Payment': (node:Request Payment connections:{Payment Handled:[0.9998412950325345]}), 'Payment Handled': (node:Payment Handled connections:{}), 'Request For Payment REJECTED by EMPLOYEE': (node:Request For Payment REJECTED by EMPLOYEE connections:{Request For Payment SUBMITTED by EMPLOYEE:[0.9984276729559748], Request For Payment SAVED by EMPLOYEE:[0.6666666666666666]}), 'Request For Payment SAVED by EMPLOYEE': (node:Request For Payment SAVED by EMPLOYEE connections:{}), 'Request For Payment FINAL_APPROVED by DIRECTOR': (node:Request For Payment FINAL_APPROVED by DIRECTOR connections:{Request Payment:[0.975]}), 'Request For Payment APPROVED by BUDGET OWNER': (node:Request For Payment APPROVED by BUDGET OWNER connections:{Request For Payment FINAL_APPROVED by SUPERVISOR:[0.9994916115912558], Request For Payment REJECTED by SUPERVISOR:[0.9743589743589743], Request For Payment APPROVED by SUPERVISOR:[0.9]}), 'Request For Payment REJECTED by BUDGET OWNER': (node:Request For Payment REJECTED by BUDGET OWNER connections:{Request For Payment REJECTED by EMPLOYEE:[0.9791666666666666]}), 'Request For Payment FINAL_APPROVED by BUDGET OWNER': (node:Request For Payment FINAL_APPROVED by BUDGET OWNER connections:{Payment Handled:[0.5]}), 'Request For Payment FOR_APPROVAL by SUPERVISOR': (node:Request For Payment FOR_APPROVAL by SUPERVISOR connections:{}), 'Request For Payment FOR_APPROVAL by ADMINISTRATION': (node:Request For Payment FOR_APPROVAL by ADMINISTRATION connections:{Request For Payment SUBMITTED by EMPLOYEE:[0]})}

Heuristic Miner ile heuristik ağ (heu_net) elde edildi.

## Directly Follows Graph (DFG)
Directly Follows Graph elde edildi.

### Start Activities:
- Request For Payment SUBMITTED by EMPLOYEE: 6814
- Request For Payment SAVED by EMPLOYEE: 72

### End Activities:
- Payment Handled: 6305
- Request For Payment REJECTED by MISSING: 41
- Request For Payment REJECTED by EMPLOYEE: 448
- Request For Payment FINAL_APPROVED by DIRECTOR: 1
- Request For Payment SAVED by EMPLOYEE: 74
- Request For Payment FINAL_APPROVED by SUPERVISOR: 11
- Request For Payment REJECTED by ADMINISTRATION: 2
- Request Payment: 2
- Request For Payment FOR_APPROVAL by SUPERVISOR: 1
- Request For Payment REJECTED by SUPERVISOR: 1

### DFG Kenarları:
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 656 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Request For Payment REJECTED by MISSING') -> 65 kez gözlenmiş
- ('Request For Payment REJECTED by MISSING', 'Request For Payment SUBMITTED by EMPLOYEE') -> 25 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment APPROVED by PRE_APPROVER') -> 413 kez gözlenmiş
- ('Request For Payment APPROVED by PRE_APPROVER', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 409 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Request Payment') -> 6261 kez gözlenmiş
- ('Request Payment', 'Payment Handled') -> 6300 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment REJECTED by SUPERVISOR') -> 43 kez gözlenmiş
- ('Request For Payment REJECTED by SUPERVISOR', 'Request For Payment REJECTED by EMPLOYEE') -> 173 kez gözlenmiş
- ('Request For Payment REJECTED by EMPLOYEE', 'Request For Payment SUBMITTED by EMPLOYEE') -> 635 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment APPROVED by SUPERVISOR') -> 12 kez gözlenmiş
- ('Request For Payment APPROVED by SUPERVISOR', 'Request For Payment FINAL_APPROVED by DIRECTOR') -> 40 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by DIRECTOR', 'Request Payment') -> 39 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment REJECTED by PRE_APPROVER') -> 51 kez gözlenmiş
- ('Request For Payment REJECTED by PRE_APPROVER', 'Request For Payment REJECTED by EMPLOYEE') -> 51 kez gözlenmiş
- ('Request For Payment REJECTED by SUPERVISOR', 'Request For Payment SUBMITTED by EMPLOYEE') -> 5 kez gözlenmiş
- ('Request For Payment APPROVED by PRE_APPROVER', 'Request For Payment REJECTED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment REJECTED by ADMINISTRATION') -> 836 kez gözlenmiş
- ('Request For Payment REJECTED by ADMINISTRATION', 'Request For Payment REJECTED by EMPLOYEE') -> 811 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment APPROVED by ADMINISTRATION') -> 5489 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 3312 kez gözlenmiş
- ('Request Payment', 'Request For Payment REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Request For Payment APPROVED by PRE_APPROVER', 'Request For Payment FINAL_APPROVED by DIRECTOR') -> 1 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by DIRECTOR', 'Request For Payment APPROVED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Request For Payment APPROVED by SUPERVISOR', 'Request Payment') -> 1 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment APPROVED by BUDGET OWNER') -> 2014 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Request For Payment FINAL_APPROVED by SUPERVISOR') -> 1966 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment REJECTED by SUPERVISOR') -> 95 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Request For Payment REJECTED by SUPERVISOR') -> 38 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Request For Payment APPROVED by SUPERVISOR') -> 9 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment REJECTED by BUDGET OWNER') -> 47 kez gözlenmiş
- ('Request For Payment REJECTED by BUDGET OWNER', 'Request For Payment REJECTED by EMPLOYEE') -> 47 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment APPROVED by SUPERVISOR') -> 19 kez gözlenmiş
- ('Request For Payment REJECTED by ADMINISTRATION', 'Request For Payment SUBMITTED by EMPLOYEE') -> 23 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment FOR_APPROVAL by ADMINISTRATION') -> 1 kez gözlenmiş
- ('Request For Payment FOR_APPROVAL by ADMINISTRATION', 'Request For Payment SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Request For Payment REJECTED by EMPLOYEE', 'Request For Payment SAVED by EMPLOYEE') -> 2 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by SUPERVISOR', 'Payment Handled') -> 6 kez gözlenmiş
- ('Request For Payment SUBMITTED by EMPLOYEE', 'Request For Payment REJECTED by EMPLOYEE') -> 3 kez gözlenmiş
- ('Request For Payment APPROVED by BUDGET OWNER', 'Request For Payment SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment FINAL_APPROVED by BUDGET OWNER') -> 1 kez gözlenmiş
- ('Request For Payment FINAL_APPROVED by BUDGET OWNER', 'Payment Handled') -> 1 kez gözlenmiş
- ('Payment Handled', 'Request Payment') -> 2 kez gözlenmiş
- ('Request For Payment APPROVED by ADMINISTRATION', 'Request For Payment FOR_APPROVAL by SUPERVISOR') -> 1 kez gözlenmiş

