from gurobipy import*

E={}  
I=2
O=3
#X、Y為各DMU的產出與投入    
DMU,X,Y=multidict({('A'):[[11,14],[2,2,1]],('B'):[[7,7],[1,1,1]],('C'):[[11,14],[1,1,2]],('D'):[[14,14],[2,3,1]],('E'):[[14,15],[3,2,3]]})

for r in DMU:            
        
    m=Model("VRS_model")
    
    v,u={},{}
    for i in range(I):
        v[i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%d"%i)
    
    for j in range(O):
        u[j]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%d"%j)
    u0=m.addVar(lb=-1000,vtype=GRB.CONTINUOUS)
    
    m.update()
    
    m.setObjective(quicksum(u[j]*Y[r][j] for j in range(O))-u0,GRB.MAXIMIZE)
        
    m.addConstr(quicksum(v[i]*X[r][i] for i in range(I))==1)
    for k in DMU:
        m.addConstr(quicksum(u[j]*Y[k][j] for j in range(O))-quicksum(v[i]*X[k][i] for i in range(I))-u0 <=0)
    
    m.optimize()
    
    E[r]="The efficiency of DMU %s:%4.3g"%(r,m.objVal)

for r in DMU:
    print (E[r])