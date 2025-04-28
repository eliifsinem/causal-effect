# DomesticDeclarations Analiz Sonuçları

## Log Yükleme
dataset/DomesticDeclarations.xes dosyası başarıyla yüklendi.

## Alpha Miner Sonuçları
Alpha Miner ile süreç modeli oluşturuldu.

(<pm4py.objects.petri.petrinet.PetriNet object at 0x129cb3610>, ['start:1'], ['end:1'])

## Heuristic Miner Sonuçları
{'Declaration SUBMITTED by EMPLOYEE': (node:Declaration SUBMITTED by EMPLOYEE connections:{Declaration FINAL_APPROVED by SUPERVISOR:[0.9993493819128172], Declaration APPROVED by PRE_APPROVER:[0.9985422740524781], Declaration REJECTED by PRE_APPROVER:[0.9885057471264368], Declaration REJECTED by SUPERVISOR:[0.9836065573770492], Declaration APPROVED by ADMINISTRATION:[0.9998780933804705], Declaration FOR_APPROVAL by SUPERVISOR:[0.5], Declaration REJECTED by ADMINISTRATION:[0.9989506820566632], Declaration FOR_APPROVAL by PRE_APPROVER:[0.5], Declaration FOR_APPROVAL by ADMINISTRATION:[0]}), 'Declaration FINAL_APPROVED by SUPERVISOR': (node:Declaration FINAL_APPROVED by SUPERVISOR connections:{Request Payment:[0.9999003884849088], Declaration REJECTED by MISSING:[0.9885057471264368]}), 'Declaration APPROVED by PRE_APPROVER': (node:Declaration APPROVED by PRE_APPROVER connections:{Declaration FINAL_APPROVED by SUPERVISOR:[0.9985185185185185]}), 'Declaration REJECTED by PRE_APPROVER': (node:Declaration REJECTED by PRE_APPROVER connections:{Declaration REJECTED by EMPLOYEE:[0.9883720930232558]}), 'Declaration REJECTED by SUPERVISOR': (node:Declaration REJECTED by SUPERVISOR connections:{Declaration REJECTED by EMPLOYEE:[0.9965156794425087]}), 'Declaration APPROVED by ADMINISTRATION': (node:Declaration APPROVED by ADMINISTRATION connections:{Declaration APPROVED by BUDGET OWNER:[0.9996455157745481], Declaration FINAL_APPROVED by SUPERVISOR:[0.9998052201012856], Declaration REJECTED by SUPERVISOR:[0.9947643979057592], Declaration REJECTED by BUDGET OWNER:[0.9833333333333333]}), 'Declaration FOR_APPROVAL by SUPERVISOR': (node:Declaration FOR_APPROVAL by SUPERVISOR connections:{Declaration REJECTED by MISSING:[0.5]}), 'Declaration REJECTED by ADMINISTRATION': (node:Declaration REJECTED by ADMINISTRATION connections:{Declaration REJECTED by EMPLOYEE:[0.9989235737351991]}), 'Declaration FOR_APPROVAL by PRE_APPROVER': (node:Declaration FOR_APPROVAL by PRE_APPROVER connections:{Declaration REJECTED by MISSING:[0.5]}), 'Request Payment': (node:Request Payment connections:{Payment Handled:[0.9999003785614664]}), 'Declaration REJECTED by MISSING': (node:Declaration REJECTED by MISSING connections:{Declaration SUBMITTED by EMPLOYEE:[0.9838709677419355]}), 'Payment Handled': (node:Payment Handled connections:{}), 'Declaration REJECTED by EMPLOYEE': (node:Declaration REJECTED by EMPLOYEE connections:{Declaration SUBMITTED by EMPLOYEE:[0.9990757855822551]}), 'Declaration APPROVED by BUDGET OWNER': (node:Declaration APPROVED by BUDGET OWNER connections:{Declaration FINAL_APPROVED by SUPERVISOR:[0.9996414485478666], Declaration REJECTED by SUPERVISOR:[0.9696969696969697]}), 'Declaration REJECTED by BUDGET OWNER': (node:Declaration REJECTED by BUDGET OWNER connections:{Declaration REJECTED by EMPLOYEE:[0.9830508474576272]}), 'Declaration SAVED by EMPLOYEE': (node:Declaration SAVED by EMPLOYEE connections:{Request Payment:[0.5]}), 'Declaration FOR_APPROVAL by ADMINISTRATION': (node:Declaration FOR_APPROVAL by ADMINISTRATION connections:{Declaration SUBMITTED by EMPLOYEE:[0]})}

