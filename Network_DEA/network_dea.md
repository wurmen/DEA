# Network DEA 

*POLab*
<br>
*2017/01/30*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)
<br>
#### ※*Reference*
*本篇主要參考於[高強教授](http://www.iim.ncku.edu.tw/files/11-1407-20368.php?Lang=zh-tw)在2007發表的Paper：[Efficiency decomposition in network data envelopment analysis: A relational model](https://www.sciencedirect.com/science/article/pii/S0377221707010077)*


## (一)前言

常見的DEA再進行效率衡量時，一般會將整個系統(System)視為一整體，並不探討內部各製程(Process)的狀況，但往往會忽略系統內部製程間的效率，就如在建置[CRS Model](https://github.com/wurmen/DEA/blob/master/CRS_Model/CRS%20model.md)所提出的範例般，而高強教授在本篇研究中建構了一個**關聯網絡DEA模型**(Relational network DEA model)，藉由該模型來探討系統內部各製程間的相互關係，並同時衡量系統效率及各製程的效率，通過引入虛擬製程(Dummy processes)，將原始網絡系統轉換為串聯系統，並使串聯中的每個階段都是並行結構，以達到效率分解的目的，透過效率分解，找出導致系統低效運行的製程，以便將來進行改進；**因此在此篇文章中主要是利用paper中的範例及所提出的數學模式來進行說明並利用Python-Gurobi進行建模**

## (二)範例說明
#### ※在此利用paper中第三節所提出的範例進行說明

### § 範例系統架構

- 下圖是一個由三個製程所形成的系統，該系統最初有兩項投入，最終會有三項產出，而系統內部各製程的投入與產出情形，如下圖所示：<br>
1. 系統最初的兩項投入會被分成三個部份分別給製程1、製程2及製程3當成他們各自的投入項。<br>
2. 製程1和製程2的產出會被分成兩個部份，一部份為最終系統產出，另一部份則當成製程3的部份投入項

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/network%20system.PNG" width="550" height="350">
</div>
<br>

- 為了能夠達到效率分解，使各製程的效率能夠被衡量，本研究透過**加入虛擬製程**來將上述系統轉換成一個具有兩個階段(stage)，並且每個階段都是並行結構的系統，如下圖所示：<br>

※ 圖中各個符號表示一併於下面的數學模型進行詳細解釋

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/network%20system1.png" width="750" height="350">
</div>

##### ※在第三節前本篇研究有提出兩個論點(推論過程可詳閱[原文](https://www.sciencedirect.com/science/article/pii/S0377221707010077))
###### 1. 在一個由串聯結構的製程所形成的系統中，各製程的效率乘積等於整體的效率值
###### 2. 在一個由並行結構的製程所形成的系統中，各製程的低效率鬆弛(inefficiency slack)總和等於整體效率的低效率鬆弛
###### 因此在此系統中，整體系統效率值為串聯結構中每個階段效率的乘積，也就是階段1及階段2的效率乘積，而每個階段的低效率鬆弛為並聯結構中，各製程的低效率鬆弛總和，也就是階段1的低效率鬆弛為製程1及製程2的總和，階段2的低效率鬆弛則等於製程3的低效率鬆弛
<br>

### § 決策單位各項產出項與投入項數據

- 共有五個決策單位要進行比較，其系統及各製程的產出與投入情形如下表所示：
<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/example-data.PNG" width="800" height="370">
</div>

## (三)數學模型
上述的系統可形成如下所示的數學模型

### § 符號說明

- E<sub>k</sup></sub>： 決策單位k的效率值
- n： 決策單位(DMU)個數 (在此例中n=5)<br>
- ε： 極小的正值稱之為非阿基米德數(non-Archimedean constant)，通常設為10<sup>-4</sup></sub>或10<sup>-6</sup></sub>(目的為了使任一投入或產出項皆不會被忽略)

### § 參數說明

- X<sub>ij</sup></sub>： 決策單位j (j=1,...,n)的整體系統中，最初的第i (i=1,...,m)個投入項 (在此例中m=2)

- X<sup>(t)</sup></sub><sub>ij</sup></sub>： 決策單位j (j=1,...,n)在製程t的第i個投入項 (在此例中t=1,2,3、i=1,2)

- Y<sup>(O)</sup></sub><sub>1j</sup></sub>、Y<sup>(I)</sup></sub><sub>1j</sup></sub>： 決策單位j (j=1,...,n)製程1的產出項，Y<sup>(O)</sup></sub><sub>1j</sup></sub>為最終的系統產出，Y<sup>(I)</sup></sub><sub>1j</sup></sub>會成為製程3的部份投入項

- Y<sup>(O)</sup></sub><sub>2j</sup></sub>、Y<sup>(I)</sup></sub><sub>2j</sup></sub>： 決策單位j (j=1,...,n)製程1的產出項，Y<sup>(O)</sup></sub><sub>2j</sup></sub>為最終的系統產出，Y<sup>(I)</sup></sub><sub>2j</sup></sub>會成為製程3的部份投入項

- Y<sub>ij</sup></sub>： 決策單位j (j=1,...,n)在製程i的總產出

### § 決策變數
- u<sub>r</sup></sub>： 第r個產出項之權重 (在此例中r=1,2,3)
- v<sub>i</sup></sub>： 第i個投入項之權重 (在此例中i=1,2)

### § 目標式及限制式

此數學模型即為高教授所提出的關聯網絡DEA模型<br>

※該模型是基於CRS Model所延伸(詳請可參閱[原文](https://www.sciencedirect.com/science/article/pii/S0377221707010077))

<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/model1.png" width="550" height="250">

### § 各製程之效率

求解完後，可透過下列的數學式來計算各製程的個別效率值

<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/model2.png" width="450" height="120">

### § 各階段之效率

求解完後，可利用下列的數學式來計算各階段的效率值

<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/model3.png" width="470" height="105">


## (三)Python-Gurobi
在此說明如何運用Python-Gurobi來建構關聯網絡DEA模型
##### ※完整程式碼可點擊[這裡](https://github.com/wurmen/DEA/blob/master/Network_DEA/network_dea_code.py)

### Import gurobipy
```python
from gurobipy import*
```
### Add parameters
- 透過for loop來計算每個決策單位的效率
```python
DMU=['A', 'B','C','D','E']
E={}
val_p1,val_p2,val_p3,val_s1,val_s2={},{},{},{},{}
slack_p1,slack_p2,slack_p3={},{},{}
for k in DMU:

    I=2 # 兩項投入
    O=3 # 三項產出
```
- Totx1、Totx2為各決策單位整體系統的兩項初始投入項數據
```python
    DMU,Totx1,Totx2=multidict({("A"):[11,14],("B"):[7,7],("C"):[11,14],("D"):[14,14],("E"):[14,15]})
```
- 紀錄各製程產出與投入項數據，以製程1為例:<br>
proc1x1：紀錄製程1的第1個投入項數據<br>
proc1x2：紀錄製程1的第2個投入項數據<br>
proc1TotyO：紀錄製程1的總產出數據 (proc1TotyO= proc1yO+Proc1yI)<br>
proc1yO：紀錄製程1總產出中為最終系統產出的數據<br>
Proc1yI：紀錄製程1總產出中將成為製程3投入項的數據<br>
```python
    DMU,proc1x1,proc1x2,proc1TotyO,proc1yO,proc1yI=multidict({("A"):[3,5,4,2,2],("B"):[2,3,2,1,1],("C"):[3,4,2,1,1],("D"):[4,6,3,2,1],("E"):[5,6,4,3,1]})
    DMU,proc2x1,proc2x2,proc2TotyO,proc2yO,proc2yI=multidict({("A"):[4,3,3,2,1],("B"):[2,1,2,1,1],("C"):[5,3,2,1,1],("D"):[5,5,4,3,1],("E"):[5,4,4,2,2]})
    DMU,proc3x1,proc3x2,proc3TotyO=multidict({("A"):[4,6,1],("B"):[3,3,1],("C"):[3,7,2],("D"):[5,3,1],("E"):[4,5,3]})
```
### Model
```python
    m=Model("network_DEA")
```
### Add decision variables
- 建立決策變數投入項與產出項權重 v<sub>i</sup></sub>、 u<sub>r</sup></sub>
```python
    P1,P2,P3={},{},{}
    v,u={},{}
   
    for i in range(I):
        v[i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%d"%i)
    
    for r in range(O):
        u[r]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%d"%i)
```
### Update
```python
    
    m.update()
```
### Add objective
```python
    m.setObjective(u[0]*proc1yO[k]+u[1]*proc2yO[k]+u[2]*proc3TotyO[k],GRB.MAXIMIZE)
```
### Add constraints
```python
    m.addConstr(v[0]*Totx1[k]+v[1]*Totx2[k]==1)
    for j in DMU:
        P1[j]=m.addConstr(u[0]*proc1TotyO[j]-(v[0]*proc1x1[j]+v[1]*proc1x2[j])<=0)
        P2[j]=m.addConstr(u[1]*proc2TotyO[j]-(v[0]*proc2x1[j]+v[1]*proc2x2[j])<=0)
        P3[j]=m.addConstr(u[2]*proc3TotyO[j]-(v[0]*proc3x1[j]+v[1]*proc3x2[j]+u[0]*proc1yI[j]+u[1]*proc2yI[j])<=0)
```
### Print result
```python
    m.optimize()
    E[k]="The efficiency of DMU %s:%4.4g"%(k,m.objVal) #取得決策單位的整體效率值
```
- 取得求得解v<sub>i</sup></sub>、 u<sub>r</sup></sub>的值
```python
    u_sol = m.getAttr('x', u)
    v_sol = m.getAttr('x',v)
```
- 計算各製程的效率值
```python
    
    E1=u_sol[0]*proc1TotyO[k]/(v_sol[0]*proc1x1[k]+v_sol[1]*proc1x2[k]) 
    E2=u_sol[1]*proc2TotyO[k]/(v_sol[0]*proc2x1[k]+v_sol[1]*proc2x2[k])
    E3=u_sol[2]*proc3TotyO[k]/(v_sol[0]*proc3x1[k]+v_sol[1]*proc3x2[k]+u_sol[0]*proc1yI[k]+u_sol[1]*proc2yI[k])
```
- 計算各stage的效率值
```python
    
    stage1=(u_sol[0]*proc1TotyO[k]+u_sol[1]*proc2TotyO[k]+v_sol[0]*proc3x1[k]+v_sol[1]*proc3x2[k])/(v_sol[0]*Totx1[k]+v_sol[1]*Totx2[k])
    stage2=(u_sol[0]*proc1yO[k]+u_sol[1]*proc2yO[k]+u_sol[2]*proc3TotyO[k])/(u_sol[0]*proc1TotyO[k]+u_sol[1]*proc2TotyO[k]+v_sol[0]*proc3x1[k]+v_sol[1]*proc3x2[k])
```
- 紀錄每個決策單位的各製程及各階段的效率值
```python
    val_p1[k]='The efficiency of process 1 of DMU %s:%4.4g'%(k,E1)
    val_p2[k]='The efficiency of process 2 of DMU %s:%4.4g'%(k,E2)
    val_p3[k]='The efficiency of process 3 of DMU %s:%4.4g'%(k,E3)
    val_s1[k]='The efficiency of stage 1 of DMU %s:%4.4g'%(k,stage1)
    val_s2[k]='The efficiency of stage 2 of DMU %s:%4.4g'%(k,stage2)
```
- 利用gurobi中的slack參數，取得各製程的無效率值

```python

    process1_slack=m.getAttr('slack',P1)
    slack_p1[k]='The inefficiency of process 1 of DMU %s:%4.4g'%(k,process1_slack[k])
    process2_slack=m.getAttr('slack',P2)
    slack_p2[k]='The inefficiency of process 2 of DMU %s:%4.4g'%(k,process2_slack[k])
    process3_slack=m.getAttr('slack',P3)
    slack_p3[k]='The inefficiency of process 3 of DMU %s:%4.4g'%(k,process3_slack[k])
```
- 顯示結果

```python
for k in DMU:
    
    print (E[k])
    print (val_p1[k])
    print (val_p2[k])
    print (val_p3[k])
    print (val_s1[k])
    print (val_s2[k])
    print (slack_p1[k])
    print (slack_p2[k])
    print (slack_p3[k])

```

**最後可得到如下所示的結果**<br>

    The efficiency of DMU A:0.5227
    The efficiency of process 1 of DMU A:   1
    The efficiency of process 2 of DMU A:0.75
    The efficiency of process 3 of DMU A:0.3462
    The efficiency of stage 1 of DMU A:0.9091
    The efficiency of stage 2 of DMU A:0.575
    The inefficiency of process 1 of DMU A:   0
    The inefficiency of process 2 of DMU A:0.09091
    The inefficiency of process 3 of DMU A:0.3864
    
    The efficiency of DMU B:0.5952
    The efficiency of process 1 of DMU B:0.8333
    The efficiency of process 2 of DMU B:   1
    The efficiency of process 3 of DMU B:0.5088
    The efficiency of stage 1 of DMU B:0.9286
    The efficiency of stage 2 of DMU B:0.641
    The inefficiency of process 1 of DMU B:0.07143
    The inefficiency of process 2 of DMU B:   0
    The inefficiency of process 3 of DMU B:0.3333
    
    The efficiency of DMU C:0.5682
    The efficiency of process 1 of DMU C: 0.5
    The efficiency of process 2 of DMU C: 0.4
    The efficiency of process 3 of DMU C:0.9474
    The efficiency of stage 1 of DMU C:0.5909
    The efficiency of stage 2 of DMU C:0.9615
    The inefficiency of process 1 of DMU C:0.1364
    The inefficiency of process 2 of DMU C:0.2727
    The inefficiency of process 3 of DMU C:0.02273
    
    The efficiency of DMU D:0.4821
    The efficiency of process 1 of DMU D:0.5625
    The efficiency of process 2 of DMU D: 0.8
    The efficiency of process 3 of DMU D:0.3333
    The efficiency of stage 1 of DMU D:0.8036
    The efficiency of stage 2 of DMU D: 0.6
    The inefficiency of process 1 of DMU D:0.125
    The inefficiency of process 2 of DMU D:0.07143
    The inefficiency of process 3 of DMU D:0.3214
    
    The efficiency of DMU E: 0.8
    The efficiency of process 1 of DMU E:0.8333
    The efficiency of process 2 of DMU E: 0.5
    The efficiency of process 3 of DMU E:   1
    The efficiency of stage 1 of DMU E: 0.8
    The efficiency of stage 2 of DMU E:   1
    The inefficiency of process 1 of DMU E:0.06667
    The inefficiency of process 2 of DMU E:0.1333
    The inefficiency of process 3 of DMU E:   0
    





