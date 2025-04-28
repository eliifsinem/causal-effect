# Sepsis Cases - Event Log Analiz Sonuçları

## Log Yükleme
dataset/Sepsis Cases - Event Log.xes dosyası başarıyla yüklendi.

## Alpha Miner Sonuçları
Alpha Miner ile süreç modeli oluşturuldu.

(<pm4py.objects.petri.petrinet.PetriNet object at 0x12e61d510>, ['start:1'], ['end:1'])

## Heuristic Miner Sonuçları
{'Leucocytes': (node:Leucocytes connections:{Leucocytes:[0.9978213507625272], Release A:[0.995575221238938], Release C:[0.8888888888888888], Release D:[0.9166666666666666], Release B:[0.9333333333333333], Release E:[0.6666666666666666], CRP:[0], Admission NC:[0], LacticAcid:[0], Admission IC:[0], IV Antibiotics:[0]}), 'Release A': (node:Release A connections:{Return ER:[0.9963898916967509]}), 'Release C': (node:Release C connections:{Return ER:[0.8571428571428571]}), 'Release D': (node:Release D connections:{Return ER:[0.9090909090909091]}), 'Release B': (node:Release B connections:{}), 'Release E': (node:Release E connections:{Return ER:[0.5]}), 'CRP': (node:CRP connections:{CRP:[0.9968553459119497], Release A:[0.9969040247678018], Release B:[0.95], Release C:[0.9285714285714286], Release D:[0.9230769230769231], Release E:[0.75], Leucocytes:[0], Admission NC:[0], LacticAcid:[0], Admission IC:[0], IV Liquid:[0], IV Antibiotics:[0]}), 'ER Triage': (node:ER Triage connections:{ER Sepsis Triage:[0.9988962472406181], Leucocytes:[0.9811320754716981]}), 'ER Sepsis Triage': (node:ER Sepsis Triage connections:{IV Liquid:[0.9965034965034965], Leucocytes:[0.9962962962962963], CRP:[0.9948186528497409], IV Antibiotics:[0.987012987012987], LacticAcid:[0.5549738219895288]}), 'IV Liquid': (node:IV Liquid connections:{IV Antibiotics:[0.7783687943262412], Admission NC:[0.9811320754716981], Release B:[0.5], Admission IC:[0.75], CRP:[0]}), 'IV Antibiotics': (node:IV Antibiotics connections:{Admission NC:[0.9979591836734694], Admission IC:[0.9787234042553191], Release B:[0.5], Leucocytes:[0], CRP:[0]}), 'LacticAcid': (node:LacticAcid connections:{IV Antibiotics:[0.5169491525423728], Admission NC:[0.5769230769230769], IV Liquid:[0.546583850931677], LacticAcid:[0.9880952380952381], Release B:[0.8], Release E:[0.5], Leucocytes:[0], CRP:[0]}), 'Admission NC': (node:Admission NC connections:{Admission NC:[0.9943181818181818], Release A:[0.9915254237288136], Release B:[0.8421052631578947], Admission IC:[0.64], Release D:[0.5], Release C:[0.8], Leucocytes:[0], CRP:[0]}), 'Admission IC': (node:Admission IC connections:{LacticAcid:[0.5961538461538461], Leucocytes:[0], CRP:[0]}), 'ER Registration': (node:ER Registration connections:{ER Triage:[0.9989711934156379]}), 'Return ER': (node:Return ER connections:{})}

Heuristic Miner ile heuristik ağ (heu_net) elde edildi.

## Directly Follows Graph (DFG)
Directly Follows Graph elde edildi.

### Start Activities:
- ER Registration: 995
- IV Liquid: 14
- ER Triage: 6
- CRP: 10
- ER Sepsis Triage: 7
- Leucocytes: 18

### End Activities:
- Release A: 393
- Return ER: 291
- IV Antibiotics: 87
- Release B: 55
- ER Sepsis Triage: 49
- Leucocytes: 44
- IV Liquid: 12
- Release C: 19
- CRP: 41
- LacticAcid: 24
- Release D: 14
- Admission NC: 14
- Release E: 5
- ER Triage: 2

