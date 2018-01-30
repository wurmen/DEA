# CRS Model  

*POLab*
<br>
*2017/01/29*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)
<br>
#### ※*Reference*
*本篇範例資料取自高強教授於2007發表的Paper：[Efficiency decomposition in network data envelopment analysis: A relational model](https://www.sciencedirect.com/science/article/pii/S0377221707010077)*


## (一)CRS Model
**※此為DEA中固定規模報酬(constant return to scale, CRS)的模型建構說明，並以投入導向的模組為例**<br>
<br>
固定規模報酬是指每一單位的投入可得到的產出量是固定的，並不會因為規模大小而改變，也就是說當投入量以等比例增加時，產出亦會以等比例增加，並在固定規模報酬的假設下，藉由將各決策單位(Decision Making Unit, DMU)的各項投入加權組合與各項產出加權組合互相比較計算其比值，以得出各個決策單位的效率值，且效率值介於0到1之間；投入導向指的是在相同產出水準下，比較各決策單位投入資源的使用效率。<br>

### § 符號說明
- h<sub>k</sup></sub>： 決策單位k的效率值
- n： 決策單位(DMU)個數<br>
- m： 投入項個數<br>
- s： 產出項個數<br>
- ε： 極小的正值稱之為非阿基米德數(non-Archimedean constant)，通常設為E-4或E-6(目的為了使任一投入或產出項皆不會被忽略)
### § 參數說明
- X<sub>ij</sup></sub>： 決策單位j (j=1,...,n)使用第i (i=1,...,m)個投入項
- Y<sub>rj</sup></sub>： 決策單位j (j=1,...,n)使用第r (r=1,...,s)個產出項
### § 決策變數
- u<sub>r</sup></sub>： 第r個產出項之權重
- v<sub>i</sup></sub>： 第i個投入項之權重
### § CRS Model
### 1. 比率型
- 目標式： 找出一組對於受評決策單位k最有利的投入項與產出項之權重，以最大化其效率值
- 限制式： 效率值必須介於0到1之間，且各權重皆為正值

<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/pictures/crs1.png" width="450" height="250">
 
### 2. 原問題
由於上述的數學模型為分數線性規劃(fractional linear programming)形式，除了會發生多重解的情況外，求解也較不易，因此透過轉換，將其變成下列線性規劃的模式，以方便求解。

<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/pictures/crs2.png" width="450" height="260">

## (二)範例說明
**※在此以一個簡單的範例來建構上述的數學模型，並說明如何利用Python-Gurobi進行建模<br>**
- 此範例為一個具有兩項投入及三個產出的系統，內部的各製程均被視為黑盒子般，在此不被考量。

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/pictures/ex1.png" width="350" height="110">
</div>
 
- 共有五個決策單位要進行比較，其各自的產出項與投入項情形如下圖所示：

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/pictures/ex2.png" width="500" height="200">
</div>

- 並能形成如下所示的CRS Model：

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/pictures/ex3.png" width="450" height="260">
</div>
<br>

## (三)Python-Gurobi

## Import gurobipy
```python
from gurobipy import*
```
## Add parameters
- 透過for loop來計算每個決策單位的效率
```python
DMU=['A','B','C','D','E']
h={}
for k in DMU:
    I=2  # 兩項投入
    O=3  # 三項產出
    #X、Y為各DMU的投入與產出情形
    DMU,X,Y=multidict({('A'):[[11,14],[2,2,1]],('B'):[[7,7],[1,1,1]],('C'):[[11,14],[1,1,2]],('D'):[[14,14],[2,3,1]],('E'):[[14,15],[3,2,3]]})
```
## Model
```python
    m=Model("CRS_System_DEA")
```
## Add decision variables
- 建立決策變數投入項與產出項權重 v<sub>i</sup></sub>、 u<sub>r</sup></sub>
```python
    v={}
    u={}
    
    for i in range(I):
        v[i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%d"%i,lb=0.0001)
    
    for r in range(O):
        u[r]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%d"%r,lb=0.0001)
```
## Update
```python
    m.update()
```
## Add objective
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/pictures/crs2-1.png" width="200" height="80">

```python
    m.setObjective(quicksum(u[r]*Y[k][r] for r in range(O)),GRB.MAXIMIZE)
```
## Add constraints
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/pictures/crs2-2.png" width="275" height="125">

```python
    m.addConstr(quicksum(v[i]*X[k][i] for i in range(I))==1)
    for j in DMU:
        m.addConstr(quicksum(u[r]*Y[j][r] for r in range(O))-quicksum(v[i]*X[j][i] for i in range(I))<=0)
```
## Print result
```python
    m.optimize()
    h[k]="The efficiency of DMU %s:%4.3g"%(k,m.objVal)
    
for k in DMU:
    print (h[k])
```
**最後可得到如下所示的結果**
```
    The efficiency of DMU A:   1
    The efficiency of DMU B:0.898
    The efficiency of DMU C:0.848
    The efficiency of DMU D:   1
    The efficiency of DMU E:   1
```
