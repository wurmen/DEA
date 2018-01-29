# CRS Model  

*POLab*
<br>
*2017/01/29*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)
<br>
## (一)CRS Model說明
**※此為DEA中固定規模報酬(constant return to scale, CRS)的模型建構說明，並以投入導向的模組為例**<br>
固定規模報酬指的是每一單位的投入可得到的產出量是固定的，並不會因為規模大小而改變，也就是說當投入量以等比例增加時，產出亦會以等比例增加，並在固定規模報酬的假設下，藉由將各決策單位(Decision Making Unit, DMU)的各項投入加權組合與各項產出加權組合互相比較，以得出各個決策單位的效率值，且效率值介於0到1之間
## (一)範例說明
此為一個具有兩項投入及三個產出的系統，內部的各製程被視為黑盒子般，在此不被考量。
```python
from gurobipy import*
DMU=['A','B','C','D','E']
val={}
for k in DMU:
    
    I=2
    O=3
    #X、Y為各DMU的產出與投入
    DMU,X,Y=multidict({('A'):[[11,14],[2,2,1]],('B'):[[7,7],[1,1,1]],('C'):[[11,14],[1,1,2]],('D'):[[14,14],[2,3,1]],('E'):[[14,15],[3,2,3]]})
    v={}
    u={}
    
    m=Model("CRS_System_DEA")
    
    for i in range(I):
        v[i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%d"%i,lb=0.0001)
    
    for r in range(O):
        u[r]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%d"%r,lb=0.0001)
    
    m.update()
    
    m.setObjective(quicksum(u[r]*Y[k][r] for r in range(O)),GRB.MAXIMIZE)
        
    m.addConstr(quicksum(v[i]*X[k][i] for i in range(I))==1)
    for j in DMU:
        m.addConstr(quicksum(u[r]*Y[j][r] for r in range(O))-quicksum(v[i]*X[j][i] for i in range(I))<=0)
    
    m.optimize()
    val[k]="The efficiency of DMU %s:%4.3g"%(k,m.objVal)
    
for k in DMU:
    print (val[k])
```

    Optimize a model with 6 rows, 5 columns and 27 nonzeros
    Coefficient statistics:
      Matrix range     [1e+00, 2e+01]
      Objective range  [1e+00, 2e+00]
      Bounds range     [1e-04, 1e-04]
      RHS range        [1e+00, 1e+00]
    Presolve removed 1 rows and 2 columns
    Presolve time: 0.04s
    Presolved: 5 rows, 3 columns, 15 nonzeros
    
    Iteration    Objective       Primal Inf.    Dual Inf.      Time
           0    1.0000000e+00   1.313453e-01   0.000000e+00      0s
           2    1.0000000e+00   0.000000e+00   0.000000e+00      0s
    
    Solved in 2 iterations and 0.06 seconds
    Optimal objective  1.000000000e+00
    Optimize a model with 6 rows, 5 columns and 27 nonzeros
    Coefficient statistics:
      Matrix range     [1e+00, 2e+01]
      Objective range  [1e+00, 1e+00]
      Bounds range     [1e-04, 1e-04]
      RHS range        [1e+00, 1e+00]
    Presolve removed 1 rows and 2 columns
    Presolve time: 0.03s
    Presolved: 5 rows, 3 columns, 15 nonzeros
    
    Iteration    Objective       Primal Inf.    Dual Inf.      Time
           0    1.9995000e+00   4.246461e+00   0.000000e+00      0s
           4    8.9791633e-01   0.000000e+00   0.000000e+00      0s
    
    Solved in 4 iterations and 0.06 seconds
    Optimal objective  8.979163265e-01
    Optimize a model with 6 rows, 5 columns and 27 nonzeros
    Coefficient statistics:
      Matrix range     [1e+00, 2e+01]
      Objective range  [1e+00, 2e+00]
      Bounds range     [1e-04, 1e-04]
      RHS range        [1e+00, 1e+00]
    Presolve removed 1 rows and 2 columns
    Presolve time: 0.03s
    Presolved: 5 rows, 3 columns, 15 nonzeros
    
    Iteration    Objective       Primal Inf.    Dual Inf.      Time
           0    1.9994000e+00   1.869235e+00   0.000000e+00      0s
           3    8.4816364e-01   0.000000e+00   0.000000e+00      0s
    
    Solved in 3 iterations and 0.06 seconds
    Optimal objective  8.481636364e-01
    Optimize a model with 6 rows, 5 columns and 27 nonzeros
    Coefficient statistics:
      Matrix range     [1e+00, 2e+01]
      Objective range  [1e+00, 3e+00]
      Bounds range     [1e-04, 1e-04]
      RHS range        [1e+00, 1e+00]
    Presolve removed 1 rows and 2 columns
    Presolve time: 0.03s
    Presolved: 5 rows, 3 columns, 15 nonzeros
    
    Iteration    Objective       Primal Inf.    Dual Inf.      Time
           0    1.4994000e+00   2.899834e-01   0.000000e+00      0s
           3    1.0000000e+00   0.000000e+00   0.000000e+00      0s
    
    Solved in 3 iterations and 0.06 seconds
    Optimal objective  1.000000000e+00
    Optimize a model with 6 rows, 5 columns and 27 nonzeros
    Coefficient statistics:
      Matrix range     [1e+00, 2e+01]
      Objective range  [2e+00, 3e+00]
      Bounds range     [1e-04, 1e-04]
      RHS range        [1e+00, 1e+00]
    Presolve removed 1 rows and 1 columns
    Presolve time: 0.04s
    Presolved: 5 rows, 4 columns, 19 nonzeros
    
    Iteration    Objective       Primal Inf.    Dual Inf.      Time
           0    2.7986800e+00   1.747242e+00   0.000000e+00      0s
           4    1.0000000e+00   0.000000e+00   0.000000e+00      0s
    
    Solved in 4 iterations and 0.06 seconds
    Optimal objective  1.000000000e+00
    The efficiency of DMU A:   1
    The efficiency of DMU B:0.898
    The efficiency of DMU C:0.848
    The efficiency of DMU D:   1
    The efficiency of DMU E:   1
    