### DFG Kenarları:
- ('ER Registration', 'Leucocytes') -> 21 kez gözlenmiş
- ('Leucocytes', 'CRP') -> 1778 kez gözlenmiş
- ('CRP', 'LacticAcid') -> 629 kez gözlenmiş
- ('LacticAcid', 'ER Triage') -> 14 kez gözlenmiş
- ('ER Triage', 'ER Sepsis Triage') -> 905 kez gözlenmiş
- ('ER Sepsis Triage', 'IV Liquid') -> 285 kez gözlenmiş
- ('IV Liquid', 'IV Antibiotics') -> 501 kez gözlenmiş
- ('IV Antibiotics', 'Admission NC') -> 489 kez gözlenmiş
- ('Admission NC', 'CRP') -> 369 kez gözlenmiş
- ('CRP', 'Leucocytes') -> 1445 kez gözlenmiş
- ('Leucocytes', 'Leucocytes') -> 458 kez gözlenmiş
- ('CRP', 'CRP') -> 317 kez gözlenmiş
- ('Leucocytes', 'Release A') -> 225 kez gözlenmiş
- ('ER Registration', 'ER Triage') -> 971 kez gözlenmiş
- ('ER Triage', 'CRP') -> 48 kez gözlenmiş
- ('LacticAcid', 'Leucocytes') -> 565 kez gözlenmiş
- ('Leucocytes', 'ER Sepsis Triage') -> 36 kez gözlenmiş
- ('CRP', 'Release A') -> 322 kez gözlenmiş
- ('ER Sepsis Triage', 'Leucocytes') -> 269 kez gözlenmiş
- ('CRP', 'IV Liquid') -> 111 kez gözlenmiş
- ('Admission NC', 'Admission NC') -> 175 kez gözlenmiş
- ('Admission NC', 'Leucocytes') -> 408 kez gözlenmiş
- ('ER Sepsis Triage', 'CRP') -> 192 kez gözlenmiş
- ('Leucocytes', 'IV Liquid') -> 102 kez gözlenmiş
- ('Release A', 'Return ER') -> 276 kez gözlenmiş
- ('IV Liquid', 'CRP') -> 46 kez gözlenmiş
- ('Leucocytes', 'LacticAcid') -> 435 kez gözlenmiş
- ('LacticAcid', 'IV Antibiotics') -> 89 kez gözlenmiş
- ('IV Antibiotics', 'IV Liquid') -> 62 kez gözlenmiş
- ('IV Liquid', 'Admission NC') -> 52 kez gözlenmiş
- ('Admission NC', 'Release A') -> 117 kez gözlenmiş
- ('IV Antibiotics', 'LacticAcid') -> 28 kez gözlenmiş
- ('LacticAcid', 'CRP') -> 404 kez gözlenmiş
- ('Leucocytes', 'Admission NC') -> 153 kez gözlenmiş
- ('Leucocytes', 'Admission IC') -> 18 kez gözlenmiş
- ('Admission IC', 'Admission NC') -> 4 kez gözlenmiş
- ('CRP', 'Admission NC') -> 187 kez gözlenmiş
- ('Admission NC', 'Release B') -> 17 kez gözlenmiş
- ('ER Sepsis Triage', 'IV Antibiotics') -> 76 kez gözlenmiş
- ('IV Antibiotics', 'Leucocytes') -> 53 kez gözlenmiş
- ('LacticAcid', 'Admission NC') -> 102 kez gözlenmiş
- ('LacticAcid', 'IV Liquid') -> 124 kez gözlenmiş
- ('ER Sepsis Triage', 'LacticAcid') -> 148 kez gözlenmiş
- ('Leucocytes', 'IV Antibiotics') -> 73 kez gözlenmiş
- ('Admission NC', 'IV Liquid') -> 22 kez gözlenmiş
- ('IV Antibiotics', 'CRP') -> 48 kez gözlenmiş
- ('Admission NC', 'Admission IC') -> 20 kez gözlenmiş
- ('Admission IC', 'LacticAcid') -> 41 kez gözlenmiş
- ('CRP', 'Release B') -> 19 kez gözlenmiş
- ('IV Liquid', 'Leucocytes') -> 55 kez gözlenmiş
- ('CRP', 'IV Antibiotics') -> 81 kez gözlenmiş
- ('IV Antibiotics', 'Admission IC') -> 46 kez gözlenmiş
- ('LacticAcid', 'LacticAcid') -> 83 kez gözlenmiş
- ('IV Liquid', 'LacticAcid') -> 36 kez gözlenmiş
- ('ER Triage', 'Leucocytes') -> 52 kez gözlenmiş
- ('LacticAcid', 'ER Sepsis Triage') -> 42 kez gözlenmiş
- ('CRP', 'Admission IC') -> 17 kez gözlenmiş
- ('CRP', 'Release C') -> 13 kez gözlenmiş
- ('ER Sepsis Triage', 'Admission NC') -> 19 kez gözlenmiş
- ('IV Liquid', 'ER Registration') -> 15 kez gözlenmiş
- ('ER Registration', 'ER Sepsis Triage') -> 11 kez gözlenmiş
- ('IV Antibiotics', 'ER Triage') -> 6 kez gözlenmiş
- ('Leucocytes', 'Release C') -> 8 kez gözlenmiş
- ('Leucocytes', 'Release D') -> 11 kez gözlenmiş
- ('Admission NC', 'LacticAcid') -> 27 kez gözlenmiş
- ('LacticAcid', 'Release A') -> 3 kez gözlenmiş
- ('CRP', 'ER Triage') -> 16 kez gözlenmiş
- ('ER Triage', 'LacticAcid') -> 29 kez gözlenmiş
- ('LacticAcid', 'Release B') -> 4 kez gözlenmiş
- ('Release D', 'Return ER') -> 10 kez gözlenmiş
- ('ER Triage', 'ER Registration') -> 5 kez gözlenmiş
- ('LacticAcid', 'Admission IC') -> 10 kez gözlenmiş
- ('Admission IC', 'CRP') -> 32 kez gözlenmiş
- ('ER Registration', 'IV Liquid') -> 22 kez gözlenmiş
- ('IV Liquid', 'ER Triage') -> 23 kez gözlenmiş
- ('Leucocytes', 'ER Registration') -> 14 kez gözlenmiş
- ('CRP', 'ER Sepsis Triage') -> 35 kez gözlenmiş
- ('ER Registration', 'LacticAcid') -> 10 kez gözlenmiş
- ('Leucocytes', 'ER Triage') -> 11 kez gözlenmiş
- ('Admission IC', 'Leucocytes') -> 38 kez gözlenmiş
- ('ER Triage', 'IV Liquid') -> 11 kez gözlenmiş
- ('IV Liquid', 'ER Sepsis Triage') -> 7 kez gözlenmiş
- ('Admission IC', 'Admission IC') -> 1 kez gözlenmiş
- ('ER Sepsis Triage', 'ER Registration') -> 5 kez gözlenmiş
- ('ER Registration', 'CRP') -> 14 kez gözlenmiş
- ('Leucocytes', 'Release B') -> 14 kez gözlenmiş
- ('CRP', 'Release D') -> 12 kez gözlenmiş
- ('IV Liquid', 'Release A') -> 2 kez gözlenmiş
- ('ER Sepsis Triage', 'Admission IC') -> 1 kez gözlenmiş
- ('CRP', 'ER Registration') -> 14 kez gözlenmiş
- ('Release A', 'CRP') -> 1 kez gözlenmiş
- ('CRP', 'Release E') -> 3 kez gözlenmiş
- ('Release E', 'Return ER') -> 1 kez gözlenmiş
- ('IV Liquid', 'Release B') -> 1 kez gözlenmiş
- ('ER Sepsis Triage', 'ER Triage') -> 5 kez gözlenmiş
- ('Admission NC', 'Release D') -> 1 kez gözlenmiş
- ('Admission NC', 'IV Antibiotics') -> 2 kez gözlenmiş
- ('Admission NC', 'Release C') -> 4 kez gözlenmiş
- ('IV Liquid', 'Admission IC') -> 3 kez gözlenmiş
- ('Release C', 'Return ER') -> 6 kez gözlenmiş
- ('IV Antibiotics', 'Release B') -> 1 kez gözlenmiş
- ('Release B', 'Admission NC') -> 1 kez gözlenmiş
- ('ER Triage', 'IV Antibiotics') -> 1 kez gözlenmiş
- ('Leucocytes', 'Release E') -> 2 kez gözlenmiş
- ('Admission NC', 'ER Sepsis Triage') -> 5 kez gözlenmiş
- ('IV Antibiotics', 'Release A') -> 2 kez gözlenmiş
- ('Return ER', 'CRP') -> 3 kez gözlenmiş
- ('IV Antibiotics', 'ER Registration') -> 1 kez gözlenmiş
- ('ER Registration', 'Admission IC') -> 1 kez gözlenmiş
- ('LacticAcid', 'Release E') -> 1 kez gözlenmiş
- ('Admission IC', 'ER Sepsis Triage') -> 1 kez gözlenmiş
- ('LacticAcid', 'ER Registration') -> 1 kez gözlenmiş
- ('Admission NC', 'ER Triage') -> 1 kez gözlenmiş
- ('Release A', 'Leucocytes') -> 1 kez gözlenmiş
- ('Leucocytes', 'Return ER') -> 1 kez gözlenmiş

