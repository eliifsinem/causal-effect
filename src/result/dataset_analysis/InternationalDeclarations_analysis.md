# InternationalDeclarations Analiz Sonuçları

## Log Yükleme
dataset/InternationalDeclarations.xes dosyası başarıyla yüklendi.

## Alpha Miner Sonuçları
Alpha Miner ile süreç modeli oluşturuldu.

(<pm4py.objects.petri.petrinet.PetriNet object at 0x139eae690>, ['start:1'], ['end:1'])

## Heuristic Miner Sonuçları
{'Start trip': (node:Start trip connections:{End trip:[0.9998271391529818]}), 'End trip': (node:End trip connections:{Permit SUBMITTED by EMPLOYEE:[0.9979716024340771], Declaration SUBMITTED by EMPLOYEE:[0.9997822299651568], Declaration SAVED by EMPLOYEE:[0.8717948717948718], Permit REJECTED by MISSING:[0.8333333333333334], Send Reminder:[0.9965397923875432], Permit REJECTED by SUPERVISOR:[0.8333333333333334]}), 'Permit SUBMITTED by EMPLOYEE': (node:Permit SUBMITTED by EMPLOYEE connections:{Permit FINAL_APPROVED by SUPERVISOR:[0.9982817869415808], Permit APPROVED by SUPERVISOR:[0.9942528735632183], Permit APPROVED by PRE_APPROVER:[0.9981203007518797], Permit REJECTED by PRE_APPROVER:[0.9615384615384616], Permit REJECTED by SUPERVISOR:[0.9375], Permit APPROVED by ADMINISTRATION:[0.9997929606625259], Permit REJECTED by ADMINISTRATION:[0.9880952380952381]}), 'Declaration SUBMITTED by EMPLOYEE': (node:Declaration SUBMITTED by EMPLOYEE connections:{Declaration FINAL_APPROVED by SUPERVISOR:[0.9985775248933144], Declaration APPROVED by PRE_APPROVER:[0.9983471074380166], Declaration APPROVED by ADMINISTRATION:[0.9997981021603068], Declaration REJECTED by PRE_APPROVER:[0.9878048780487805], Permit REJECTED by MISSING:[0.5], Declaration REJECTED by SUPERVISOR:[0.9285714285714286], Declaration APPROVED by SUPERVISOR:[0.9887640449438202], Declaration REJECTED by ADMINISTRATION:[0.9993412384716732]}), 'Declaration SAVED by EMPLOYEE': (node:Declaration SAVED by EMPLOYEE connections:{Start trip:[0.9411764705882353], Permit REJECTED by MISSING:[0.75]}), 'Permit REJECTED by MISSING': (node:Permit REJECTED by MISSING connections:{Permit SUBMITTED by EMPLOYEE:[0.9473684210526315], Payment Handled:[0.9090909090909091]}), 'Send Reminder': (node:Send Reminder connections:{Send Reminder:[0.9655172413793104], Declaration SUBMITTED by EMPLOYEE:[0.9973614775725593], Declaration SAVED by EMPLOYEE:[0.9333333333333333]}), 'Permit REJECTED by SUPERVISOR': (node:Permit REJECTED by SUPERVISOR connections:{Permit REJECTED by EMPLOYEE:[0.9885057471264368]}), 'Permit FINAL_APPROVED by SUPERVISOR': (node:Permit FINAL_APPROVED by SUPERVISOR connections:{Declaration SUBMITTED by EMPLOYEE:[0.9987129987129987], Start trip:[0.9997623009270263], End trip:[0.9963768115942029], Permit REJECTED by MISSING:[0.9090909090909091], Send Reminder:[0.9901960784313726], Declaration SAVED by EMPLOYEE:[0.9166666666666666]}), 'Permit APPROVED by SUPERVISOR': (node:Permit APPROVED by SUPERVISOR connections:{Permit FINAL_APPROVED by DIRECTOR:[0.9983633387888707], Permit REJECTED by DIRECTOR:[0.5]}), 'Permit APPROVED by PRE_APPROVER': (node:Permit APPROVED by PRE_APPROVER connections:{Permit FINAL_APPROVED by SUPERVISOR:[0.997920997920998], Permit REJECTED by SUPERVISOR:[0.875]}), 'Permit REJECTED by PRE_APPROVER': (node:Permit REJECTED by PRE_APPROVER connections:{Permit REJECTED by EMPLOYEE:[0.9615384615384616]}), 'Permit APPROVED by ADMINISTRATION': (node:Permit APPROVED by ADMINISTRATION connections:{Permit FINAL_APPROVED by SUPERVISOR:[0.999609984399376], Permit APPROVED by BUDGET OWNER:[0.9994022713687986], Permit REJECTED by BUDGET OWNER:[0.967741935483871], Permit APPROVED by SUPERVISOR:[0.9959183673469387], Permit REJECTED by SUPERVISOR:[0.9795918367346939], Start trip:[0.996]}), 'Permit REJECTED by ADMINISTRATION': (node:Permit REJECTED by ADMINISTRATION connections:{Permit REJECTED by EMPLOYEE:[0.9876543209876543]}), 'Declaration FINAL_APPROVED by SUPERVISOR': (node:Declaration FINAL_APPROVED by SUPERVISOR connections:{Request Payment:[0.9998310525426592], Declaration REJECTED by MISSING:[0.9893617021276596]}), 'Declaration APPROVED by PRE_APPROVER': (node:Declaration APPROVED by PRE_APPROVER connections:{Declaration FINAL_APPROVED by SUPERVISOR:[0.9982847341337907], Declaration REJECTED by SUPERVISOR:[0.9375]}), 'Declaration APPROVED by ADMINISTRATION': (node:Declaration APPROVED by ADMINISTRATION connections:{Declaration FINAL_APPROVED by SUPERVISOR:[0.9996621621621622], Declaration APPROVED by BUDGET OWNER:[0.9994493392070485], Declaration APPROVED by SUPERVISOR:[0.9903846153846154], Declaration REJECTED by BUDGET OWNER:[0.975609756097561], Declaration REJECTED by SUPERVISOR:[0.9861111111111112], Permit REJECTED by MISSING:[0.5]}), 'Declaration REJECTED by PRE_APPROVER': (node:Declaration REJECTED by PRE_APPROVER connections:{Declaration REJECTED by EMPLOYEE:[0.9879518072289156], Permit REJECTED by MISSING:[0.5]}), 'Declaration REJECTED by SUPERVISOR': (node:Declaration REJECTED by SUPERVISOR connections:{Declaration REJECTED by EMPLOYEE:[0.9917355371900827]}), 'Declaration APPROVED by SUPERVISOR': (node:Declaration APPROVED by SUPERVISOR connections:{Declaration FINAL_APPROVED by DIRECTOR:[0.996], Declaration REJECTED by DIRECTOR:[0.8]}), 'Declaration REJECTED by ADMINISTRATION': (node:Declaration REJECTED by ADMINISTRATION connections:{Declaration REJECTED by EMPLOYEE:[0.99933818663137]}), 'Request Payment': (node:Request Payment connections:{Payment Handled:[0.9998373983739838], Permit REJECTED by MISSING:[0.5]}), 'Declaration REJECTED by MISSING': (node:Declaration REJECTED by MISSING connections:{Declaration SUBMITTED by EMPLOYEE:[0.9885057471264368], Permit REJECTED by MISSING:[0.6666666666666666]}), 'Payment Handled': (node:Payment Handled connections:{Start trip:[0.9975961538461539]}), 'Permit FINAL_APPROVED by DIRECTOR': (node:Permit FINAL_APPROVED by DIRECTOR connections:{Declaration SUBMITTED by EMPLOYEE:[0.9895833333333334], End trip:[0.9743589743589743], Start trip:[0.9979757085020243], Declaration SAVED by EMPLOYEE:[0.8], Permit REJECTED by MISSING:[0.8]}), 'Permit REJECTED by DIRECTOR': (node:Permit REJECTED by DIRECTOR connections:{Permit REJECTED by EMPLOYEE:[0.5]}), 'Declaration APPROVED by BUDGET OWNER': (node:Declaration APPROVED by BUDGET OWNER connections:{Declaration FINAL_APPROVED by SUPERVISOR:[0.9994275901545506], Declaration APPROVED by SUPERVISOR:[0.9807692307692307], Declaration REJECTED by SUPERVISOR:[0.9629629629629629]}), 'Declaration REJECTED by BUDGET OWNER': (node:Declaration REJECTED by BUDGET OWNER connections:{Declaration REJECTED by EMPLOYEE:[0.975]}), 'Declaration REJECTED by EMPLOYEE': (node:Declaration REJECTED by EMPLOYEE connections:{Declaration SUBMITTED by EMPLOYEE:[0.9993757802746567]}), 'Declaration FINAL_APPROVED by DIRECTOR': (node:Declaration FINAL_APPROVED by DIRECTOR connections:{Request Payment:[0.995850622406639], Declaration REJECTED by MISSING:[0.9]}), 'Declaration REJECTED by DIRECTOR': (node:Declaration REJECTED by DIRECTOR connections:{Declaration REJECTED by EMPLOYEE:[0.8]}), 'Permit REJECTED by EMPLOYEE': (node:Permit REJECTED by EMPLOYEE connections:{Permit SUBMITTED by EMPLOYEE:[0.9955357142857143]}), 'Permit APPROVED by BUDGET OWNER': (node:Permit APPROVED by BUDGET OWNER connections:{Permit FINAL_APPROVED by SUPERVISOR:[0.9992937853107344], Permit REJECTED by SUPERVISOR:[0.9375], Permit APPROVED by SUPERVISOR:[0.9947916666666666], Start trip:[0.9900990099009901]}), 'Permit REJECTED by BUDGET OWNER': (node:Permit REJECTED by BUDGET OWNER connections:{Permit REJECTED by EMPLOYEE:[0.96875]})}

