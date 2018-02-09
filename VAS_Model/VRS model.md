# VRS Model 

*POLab*
<br>
*2017/02/05*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)
<br>
#### ※*Reference*
*本篇範例資料取自[高強教授](http://www.iim.ncku.edu.tw/files/11-1407-20368.php?Lang=zh-tw)於2007發表的Paper：[Efficiency decomposition in network data envelopment analysis: A relational model](https://www.sciencedirect.com/science/article/pii/S0377221707010077)*


## (一)VRS Model
**※此為DEA中變動規模報酬(variable return to scale, VRS)的模型建構說明，並以投入導向的模組為例**<br>
<br>
在CRS模式中，假設每一單位的投入可得到的產出量是固定的，並不會因為規模大小而改變的固定規模報酬形式，但在現實生產過程中，可能會因為不同的生產規模，規模報酬也會跟著改變，因此Banker等人(1984)將CRS模式修正成VRS模式，在此假設下衡量各決策單位(Decision Making Unit, DMU)的相對效率，並同時評估決策單位是否達到有效的生產規模，故VRS模式可一併衡量**規模效率(scale efficiency, SE)**與**技術效率(technical efficiency, TE)**。<br>
<br>
CRS模式中所求得的效率值稱為**總體效率值(overall efficiency)**，而VRS模式所得的效率值為**技術效率(technical efficiency)**，藉由這兩者之比較可得到**規模效率(scale efficiency)**，因此得出以下公式:<br>
<br>
**<p align="center">總體效率值(OE) = 技術效率(TE)X規模效率(SE)</p>** 
**<p align="center">SE =   E<sub>r</sup></sub><sup>CRS</sup></sub>/E<sub>r</sup></sub><sup>VRS</sup></sub> </p>**
#### ※規模報酬又可分為三種形式
##### 1.固定規模報酬(constant returns to scale, CRS)：<br>
###### 產出與投入成正比，且每一單位投入可得到的產出量是固定的；以公司的發展而言，此狀態是最佳的
##### 2.規模報酬遞減(decreasing returns to scale, DRS)： 
###### 投入增加時，產出的增加比例，比投入增加的比例少；以公司的發展而言，此狀態可能位於生產規模過於龐大時，導致生產減緩
##### 3.規模報酬遞增(increasing returns to scale, IRS)： 
###### 投入增加時，產出的增加比例，比投入增加的比例多；以公司的發展而言，此狀態可能位於初創時期，或者進行併購或聯盟等策略
### § 符號說明
- E<sub>r</sup></sub><sup>VRS</sup></sub>： 決策單位r的效率值
- K： 決策單位(DMU)個數 r,k∈K <br>
- I： 投入項個數 i∈I <br>
- J： 產出項個數 j∈J <br>
- ε： 極小的正值稱之為非阿基米德數(non-Archimedean constant)，通常設為10<sup>-4</sup></sub>或10<sup>-6</sup></sub>(目的為了使任一投入或產出項皆不會被忽略)
### § 參數說明
- X<sub>ki</sup></sub>： 決策單位k (k=1,...,K)使用第i (i=1,...,I)個投入項
- Y<sub>kj</sup></sub>： 決策單位k (k=1,...,K)使用第j (j=1,...,J)個產出項
### § 決策變數
- u<sub>rj</sup></sub>： 決策單位r的第j個產出項之權重
- v<sub>ri</sup></sub>： 決策單位r的第i個投入項之權重
- u<sub>0r</sup></sub>： 允許生產函數不必通過原點，可用來判斷規模報酬型態<br>
#### ※透過u<sub>0r</sup></sub>的正負來分辨規模報酬
##### u<sub>0r</sup></sub> = 0 為固定規模報酬(CRS)<br>
##### -u<sub>0r</sup></sub> > 0 為規模報酬遞增(IRS)<br>
##### -u<sub>0r</sup></sub> < 0 為規模報酬遞減(DRS)<br>
### § VRS Model
#### 1. 比率型
- 目標式： 找出一組對於受評決策單位r最有利的投入項與產出項之權重，以最大化其效率值
- 限制式： 效率值必須介於0到1之間，且各權重皆為正值

<img src="https://github.com/wurmen/DEA/blob/master/VAS_Model/picture/vrs1.png" width="450" height="250">
 
#### 2. 原問題
如同在CRS Model所述，由於上述的數學模型為分數線性規劃(fractional linear programming)形式，除了會發生多重解的情況外，求解也較不易，因此透過轉換，將其變成下列線性規劃的模式，以方便求解。

<img src="https://github.com/wurmen/DEA/blob/master/VAS_Model/picture/vrs2.png" width="450" height="260">

## (二)範例說明
**※在此以一個簡單的範例來建構上述的數學模型，並說明如何利用Python-Gurobi進行建模<br>**
- 此範例為一個具有兩項投入及三項產出的系統，系統內部的各製程均被視為黑盒子般，在此不被考量。

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/picture/ex1.png" width="350" height="110">
</div>
 
- 共有五個決策單位要進行比較，其各自的產出項與投入項情形如下圖所示：

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/picture/ex2.png" width="500" height="200">
</div>

- 並能形成如下所示的VRS Model：

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/VAS_Model/picture/ex.png" width="450" height="260">
</div>
<br>

## (三)Python-Gurobi
在此說明如何運用Python-Gurobi來建構VRS model
##### ※完整程式碼可點擊[這裡](https://github.com/wurmen/DEA/blob/master/VAS_Model/VRS_code.py)

### Import gurobipy
```python
from gurobipy import*
```
### Add parameters
```python
E={}
I=2  # 兩項投入
O=3  # 三項產出
#X、Y為各DMU的投入與產出情形
DMU,X,Y=multidict({('A'):[[11,14],[2,2,1]],('B'):[[7,7],[1,1,1]],('C'):[[11,14],[1,1,2]],('D'):[[14,14],[2,3,1]],('E'):[[14,15],[3,2,3]]})
```
### Model
- 透過for loop來計算每個決策單位的效率
```python
for r in DMU:
    m=Model("VRS_model")
```
### Add decision variables
- 建立決策變數投入項與產出項權重 v<sub>ri</sup></sub>、 u<sub>rj</sup></sub>以及u<sub>or</sup></sub>
```python

    v,u={},{}

    for i in range(I):
        v[r,i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%s%d"%(r,i),lb=0.0001)
    
    for j in range(O):
        u[r,j]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%s%d"%(r,j),lb=0.0001)
    u[0,r]=m.addVar(lb=-1000,vtype=GRB.CONTINUOUS,name="u_0%s"%r)
```
### Update
```python
    m.update()
```
### Add objective
<img src="https://github.com/wurmen/DEA/blob/master/VAS_Model/picture/vrs2-1.png" width="200" height="80">

```python
    m.setObjective(quicksum(u[r,j]*Y[r][j] for j in range(O))-u[0,r],GRB.MAXIMIZE)
```
### Add constraints
<img src="https://github.com/wurmen/DEA/blob/master/VAS_Model/picture/vrs2-2.png" width="275" height="125">

```python
    m.addConstr(quicksum(v[r,i]*X[r][i] for i in range(I))==1)
    for k in DMU:
        m.addConstr(quicksum(u[r,j]*Y[k][j] for j in range(O))-quicksum(v[r,i]*X[k][i] for i in range(I))-u[0,r] <=0)
```
### Print result
- 取得各決策單位之效率值，並透過gurobi屬性varName、X來取得各決策單位u<sub>0r</sup></sub>之值
```python
    m.optimize()
    E[r]="The efficiency of DMU %s:%0.3f and \n %s= %0.3f"%(r,m.objVal,u[0,r].varName,u[0,r].X)
    
for r in DMU:
    print (E[r])
```
**最後可得到如下所示的結果**<br>
```
    The efficiency of DMU A:1.000 and 
     u_0A= -0.273
    The efficiency of DMU B:1.000 and 
     u_0B= -1.000
    The efficiency of DMU C:0.955 and 
     u_0C= -0.318
    The efficiency of DMU D:1.000 and 
     u_0D= -0.250
    The efficiency of DMU E:1.000 and 
     u_0E= -0.200
```


**整合CRS Model與VRS Model所求得的結果，我們可得到下表:**

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/VAS_Model/picture/all.jpg" width="550" height="200">
</div>





