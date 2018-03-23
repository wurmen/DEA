# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from gurobipy import*
from itertools import islice
import csv

# TODO reading csv file including inputs and outputs for DMUs, transfered to 'dict' types for Linear Programming Modeling in Gurobi Software(package) 
def csv2dict(dea_data, in_range, out_range, assign=False):
    
    f=open(dea_data)
    reader=csv.reader(f)
    DMU = []
    X,Y={},{}
    
    # All values in in_range should be greater than 0; otherwise, stop the function    
    if all(value > 0 for value in in_range):
        in_range[:]=[x-1 for x in in_range]
    else:
        print("Error: all values given in in_range should be greater than 0")
        
		# Return nothing to stop the function
        return 

    # Same as the in_range
    if all(value > 0 for value in out_range):
        out_range[:] = [y-1 for y in out_range]
    else:
        print("Error: all values given in out_range should be greater than 0")
		
		# Return nothing to stop the function
        return 

    for line in islice(reader,1,None):
        
        obs = line     
        key=obs[0]    # Remove line breaks '/n'

        DMU.append(key)  # Get DMU names
        
        # Create dictionaries
        try:
            if (assign==False): 
                
                # Give a range to get input and ouput data
                X[key]= [float(v) for v in obs[(in_range[0]):(in_range[1]+1)]] # List comprehension
                Y[key]= [float(v) for v in obs[(out_range[0]):(out_range[1]+1)]]
                
            elif (assign==True): 
                
                # Get specific lines as input and output data
                # X and Y are input and output of DMU separately
                X[key]= [float(v) for v in (list(obs[i] for i in in_range))] # List comprehension
                Y[key]= [float(v) for v in (list(obs[i] for i in out_range))]

        except ValueError :
            print("which means your data include string not number")
            
    return DMU, X, Y



# TODO reading csv file including inputs and outputs for DMUs if they are separated in different two files (one for inputs, another for outputs)
# then, transfered to 'dict' types for Linear Programming Modeling in Gurobi Software(package)  
def csv2dict_sep(dea_data, vrange=[0,0], assign=False):
    
#    The input and output data are separated into different files
    f=open(dea_data)
    reader=csv.reader(f)
    DMU = []
    value={}
    
    vrange[:]=[v-1 for v in vrange]
    
    for line in islice(reader,1,None):
        obs = line 
        obs_len = len(obs)    
        key=obs[0]   #Get DMU names
        DMU.append(key)
        
        # Create dictionaries
        try:
            if (assign==False):
                value[key]= [float(v) for v in obs[1:(obs_len)]]
            elif (assign==True):
                # Get specific lines as input or output data
                value[key]= [float(v) for v in (list(obs[i] for i in vrange))]
        except IOError :
            print("which means your data include string not number")
            
    return DMU, value