Heuristic Miner ile heuristik ağ (heu_net) elde edildi.

## Directly Follows Graph (DFG)
Directly Follows Graph elde edildi.

### Start Activities:
- Start trip: 740
- Declaration SUBMITTED by EMPLOYEE: 407
- Permit SUBMITTED by EMPLOYEE: 5294
- Declaration SAVED by EMPLOYEE: 8

### End Activities:
- Payment Handled: 5646
- End trip: 593
- Declaration SAVED by EMPLOYEE: 54
- Permit REJECTED by MISSING: 8
- Declaration REJECTED by MISSING: 11
- Declaration REJECTED by EMPLOYEE: 130
- Declaration FINAL_APPROVED by SUPERVISOR: 1
- Send Reminder: 2
- Request Payment: 3
- Declaration REJECTED by SUPERVISOR: 1

### DFG Kenarları:
- ('Start trip', 'End trip') -> 5784 kez gözlenmiş
- ('End trip', 'Permit SUBMITTED by EMPLOYEE') -> 492 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit FINAL_APPROVED by SUPERVISOR') -> 581 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Declaration SUBMITTED by EMPLOYEE') -> 776 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 702 kez gözlenmiş
- ('Declaration FINAL_APPROVED by SUPERVISOR', 'Request Payment') -> 5918 kez gözlenmiş
- ('Request Payment', 'Payment Handled') -> 6149 kez gözlenmiş
- ('Start trip', 'Permit SUBMITTED by EMPLOYEE') -> 225 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit APPROVED by SUPERVISOR') -> 173 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Permit FINAL_APPROVED by DIRECTOR') -> 610 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Declaration SUBMITTED by EMPLOYEE') -> 95 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration APPROVED by PRE_APPROVER') -> 604 kez gözlenmiş
- ('Declaration APPROVED by PRE_APPROVER', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 582 kez gözlenmiş
- ('Payment Handled', 'End trip') -> 121 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'End trip') -> 38 kez gözlenmiş
- ('End trip', 'Declaration SUBMITTED by EMPLOYEE') -> 4591 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration APPROVED by ADMINISTRATION') -> 4952 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 2959 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit APPROVED by PRE_APPROVER') -> 531 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'Permit FINAL_APPROVED by SUPERVISOR') -> 480 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration REJECTED by PRE_APPROVER') -> 81 kez gözlenmiş
- ('Declaration REJECTED by PRE_APPROVER', 'Declaration REJECTED by EMPLOYEE') -> 82 kez gözlenmiş
- ('Declaration REJECTED by EMPLOYEE', 'Declaration SUBMITTED by EMPLOYEE') -> 1601 kez gözlenmiş
- ('Payment Handled', 'Start trip') -> 415 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Start trip') -> 4206 kez gözlenmiş
- ('End trip', 'Declaration SAVED by EMPLOYEE') -> 36 kez gözlenmiş
- ('Declaration FINAL_APPROVED by SUPERVISOR', 'Declaration REJECTED by MISSING') -> 93 kez gözlenmiş
- ('Declaration REJECTED by MISSING', 'Declaration SUBMITTED by EMPLOYEE') -> 86 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Start trip') -> 493 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Permit REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Permit REJECTED by MISSING', 'Permit SUBMITTED by EMPLOYEE') -> 18 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Declaration APPROVED by PRE_APPROVER') -> 1 kez gözlenmiş
- ('End trip', 'Permit REJECTED by MISSING') -> 5 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration REJECTED by SUPERVISOR') -> 13 kez gözlenmiş
- ('Declaration REJECTED by SUPERVISOR', 'Declaration REJECTED by EMPLOYEE') -> 120 kez gözlenmiş
- ('Declaration SAVED by EMPLOYEE', 'Start trip') -> 16 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Start trip') -> 28 kez gözlenmiş
- ('End trip', 'Permit FINAL_APPROVED by DIRECTOR') -> 8 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration APPROVED by SUPERVISOR') -> 88 kez gözlenmiş
- ('Declaration APPROVED by SUPERVISOR', 'Declaration FINAL_APPROVED by DIRECTOR') -> 249 kez gözlenmiş
- ('Declaration FINAL_APPROVED by DIRECTOR', 'Request Payment') -> 240 kez gözlenmiş
- ('Declaration APPROVED by PRE_APPROVER', 'Declaration APPROVED by SUPERVISOR') -> 10 kez gözlenmiş
- ('Declaration FINAL_APPROVED by DIRECTOR', 'Declaration REJECTED by MISSING') -> 9 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit REJECTED by PRE_APPROVER') -> 25 kez gözlenmiş
- ('Permit REJECTED by PRE_APPROVER', 'Permit REJECTED by EMPLOYEE') -> 25 kez gözlenmiş
- ('Permit REJECTED by EMPLOYEE', 'Permit SUBMITTED by EMPLOYEE') -> 223 kez gözlenmiş
- ('Declaration APPROVED by PRE_APPROVER', 'Declaration REJECTED by SUPERVISOR') -> 15 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'End trip') -> 275 kez gözlenmiş
- ('Declaration APPROVED by SUPERVISOR', 'Declaration REJECTED by DIRECTOR') -> 4 kez gözlenmiş
- ('Declaration REJECTED by DIRECTOR', 'Declaration REJECTED by EMPLOYEE') -> 4 kez gözlenmiş
- ('Start trip', 'Permit FINAL_APPROVED by DIRECTOR') -> 19 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit REJECTED by SUPERVISOR') -> 15 kez gözlenmiş
- ('Permit REJECTED by SUPERVISOR', 'Permit REJECTED by EMPLOYEE') -> 86 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Permit REJECTED by MISSING') -> 10 kez gözlenmiş
- ('Permit REJECTED by MISSING', 'Start trip') -> 2 kez gözlenmiş
- ('Start trip', 'Declaration SUBMITTED by EMPLOYEE') -> 138 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'End trip') -> 57 kez gözlenmiş
- ('End trip', 'Declaration APPROVED by PRE_APPROVER') -> 7 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit APPROVED by ADMINISTRATION') -> 4829 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit FINAL_APPROVED by SUPERVISOR') -> 2563 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Send Reminder') -> 101 kez gözlenmiş
- ('Send Reminder', 'Send Reminder') -> 28 kez gözlenmiş
- ('Send Reminder', 'Declaration SUBMITTED by EMPLOYEE') -> 378 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'Start trip') -> 26 kez gözlenmiş
- ('Start trip', 'Permit FINAL_APPROVED by SUPERVISOR') -> 176 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Permit APPROVED by PRE_APPROVER') -> 1 kez gözlenmiş
- ('Request Payment', 'End trip') -> 13 kez gözlenmiş
- ('End trip', 'Payment Handled') -> 15 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'Permit APPROVED by SUPERVISOR') -> 16 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Start trip') -> 15 kez gözlenmiş
- ('Declaration REJECTED by MISSING', 'Start trip') -> 3 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Declaration SAVED by EMPLOYEE') -> 4 kez gözlenmiş
- ('Declaration SAVED by EMPLOYEE', 'Permit REJECTED by MISSING') -> 3 kez gözlenmiş
- ('Declaration REJECTED by SUPERVISOR', 'Declaration SUBMITTED by EMPLOYEE') -> 3 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Start trip') -> 78 kez gözlenmiş
- ('End trip', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 43 kez gözlenmiş
- ('End trip', 'Permit FINAL_APPROVED by SUPERVISOR') -> 156 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'Permit REJECTED by SUPERVISOR') -> 7 kez gözlenmiş
- ('Declaration FINAL_APPROVED by SUPERVISOR', 'End trip') -> 10 kez gözlenmiş
- ('End trip', 'Request Payment') -> 12 kez gözlenmiş
- ('Declaration REJECTED by MISSING', 'End trip') -> 1 kez gözlenmiş
- ('Declaration REJECTED by MISSING', 'Permit REJECTED by MISSING') -> 2 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Declaration APPROVED by BUDGET OWNER') -> 1815 kez gözlenmiş
- ('Declaration APPROVED by BUDGET OWNER', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 1746 kez gözlenmiş
- ('Request Payment', 'Start trip') -> 8 kez gözlenmiş
- ('Start trip', 'Payment Handled') -> 8 kez gözlenmiş
- ('End trip', 'Permit APPROVED by PRE_APPROVER') -> 2 kez gözlenmiş
- ('Declaration FINAL_APPROVED by SUPERVISOR', 'Permit REJECTED by MISSING') -> 3 kez gözlenmiş
- ('Permit REJECTED by MISSING', 'Request Payment') -> 3 kez gözlenmiş
- ('Declaration REJECTED by EMPLOYEE', 'Start trip') -> 36 kez gözlenmiş
- ('End trip', 'Declaration REJECTED by PRE_APPROVER') -> 2 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration FINAL_APPROVED by DIRECTOR') -> 1 kez gözlenmiş
- ('Declaration FINAL_APPROVED by DIRECTOR', 'Declaration APPROVED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Declaration APPROVED by SUPERVISOR', 'Request Payment') -> 3 kez gözlenmiş
- ('End trip', 'Declaration REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Start trip', 'Declaration REJECTED by PRE_APPROVER') -> 1 kez gözlenmiş
- ('Declaration REJECTED by PRE_APPROVER', 'End trip') -> 1 kez gözlenmiş
- ('End trip', 'Declaration REJECTED by EMPLOYEE') -> 16 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'End trip') -> 4 kez gözlenmiş
- ('Permit REJECTED by SUPERVISOR', 'Start trip') -> 3 kez gözlenmiş
- ('Start trip', 'Permit REJECTED by EMPLOYEE') -> 3 kez gözlenmiş
- ('Declaration APPROVED by PRE_APPROVER', 'Declaration FINAL_APPROVED by DIRECTOR') -> 2 kez gözlenmiş
- ('Permit REJECTED by EMPLOYEE', 'Start trip') -> 6 kez gözlenmiş
- ('Declaration APPROVED by PRE_APPROVER', 'End trip') -> 2 kez gözlenmiş
- ('Declaration REJECTED by PRE_APPROVER', 'Permit REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Permit REJECTED by MISSING', 'Declaration REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Permit REJECTED by MISSING') -> 4 kez gözlenmiş
- ('Start trip', 'Permit REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Declaration APPROVED by PRE_APPROVER', 'Start trip') -> 1 kez gözlenmiş
- ('Start trip', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 6 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Declaration APPROVED by SUPERVISOR') -> 103 kez gözlenmiş
- ('Request Payment', 'Permit REJECTED by MISSING') -> 10 kez gözlenmiş
- ('Permit REJECTED by MISSING', 'Payment Handled') -> 10 kez gözlenmiş
- ('Declaration REJECTED by EMPLOYEE', 'Permit REJECTED by MISSING') -> 2 kez gözlenmiş
- ('Start trip', 'Permit APPROVED by SUPERVISOR') -> 12 kez gözlenmiş
- ('Start trip', 'Declaration REJECTED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Declaration REJECTED by SUPERVISOR', 'End trip') -> 2 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration REJECTED by ADMINISTRATION') -> 1517 kez gözlenmiş
- ('Declaration REJECTED by ADMINISTRATION', 'Declaration REJECTED by EMPLOYEE') -> 1510 kez gözlenmiş
- ('End trip', 'Send Reminder') -> 288 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit APPROVED by BUDGET OWNER') -> 1672 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Permit FINAL_APPROVED by SUPERVISOR') -> 1415 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'End trip') -> 36 kez gözlenmiş
- ('End trip', 'Permit REJECTED by SUPERVISOR') -> 5 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Permit REJECTED by SUPERVISOR') -> 15 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit REJECTED by ADMINISTRATION') -> 83 kez gözlenmiş
- ('Permit REJECTED by ADMINISTRATION', 'Permit REJECTED by EMPLOYEE') -> 80 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Declaration REJECTED by BUDGET OWNER') -> 40 kez gözlenmiş
- ('Declaration REJECTED by BUDGET OWNER', 'Declaration REJECTED by EMPLOYEE') -> 39 kez gözlenmiş
- ('Declaration APPROVED by BUDGET OWNER', 'Declaration APPROVED by SUPERVISOR') -> 51 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Send Reminder') -> 4 kez gözlenmiş
- ('Send Reminder', 'Permit FINAL_APPROVED by SUPERVISOR') -> 10 kez gözlenmiş
- ('Permit REJECTED by SUPERVISOR', 'End trip') -> 2 kez gözlenmiş
- ('End trip', 'Permit REJECTED by EMPLOYEE') -> 3 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit REJECTED by BUDGET OWNER') -> 30 kez gözlenmiş
- ('Permit REJECTED by BUDGET OWNER', 'Permit REJECTED by EMPLOYEE') -> 31 kez gözlenmiş
- ('Declaration REJECTED by ADMINISTRATION', 'Declaration SUBMITTED by EMPLOYEE') -> 24 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit APPROVED by SUPERVISOR') -> 244 kez gözlenmiş
- ('End trip', 'Declaration APPROVED by ADMINISTRATION') -> 81 kez gözlenmiş
- ('Send Reminder', 'Declaration SAVED by EMPLOYEE') -> 14 kez gözlenmiş
- ('End trip', 'Declaration REJECTED by ADMINISTRATION') -> 29 kez gözlenmiş
- ('Declaration APPROVED by BUDGET OWNER', 'End trip') -> 8 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Declaration REJECTED by SUPERVISOR') -> 71 kez gözlenmiş
- ('Permit APPROVED by PRE_APPROVER', 'Permit FINAL_APPROVED by DIRECTOR') -> 1 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Permit APPROVED by SUPERVISOR') -> 3 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'End trip') -> 43 kez gözlenmiş
- ('End trip', 'Declaration APPROVED by BUDGET OWNER') -> 18 kez gözlenmiş
- ('End trip', 'Permit APPROVED by ADMINISTRATION') -> 7 kez gözlenmiş
- ('Permit FINAL_APPROVED by DIRECTOR', 'Send Reminder') -> 3 kez gözlenmiş
- ('Declaration APPROVED by BUDGET OWNER', 'Declaration REJECTED by SUPERVISOR') -> 26 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Permit REJECTED by SUPERVISOR') -> 48 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Send Reminder') -> 8 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Permit APPROVED by SUPERVISOR') -> 191 kez gözlenmiş
- ('Declaration REJECTED by EMPLOYEE', 'End trip') -> 10 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'End trip') -> 1 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Start trip') -> 100 kez gözlenmiş
- ('Declaration REJECTED by ADMINISTRATION', 'End trip') -> 9 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'Start trip') -> 249 kez gözlenmiş
- ('End trip', 'Permit APPROVED by BUDGET OWNER') -> 35 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Permit REJECTED by MISSING') -> 1 kez gözlenmiş
- ('Permit REJECTED by MISSING', 'Declaration FINAL_APPROVED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Permit APPROVED by ADMINISTRATION', 'End trip') -> 25 kez gözlenmiş
- ('Start trip', 'Permit APPROVED by ADMINISTRATION') -> 3 kez gözlenmiş
- ('Declaration SAVED by EMPLOYEE', 'End trip') -> 2 kez gözlenmiş
- ('Declaration REJECTED by ADMINISTRATION', 'Start trip') -> 6 kez gözlenmiş
- ('Declaration FINAL_APPROVED by SUPERVISOR', 'Payment Handled') -> 5 kez gözlenmiş
- ('Declaration APPROVED by ADMINISTRATION', 'Start trip') -> 5 kez gözlenmiş
- ('Start trip', 'Permit APPROVED by BUDGET OWNER') -> 54 kez gözlenmiş
- ('Permit FINAL_APPROVED by SUPERVISOR', 'Declaration SAVED by EMPLOYEE') -> 11 kez gözlenmiş
- ('Permit APPROVED by BUDGET OWNER', 'Permit FINAL_APPROVED by DIRECTOR') -> 2 kez gözlenmiş
- ('Declaration SUBMITTED by EMPLOYEE', 'Declaration REJECTED by EMPLOYEE') -> 5 kez gözlenmiş
- ('Payment Handled', 'Send Reminder') -> 2 kez gözlenmiş
- ('Declaration FINAL_APPROVED by SUPERVISOR', 'Start trip') -> 9 kez gözlenmiş
- ('Payment Handled', 'Request Payment') -> 3 kez gözlenmiş
- ('Declaration REJECTED by EMPLOYEE', 'Declaration SAVED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Start trip', 'Request Payment') -> 4 kez gözlenmiş
- ('Declaration APPROVED by BUDGET OWNER', 'Start trip') -> 3 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'End trip') -> 2 kez gözlenmiş
- ('Permit REJECTED by EMPLOYEE', 'End trip') -> 2 kez gözlenmiş
- ('Start trip', 'Declaration REJECTED by ADMINISTRATION') -> 3 kez gözlenmiş
- ('Start trip', 'Declaration APPROVED by ADMINISTRATION') -> 4 kez gözlenmiş
- ('Start trip', 'Declaration APPROVED by BUDGET OWNER') -> 1 kez gözlenmiş
- ('End trip', 'Permit APPROVED by SUPERVISOR') -> 2 kez gözlenmiş
- ('Start trip', 'Declaration REJECTED by EMPLOYEE') -> 3 kez gözlenmiş
- ('Send Reminder', 'Permit APPROVED by BUDGET OWNER') -> 2 kez gözlenmiş
- ('Declaration REJECTED by BUDGET OWNER', 'End trip') -> 1 kez gözlenmiş
- ('Permit REJECTED by SUPERVISOR', 'Permit SUBMITTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Start trip', 'Permit REJECTED by SUPERVISOR') -> 2 kez gözlenmiş
- ('Permit REJECTED by ADMINISTRATION', 'Start trip') -> 1 kez gözlenmiş
- ('End trip', 'Declaration APPROVED by SUPERVISOR') -> 1 kez gözlenmiş
- ('Permit REJECTED by ADMINISTRATION', 'Permit SUBMITTED by EMPLOYEE') -> 2 kez gözlenmiş
- ('Permit SUBMITTED by EMPLOYEE', 'Permit REJECTED by EMPLOYEE') -> 2 kez gözlenmiş
- ('Permit APPROVED by SUPERVISOR', 'Permit REJECTED by DIRECTOR') -> 1 kez gözlenmiş
- ('Permit REJECTED by DIRECTOR', 'Permit REJECTED by EMPLOYEE') -> 1 kez gözlenmiş
- ('Start trip', 'Declaration SAVED by EMPLOYEE') -> 1 kez gözlenmiş
- ('End trip', 'Permit REJECTED by BUDGET OWNER') -> 1 kez gözlenmiş

