import time
rule_begning_flag=False
count=0
head=['Rule-ID']
with open('HRC_PUBLIC-MGMT.conf') as f:
    lines = f.readlines()
    for l in lines: 
        count=count+1       
        if l.strip() == "config firewall policy":
            rule_begning_flag=True
            
        
        elif rule_begning_flag==True and "set" in  l.strip():
            set_cmd_split=l.strip().split()
            
            if set_cmd_split[1] not in head:
                head.append(set_cmd_split[1])
            
            
        
        elif rule_begning_flag==True and l.strip() == "end":
            rule_begning_flag=False
f.close()

dummy_rule_list=[]
for i in range(len(head)):
    dummy_rule_list.append('')
    
def comb(value):
    m=''
    for i in range(2,len(value)):
        if value[1]!= 'uuid':
            m=m+" "+value[i].strip('"')
    return m

def csv_mode(printer_list):
    j=""
    for i in printer_list:
        j=j+i+"," 
    print (j)  

csv_mode(head)
rl_begin=False 
with open('HRC_PUBLIC-MGMT.conf') as f:
    lines = f.readlines()
    for l in lines: 
        count=count+1       
        if l.strip() == "config firewall policy":
            rule_begning_flag=True
            
            
        elif rule_begning_flag==True and "edit" in  l.strip():
            rule_id_split=l.strip().split()
            real_rule=dummy_rule_list
            real_rule[0]=rule_id_split[1]
            rl_begin=True   
            
            
        elif rl_begin==True and "set" in  l.strip():
            set_rule_split=l.strip().split()
            real_rule[head.index(set_rule_split[1])]=comb(set_rule_split)
            
            
        elif rule_begning_flag==True and "next" in  l.strip():
            rule_id_split=l.strip().split()
            rl_begin=False  
            #print(real_rule)
            csv_mode(real_rule)
                
            
        
        elif rule_begning_flag==True and "set" in  l.strip():
            set_cmd_split=l.strip().split()
            
            if set_cmd_split[1] not in head:
                head.append(set_cmd_split[1])
            
            
        
        elif rule_begning_flag==True and l.strip() == "end":
            rule_begning_flag=False
f.close()




     