# -*- coding: utf-8 -*-

from gurobipy import*
from itertools import islice
import csv

def csv2dict_for_network_dea(dea_data, v1_range, v2_range, p_n=0):
    
    f=open(dea_data)
    reader=csv.reader(f)
    
    DMU = []
    X,Y={},{}
    
    
    # All values in v1_range should be greater than 0; otherwise, stop the function    
    if all(value > 0 for value in v1_range):
        v1_range[:]=[x-1 for x in v1_range]
    else:
        print("Error: all values given in in_range should be greater than 0")
        
		# Return nothing to stop the function
        return 

    # Same as the v1_range
    if all(value > 0 for value in v2_range):
        v2_range[:] = [y-1 for y in v2_range]
    else:
        print("Error: all values given in out_range should be greater than 0")
		
		# Return nothing to stop the function
        return 

    counter = 0
    for line in islice(reader,1,None):
        
        obs=line    
        key=obs[0]
        
        # Create dictionaries
        if (counter % (p_n + 1)) == 0:   
            DMU.append(key)  # Get DMU names
            tmp_key = key
            X[key]=[]
            Y[key]=[]
            
            try:             
                # Give a range to get input or ouput data
                X[key].append([float(v) for v in obs[(v1_range[0]):(v1_range[1]+1)]]) # List comprehension
                Y[key].append([float(v) for v in obs[(v2_range[0]):(v2_range[1]+1)]])                    
        
            except ValueError :
                print("which means your data include string not number")
        else:
            
            try:                         
                 # Give a range to get input or ouput data
                 X[tmp_key].append([float(v) for v in obs[(v1_range[0]):(v1_range[1]+1)]] ) # List comprehension                 
                 Y[tmp_key].append([float(v) for v in obs[(v2_range[0]):(v2_range[1]+1)]])
    
            except ValueError :
                print("which means your data include string not number")
        
        counter += 1     
    return DMU,X,Y,p_n


def network(DMU,X,Y,Z_input,Z_output,p_n,var_lb):
    E={}
    P,P_efficiency={},{}    
    for r in DMU:
    
        I=len(X[DMU[0]][0])
        O=len(Y[DMU[0]][0])
        G=len(Z_input[DMU[0]][0])
        
        v,u,w={},{},{}
        
        m=Model("network_DEA")
        m.setParam('OutputFlag', 0) # Muting the optimize function
        
        for i in range(I):
            v[r,i]=m.addVar(lb=var_lb,vtype=GRB.CONTINUOUS,name="v_%s%d"%(r,i))
        
        for j in range(O):
            u[r,j]=m.addVar(lb=var_lb,vtype=GRB.CONTINUOUS,name="u_%s%d"%(r,j))
        for g in range(G):
            w[r,g]=m.addVar(lb=var_lb,vtype=GRB.CONTINUOUS,name="w_%s%d"%(r,g))

                                 
        m.update()
       
        m.setObjective(quicksum(u[r,j]*Y[r][0][j] for j in range(O))+quicksum(w[r,g]*Z_output[r][0][g] for g in range(G)),GRB.MAXIMIZE)
        
        m.addConstr(quicksum(v[r,i]*X[r][0][i] for i in range(I))==1)
        m.addConstr(quicksum(u[r,j]*Y[r][0][j] for j in range(O))-quicksum(v[r,i]*X[r][0][i] for i in range(I))<=0)    
        for k in DMU:
            for p in range(p_n):
                P[r,k,p]=m.addConstr((quicksum(u[r,j]*Y[k][p+1][j] for j in range(O))+quicksum(w[r,g]*Z_output[k][p+1][g] for g in range(G)))-
                 (quicksum(v[r,i]*X[k][p+1][i] for i in range(I)) + quicksum(w[r,g]*Z_input[k][p+1][g] for g in range(G)))<=0)         
       
        m.optimize()
        

        if m.status==GRB.OPTIMAL:
            E[r]=m.objVal
            print("The efficiency of DMU %s:%0.3f"%(r,E[r]))
            for p in range(p_n):
                denominator=sum(v[r,i].x*X[r][p+1][i] for i in range(I)) + sum(w[r,g].x*Z_input[r][p+1][g] for g in range(G))
                if denominator!=0:                
                    P_efficiency[r,p]=((sum(u[r,j].x*Y[r][p+1][j] for j in range(O))+sum(w[r,g].x*Z_output[r][p+1][g] for g in range(G)))/
                                (sum(v[r,i].x*X[r][p+1][i] for i in range(I)) + sum(w[r,g].x*Z_input[r][p+1][g] for g in range(G))))
                    print('The efficiency and inefficiency of Process %s for DMU %s:%0.4f and %0.4g'%(p,r,P_efficiency[r,p],P[r,r,p].slack))
                else:
                    print('The efficiency of Process %s for DMU %s can\'t be calculated, probably because the process is calculated with a denominator of 0'%(p,r))

        else:
            print('The model status of the DMU %s is %d. \n you can confirm what the value means on the website(http://www.gurobi.com/documentation/7.5/refman/status.html)'%(r,m.status))

        
                
#        for c in m.getVars():
#            print('the weight of DMU %s :(%s=%0.20f)'%(r,c.varName,c.X))

    #return E