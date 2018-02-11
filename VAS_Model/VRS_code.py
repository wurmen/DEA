from gurobipy import*

E={}  
I=2
O=3
#X、Y為各DMU的投入與產出    
DMU,X,Y=multidict({('A'):[[11,14],[2,2,1]],('B'):[[7,7],[1,1,1]],('C'):[[11,14],[1,1,2]],('D'):[[14,14],[2,3,1]],('E'):[[14,15],[3,2,3]]})

for r in DMU:            
        
    m=Model("VRS_model")
    
    v,u,u0={},{},{}
    for i in range(I):
        v[r,i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%s%d"%(r,i))
    
    for j in range(O):
        u[r,j]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%s%d"%(r,j))
    u0[r]=m.addVar(lb=-1000,vtype=GRB.CONTINUOUS,name="u_0%s"%r)
    
    m.update()
    
    m.setObjective(quicksum(u[r,j]*Y[r][j] for j in range(O))-u0[r],GRB.MAXIMIZE)
        
    m.addConstr(quicksum(v[r,i]*X[r][i] for i in range(I))==1)
    for k in DMU:
        m.addConstr(quicksum(u[r,j]*Y[k][j] for j in range(O))-quicksum(v[r,i]*X[k][i] for i in range(I))-u0[r] <=0)
    
    m.optimize()
    
    E[r]="The efficiency of DMU %s:%0.3f and \n %s= %0.3f"%(r,m.objVal,u0[r].varName,u0[r].X)


for r in DMU:
    print (E[r])