Heuristic Miner ile heuristik ağ (heu_net) elde edildi.

## Directly Follows Graph (DFG)
Directly Follows Graph elde edildi.

### Start Activities:
- Declaration SUBMITTED by EMPLOYEE: 10365
- Declaration SAVED by EMPLOYEE: 135

### End Activities:
- Payment Handled: 10043
- Declaration SAVED by EMPLOYEE: 134
- Declaration REJECTED by MISSING: 30
- Declaration REJECTED by EMPLOYEE: 284
- Declaration REJECTED by ADMINISTRATION: 5
- Declaration REJECTED by SUPERVISOR: 4

### DFG Kenarları:
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 1536 kez gözlenmiş
- ('Declaration FINAL_APPROVED by SUPERVISOR', 'Request Payment') -> 10038 kez gözlenmiş
- ('Request Payment', 'Payment Handled') -> 10037 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration APPROVED by PRE_APPROVER') -> 685 kez gözlenmiş
- ('Declaration APPROVED by PRE_APPROVER', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 674 kez gözlenmiş
- ('Declaration FINAL_APPROVED by SUPERVISOR', 'Declaration REJECTED by MISSING') -> 86 kez gözlenmiş
- ('Declaration REJECTED by MISSING', 'Declaration SUBMITTED by EMPLOYEE') -> 61 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration REJECTED by PRE_APPROVER') -> 86 kez gözlenmiş
- ('Declaration REJECTED by PRE_APPROVER', 'Declaration REJECTED by EMPLOYEE') -> 85 kez gözlenmiş
- ('Declaration REJECTED by EMPLOYEE', 'Declaration SUBMITTED by EMPLOYEE') -> 1081 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration REJECTED by SUPERVISOR') -> 60 kez gözlenmiş
- ('Declaration REJECTED by SUPERVISOR', 'Declaration REJECTED by EMPLOYEE') -> 286 kez gözlenmiş
- ('Declaration REJECTED by PRE_APPROVER', 'Declaration SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration REJECTED by EMPLOYEE') -> 7 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration APPROVED by ADMINISTRATION') -> 8202 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Declaration APPROVED by BUDGET OWNER') -> 2820 kez gözlenmiş
- ('Declaration APPROVED by BUDGET OWNER', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 2788 kez gözlenmiş
- ('Declaration APPROVED by PRE_APPROVER', 'Declaration REJECTED by SUPERVISOR') -> 11 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration FOR_APPROVAL by SUPERVISOR') -> 1 kez gözlenmiş
- ('Declaration FOR_APPROVAL by SUPERVISOR', 'Declaration REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Declaration SAVED by EMPLOYEE', 'Request Payment') -> 1 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 5133 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration REJECTED by ADMINISTRATION') -> 952 kez gözlenmiş
- ('Declaration REJECTED by ADMINISTRATION', 'Declaration REJECTED by EMPLOYEE') -> 928 kez gözlenmiş
- ('Request Payment', 'Declaration REJECTED by MISSING') -> 3 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration FOR_APPROVAL by PRE_APPROVER') -> 1 kez gözlenmiş
- ('Declaration FOR_APPROVAL by PRE_APPROVER', 'Declaration REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Declaration REJECTED by SUPERVISOR', 'Request Payment') -> 1 kez gözlenmiş
- ('Payment Handled', 'Declaration REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Declaration REJECTED by SUPERVISOR') -> 190 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Declaration REJECTED by BUDGET OWNER') -> 59 kez gözlenmiş
- ('Declaration REJECTED by BUDGET OWNER', 'Declaration REJECTED by EMPLOYEE') -> 58 kez gözlenmiş
- ('Declaration APPROVED by BUDGET OWNER', 'Declaration REJECTED by SUPERVISOR') -> 32 kez gözlenmiş
- ('Declaration REJECTED by ADMINISTRATION', 'Declaration SUBMITTED by EMPLOYEE') -> 19 kez gözlenmiş
- ('Declaration REJECTED by BUDGET OWNER', 'Declaration SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration FOR_APPROVAL by ADMINISTRATION') -> 1 kez gözlenmiş
- ('Declaration FOR_APPROVAL by ADMINISTRATION', 'Declaration SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Declaration FINAL_APPROVED by SUPERVISOR', 'Payment Handled') -> 7 kez gözlenmiş
- ('Declaration REJECTED by SUPERVISOR', 'Declaration SUBMITTED by EMPLOYEE') -> 2 kez gözlenmiş