# TODO solve DEA_CRS models with LP technique by Gurobi Software (package) 
def CRS(DMU, X, Y, orientation, dual):

    I=len(X[DMU[0]])
    O=len(Y[DMU[0]])   
    E={}# Efficiency    
    if (orientation=='input' and dual==False):
        
        for r in DMU:
            try:    
                # The decision variables                            
                v,u={},{}
                
                # Initialize LP model
                m=Model("CRS_model")
                m.setParam('OutputFlag', 0) # Muting the optimize function
                
                # Add decision variables
                for i in range(I):
                    v[r,i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%s%d"%(r,i))
                
                for j in range(O):
                    u[r,j]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%s%d"%(r,j))
                
                m.update()
                
                # Add objective function 
                m.setObjective(quicksum(u[r,j]*Y[r][j] for j in range(O)),GRB.MAXIMIZE)
                
                # Add constraints
                m.addConstr(quicksum(v[r,i]*X[r][i] for i in range(I))==1)
                for k in DMU:
                    m.addConstr(quicksum(u[r,j]*Y[k][j] for j in range(O))-quicksum(v[r,i]*X[k][i] for i in range(I))<=0)
                
                # Start optimize the formulation
                m.optimize()
                
                # Store the result
                E[r]="The efficiency of DMU %s:%0.3f"%(r,m.objVal)
                
            except GurobiError:
            	print ('GurobiError reported')
                
            # Print result    
            print (E[r])

    elif (orientation=='input' and dual==True):                
        # TODO solve dual of input-oriented CRS DEA model with LP technique by Gurobi Software (package)                     
        for r in DMU:
            try:        
                
                # The decision variables
                theta,λ={},{}
            
                # Initialize LP model
                m=Model("Dual_of_CRS_model")
                m.setParam('OutputFlag',False)  # Muting the optimize function
                
                # Add decision variables
                for k in DMU:
                    λ[k]=m.addVar(vtype=GRB.CONTINUOUS,name="λ_%s"%k)
                theta[r]=m.addVar(vtype=GRB.CONTINUOUS,lb=-1000,name="theta_%s"%r)    
               
                m.update()
                
                # Add objective function
                m.setObjective(theta[r],GRB.MINIMIZE)
                
                # Add constraints
                for i in range(I):
                    m.addConstr(quicksum(λ[k]*X[k][i] for k in DMU)<= theta[r]*X[r][i])
                for j in range(O):
                    m.addConstr(quicksum(λ[k]*Y[k][j] for k in DMU)>= Y[r][j])
                
                # Start optimize the formulation 
                m.optimize()
                
                # Store the result
                E[r]="The efficiency of DMU %s:%0.3f"%(r,m.objVal)
                
    #            for c in m.getConstrs():
    #                print ("The slack value of %s : %g"%(c.constrName,c.Slack))
    #            print(m.getAttr('slack', m.getConstrs()))
    #            print(m.getAttr('x', m.getVars()))
            
            except GurobiError:
            	print ('GurobiError reported')
            
            # Print efficiency
            print (E[r])        
    elif(orientation=='output' and dual==False):        
    # TODO solve output-oriented DEA_CRS  model with LP technique by Gurobi Software (package) 
        for r in DMU:
            try:    
                # The decision variables                            
                v,u={},{}
                
                # Initialize LP model
                m=Model("CRS_model")
                m.setParam('OutputFlag', 0) # Muting the optimize function
                
                # Add decision variables
                for i in range(I):
                    v[r,i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%s%d"%(r,i))
                
                for j in range(O):
                    u[r,j]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%s%d"%(r,j))
                
                m.update()
                
                # Add objective function 
                m.setObjective(quicksum(v[r,i]*X[r][i] for i in range(I)),GRB.MINIMIZE)
                
                # Add constraints
                m.addConstr(quicksum(u[r,j]*Y[r][j] for j in range(O))==1)
                for k in DMU:
                    m.addConstr(quicksum(v[r,i]*X[k][i] for i in range(I))-quicksum(u[r,j]*Y[k][j] for j in range(O))>=0)
                
                # Start optimize the formulation
                m.optimize()
                
                # Store the result
                E[r]="The efficiency of DMU %s:%0.3f"%(r,1/m.objVal)
                
            except GurobiError:
            	print ('GurobiError reported')
                
            # Print result    
            print (E[r])
    elif(orientation=='output' and dual==True):  
        # TODO solve dual of output-oriented CRS DEA model with LP technique by Gurobi Software (package)                     
        for r in DMU:
            try:        
                
                # The decision variables
                theta, λ={}, {}
            
                # Initialize LP model
                m=Model("Dual_of_CRS_model")
                m.setParam('OutputFlag',False)  # Muting the optimize function
                
                # Add decision variables
                for k in DMU:
                    λ[k]=m.addVar(vtype=GRB.CONTINUOUS,name="λ_%s"%k)
                theta[r]=m.addVar(vtype=GRB.CONTINUOUS,lb=-1000,name="theta_%s"%r)    
               
                m.update()
                
                # Add objective function
                m.setObjective(theta[r],GRB.MAXIMIZE)
                
                # Add constraints
                for j in range(O):
                    m.addConstr(quicksum(λ[k]*Y[k][j] for k in DMU)>= theta[r]*Y[r][j])
                for i in range(I):
                    m.addConstr(quicksum(λ[k]*X[k][i] for k in DMU)<= X[r][i])
                
                # Start optimize the formulation 
                m.optimize()
                
                # Store the result
                E[r]="The efficiency of DMU %s:%0.3f"%(r,1/m.objVal)
                
#                for c in m.getConstrs():
#                    print ("The slack value of %s : %g"%(c.constrName,c.Slack))
#                print(m.getAttr('slack', m.getConstrs()))
#                print(m.getAttr('x', λ))
            
            except GurobiError:
            	print ('GurobiError reported')
            
            # Print efficiency
            print (E[r])        
        
        
# TODO solve DEA_VRS models with LP technique by Gurobi Software (package)       
def VRS(DMU, X, Y, orientation, dual):
    
    I=len(X[DMU[0]])
    O=len(Y[DMU[0]])    
    E={}  
    u0_v={}
    
    if(orientation=="input" and dual==False):
        
        for r in DMU:
            try:
             
                
                # Initialize LP model
                m=Model("VRS_model")
                m.setParam('OutputFlag',0) # Muting the optimize function 
                
                # The decision variable
                v,u,u0={},{},{}
                
                # Add decision variables
                for i in range(I):
                    v[r,i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%s%d"%(r,i))
                
                for j in range(O):
                    u[r,j]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%s%d"%(r,j))
                u0[r]=m.addVar(lb=-1000,vtype=GRB.CONTINUOUS,name="u0_%s"%r)
                
                
                m.update()
                
                # Add objective function
                m.setObjective(quicksum(u[r,j]*Y[r][j] for j in range(O))-u0[r],GRB.MAXIMIZE)
                
                # Add constraints
                m.addConstr(quicksum(v[r,i]*X[r][i] for i in range(I))==1)
                for k in DMU:
                    m.addConstr(quicksum(u[r,j]*Y[k][j] for j in range(O))-quicksum(v[r,i]*X[k][i] for i in range(I))-u0[r] <=0)
                
                m.optimize()
                
                # Print efficiency            
                E[r]="The efficiency of DMU %s:%0.3f"%(r,m.objVal)
                
                print (E[r])
    #            if RTS_check==True:
    #                u0_v[r]='%s = %0.3f'%(u0[r].varName,u0[r].X)
    #                print(u0_v[r])
    
            except GurobiError:
            	print ('GurobiError reported')


    elif(orientation=="input" and dual==True):
        # TODO solve dual of input-oriented VRS DEA model with LP technique by Gurobi Software (package)         
        for r in DMU:
            try:        
                
                # The decision variables
                theta, λ={}, {}
            
                # Initialize LP model
                m=Model("Dual_of_CRS_model")
                m.setParam('OutputFlag',False)  # Muting the optimize function
                
                # Add decision variables
                for k in DMU:
                    λ[k]=m.addVar(vtype=GRB.CONTINUOUS,name="λ_%s"%k)
                theta[r]=m.addVar(vtype=GRB.CONTINUOUS,lb=-1000,name="theta_%s"%r)    
               
                m.update()
                
                # Add objective function
                m.setObjective(theta[r],GRB.MINIMIZE)
                
                # Add constraints
                for i in range(I):
                    m.addConstr(quicksum(λ[k]*X[k][i] for k in DMU)<= theta[r]*X[r][i])
                for j in range(O):
                    m.addConstr(quicksum(λ[k]*Y[k][j] for k in DMU)>= Y[r][j])
                m.addConstr(quicksum(λ[k] for k in DMU)==1,name='sum of λ')
                
                # Start optimize the formulation 
                m.optimize()
                
                # Store the result
                E[r]="The efficiency of DMU %s:%0.3f"%(r,m.objVal)
                val=m.getAttr('X',λ)
    #            for c in m.getConstrs():
    #                print ("The slack value of %s : %g"%(c.constrName,c.Slack))
    #            print(m.getAttr('slack', m.getConstrs()))
    #            print(m.getAttr('x', m.getVars()))
            
            except GurobiError:
            	print ('GurobiError reported')
            
            # Print efficiency
            print (E[r]) 
        

    # TODO solve output-oriented DEA_VRS model with LP technique by Gurobi Software (package)       
    elif(orientation=="output" and dual==False):        
        v0_v={}
        
        
        for r in DMU:
            try:
             
                
                # Initialize LP model
                m=Model("VRS_output_model")
                m.setParam('OutputFlag',0) # Muting the optimize function 
                
                # The decision variable
                v,u,v0={},{},{}
                
                # Add decision variables
                for i in range(I):
                    v[r,i]=m.addVar(vtype=GRB.CONTINUOUS,name="v_%s%d"%(r,i))
                
                for j in range(O):
                    u[r,j]=m.addVar(vtype=GRB.CONTINUOUS,name="u_%s%d"%(r,j))
                v0[r]=m.addVar(lb=-1000,vtype=GRB.CONTINUOUS,name="v0_%s"%r)
                
                
                m.update()
                
                # Add objective function
                m.setObjective(quicksum(v[r,i]*X[r][i] for i in range(I))+v0[r],GRB.MINIMIZE)
                
                # Add constraints
                m.addConstr(quicksum(u[r,j]*Y[r][j] for j in range(O))==1)
                for k in DMU:
                    m.addConstr(quicksum(v[r,i]*X[k][i] for i in range(I))-quicksum(u[r,j]*Y[k][j] for j in range(O))+v0[r] >=0)
                
                m.optimize()
                
                # Print efficiency            
                E[r]="The efficiency of DMU %s:%0.3f"%(r,1/m.objVal)
                
                print (E[r])
#                if RTS_check==True:            
#                    v0_v[r]='%s = %0.3f'%(v0[r].varName,v0[r].X)
#                    print(v0_v[r])
        
            except GurobiError:
            	print ('GurobiError reported')

    elif(orientation=="output" and dual==True):
        # TODO solve dual of output-oriented VRS DEA model with LP technique by Gurobi Software (package)      
        for r in DMU:
            try:        
                
                # The decision variables
                theta, λ={}, {}
            
                # Initialize LP model
                m=Model("Dual_of_output-oriented_VRS_model")
                m.setParam('OutputFlag',False)  # Muting the optimize function
                
                # Add decision variables
                for k in DMU:
                    λ[k]=m.addVar(vtype=GRB.CONTINUOUS,name="λ_%s"%k)
                theta[r]=m.addVar(vtype=GRB.CONTINUOUS,lb=-1000,name="theta_%s"%r)    
               
                m.update()
                
                # Add objective function
                m.setObjective(theta[r],GRB.MAXIMIZE)
                
                # Add constraints
                for j in range(O):
                    m.addConstr(quicksum(λ[k]*Y[k][j] for k in DMU)>= theta[r]*Y[r][j])
                for i in range(I):
                    m.addConstr(quicksum(λ[k]*X[k][i] for k in DMU)<= X[r][i])
                m.addConstr(quicksum(λ[k] for k in DMU)==1,name='sum of λ')
                
                # Start optimize the formulation 
                m.optimize()
                
                # Store the result
                E[r]="The efficiency of DMU %s:%0.3f"%(r,1/m.objVal)
                
        #        for c in m.getConstrs():
        #            print ("The slack value of %s : %g"%(c.constrName,c.Slack))
        #        print(m.getAttr('slack', m.getConstrs()))
        #        print(m.getAttr('x', λ))
            
            except GurobiError:
            	print ('GurobiError reported')
            
            # Print efficiency
            print (E[r]) 
        

    
    