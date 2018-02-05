# CRS Model  

*POLab*
<br>
*2017/01/29*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)
<br>
#### ※*Reference*
*本篇範例資料取自[高強教授](http://www.iim.ncku.edu.tw/files/11-1407-20368.php?Lang=zh-tw)於2007發表的Paper：[Efficiency decomposition in network data envelopment analysis: A relational model](https://www.sciencedirect.com/science/article/pii/S0377221707010077)*


## (一)CRS Model
**※此為DEA中固定規模報酬(constant return to scale, CRS)的模型建構說明，並以投入導向的模組為例**<br>
<br>
固定規模報酬是指每一單位的投入可得到的產出量是固定的，並不會因為規模大小而改變，也就是說當投入量以等比例增加時，產出亦會以等比例增加，並在固定規模報酬的假設下，藉由將各決策單位(Decision Making Unit, DMU)的各項投入加權組合與各項產出加權組合互相比較計算其比值，以得出各個決策單位的相對效率值，且效率值介於0到1之間，而在CRS模式中所求得的效率值又稱之為**總體效率值(overall efficiency)**；投入導向指的是在相同產出水準下，比較各決策單位投入資源的使用效率。<br>

### § 符號說明
- E<sub>r</sup></sub>： 決策單位r的效率值
- K： 決策單位(DMU)個數 r,k∈K <br>
- I： 投入項個數 i∈I <br>
- J： 產出項個數 j∈J <br>
- ε： 極小的正值稱之為非阿基米德數(non-Archimedean constant)，通常設為10<sup>-4</sup></sub>或10<sup>-6</sup></sub>(目的為了使任一投入或產出項皆不會被忽略)
### § 參數說明
- X<sub>ik</sup></sub>： 決策單位k (k=1,...,K)使用第i (i=1,...,I)個投入項
- Y<sub>jk</sup></sub>： 決策單位k (k=1,...,K)使用第j (j=1,...,J)個產出項
### § 決策變數
- u<sub>j</sup></sub>： 第j個產出項之權重
- v<sub>i</sup></sub>： 第i個投入項之權重
### § CRS Model
#### 1. 比率型
- 目標式： 找出一組對於受評決策單位r最有利的投入項與產出項之權重，以最大化其效率值
- 限制式： 效率值必須介於0到1之間，且各權重皆為正值

<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/picture/crs1.png" width="450" height="250">
 
#### 2. 原問題
由於上述的數學模型為分數線性規劃(fractional linear programming)形式，除了會發生多重解的情況外，求解也較不易，因此透過轉換，將其變成下列線性規劃的模式，以方便求解。

<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/picture/crs2.png" width="450" height="260">

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

- 並能形成如下所示的CRS Model：

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/picture/ex3.png" width="450" height="260">
</div>
<br>

## (三)Python-Gurobi
在此說明如何運用Python-Gurobi來建構CRS model
##### ※完整程式碼可點擊[這裡](https://github.com/wurmen/DEA/blob/master/CRS_Model/CRS_code.py)

### Import gurobipy
```python
from gurobipy import*
```
### Add parameters
- 透過for loop來計算每個決策單位的效率
```python
DMU=['A','B','C','D','E']
E={}
for r in DMU:
    I=2  # 兩項投入
    O=3  # 三項產出
    #X、Y為各DMU的投入與產出情形
    DMU,X,Y=multidict({('A'):[[11,14],[2,2,1]],('B'):[[7,7],[1,1,1]],('C'):[[11,14],[1,1,2]],('D'):[[14,14],[2,3,1]],('E'):[[14,15],[3,2,3]]})
```
### Model
```python
    m=Model("CRS_model")
```
### Add decision variables
- 建立決策變數投入項與產出項權重 v<sub>i</sup></sub>、 u<sub>j</sup></sub>
```python

    v,u={},{}

    for i in range(I):
        v[i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%d"%i,lb=0.0001)
    
    for j in range(O):
        u[j]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%d"%j,lb=0.0001)
```
### Update
```python
    m.update()
```
### Add objective
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/picture/crs2-1.png" width="200" height="80">

```python
    m.setObjective(quicksum(u[j]*Y[r][j] for j in range(O)),GRB.MAXIMIZE)
```
### Add constraints
<img src="https://github.com/wurmen/DEA/blob/master/CRS_Model/picture/crs2-2.png" width="275" height="125">

```python
    m.addConstr(quicksum(v[i]*X[r][i] for i in range(I))==1)
    for k in DMU:
        m.addConstr(quicksum(u[j]*Y[k][j] for j in range(O))-quicksum(v[i]*X[k][i] for i in range(I))<=0)
```
### Print result
```python
    m.optimize()
    E[r]="The efficiency of DMU %s:%4.3g"%(r,m.objVal)
    
for r in DMU:
    print (E[r])
```
**最後可得到如下所示的結果**<br>
從結果我們可知決策單位A、D、E與其他決策單位相比是相較有效率的，其效率值皆為1。
```
    The efficiency of DMU A:   1
    The efficiency of DMU B:0.898
    The efficiency of DMU C:0.848
    The efficiency of DMU D:   1
    The efficiency of DMU E:   1
```
