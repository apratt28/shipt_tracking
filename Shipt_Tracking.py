#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Using regular expression to extract addresses and associated tips, and addresses without tips. 
def regex_pat():
    global working_tip_list
    global working_notip_list
    address_tip_pat = '\n\d+\s\D*\s*\D*\s*\D*\s*\D*\s*\D*\s*\D*\n|\d+\/\d+'
    working_tip_list = re.findall(address_tip_pat,text)
    notip_pat = '\n\d+\s\D*\s*\D*\s*\D*\s*\D*\s*\D*\s*\D*\n'
    working_notip_list = re.findall(notip_pat,no_tip_txt)


# In[ ]:


### Add each tip associsted with address to index position containing the address. 
### Also count the maximum number of orders for one address. 
def address_tip_same_line():
    x = 0
    global max_orders
    max_orders = 0
    for i in working_tip_list:
        try:
            if '\n' in working_tip_list[x]:
                y = 1
                for z in working_tip_list[x:]:
                    if '\n' not in working_tip_list[x+y]:
                        working_tip_list[x] = working_tip_list[x] + ' ' + working_tip_list[x+y]
                        y = y + 1
                        if y > max_orders:
                            max_orders = y
                
        except: IndexError
        x = x + 1
    


# In[ ]:


### Create the dictionaries that hold lists of tips, order pay, and percent tip. 
def initialize_dicts():
    global tips_dict
    global tips_pay_dict
    global tips_order_pay_dict
    global tips_pcent_dict
    tips_dict = {}
    tips_pay_dict = {}
    tips_order_pay_dict = {}
    tips_pcent_dict = {}

    for i in range(1,max_orders+1):
        tips_dict['tip'+str(i)] = []
        tips_pay_dict['tip'+str(i)+'_tip_pay'] = []
        tips_order_pay_dict['tip'+str(i)+'_order_pay'] = []
        tips_pcent_dict['tip'+str(i)+'_percent'] = []


# In[ ]:


### Extract the index values that contain the addresses (and tips).
### Convert tip list into nexted list with index [1] being address, and index [2] as associated tips. 
### Sort addresses numerically.
def extract_split_sort_address_tip_list():
    for i in working_tip_list:
        if '\n' in i:
            extracted_address_tip_list.append(i)
        else:
            pass
    x = 0
    for i in extracted_address_tip_list:
        extracted_address_tip_list[x] = extracted_address_tip_list[x].split('\n')
        x = x + 1
    extracted_address_tip_list.sort()


# In[ ]:


### If address was originally in multiple Google maps lists, gather all tips for address on first instance. 
def handle_duplicates1():
    x = 0
    for i in extracted_address_tip_list:
        try:
            if extracted_address_tip_list[x][1] == extracted_address_tip_list[x+1][1]:
                extracted_address_tip_list[x].append(extracted_address_tip_list[x+1][2])
                extracted_address_tip_list.pop(x+1)
                if extracted_address_tip_list[x][1] == extracted_address_tip_list[x+1][1]:
                    extracted_address_tip_list[x].append(extracted_address_tip_list[x+1][2])
                    extracted_address_tip_list.pop(x+1)
        except: IndexError
        x = x + 1


# In[ ]:


### A new index position was created for adding tips from other Google Maps lists, so combine all tips into one index position. 
def handle_duplicates2():
    x = 0
    for i in extracted_address_tip_list:
        try:
            extracted_address_tip_list[x][2] = extracted_address_tip_list[x][2] + extracted_address_tip_list[x][3] 
            extracted_address_tip_list[x].pop(3)
        except: IndexError
            
        try:
            extracted_address_tip_list[x][2] = extracted_address_tip_list[x][2] + extracted_address_tip_list[x][3] 
            extracted_address_tip_list[x].pop(3)
        except: IndexError    
        x = x + 1
        


# In[ ]:


### Extract the addresses from no tip list (remove \n)
### Create new no tip list in same format as tip list (index [0] blank, index [1] is address, index [2] is tip.)
def organize_no_tip_list():
    x = 0
    for i in working_notip_list:
        no_tip_list1.append(working_notip_list[x][1:-1])
        x = x + 1
    x = 0
    for i in no_tip_list1:
        no_tip_list2.append(['',no_tip_list1[x],""])
        x = x + 1
    


# In[ ]:


### Combine lists of addresses with tips, and addresses without tips. 
def combine_tip_no_tip():
    for i in extracted_address_tip_list:
        all_address_with_tips.append(i)
    for i in no_tip_list2:
        all_address_with_tips.append(i)
    all_address_with_tips.sort()
    
    try:
        x = 0
        for i in all_address_with_tips:
            if all_address_with_tips[x][1] == all_address_with_tips[x+1][1]:
                final_address_list.append(all_address_with_tips[x+1])
                x = x + 1
            else:
                final_address_list.append(all_address_with_tips[x])
            x = x + 1
    except:
        IndexError
    
    if all_address_with_tips[-1][1] == all_address_with_tips[-2][1]:
        pass
    else:
        final_address_list.append(all_address_with_tips[-1])
    


# In[ ]:


### Create new nested lists of tips.
def split_tips_sublist():
    x = 0 
    for i in final_address_list:
        final_address_list[x][2] = final_address_list[x][2].split(' ')
        x = x + 1
    


# In[ ]:


### Create lists just containing adresses, and all tips for each address. 
def create_address_raw_tip_lists():
    x = 0
    for i in final_address_list:
        if final_address_list[x][1] not in address:
            address.append(final_address_list[x][1])
            raw_tips.append(final_address_list[x][2])
        else:
            pass
        x = x + 1
    x = 0
    for i in raw_tips:
        for e in range(1,max_orders+1):
            raw_tips[x].append('')
        x = x + 1


# In[ ]:


### Create list for the number of orders for each address. 
def extract_num_of_orders_with_data():
    x = 0
    for i in raw_tips:
        num_of_orders_for_address.append(len(raw_tips[x])-max_orders-1)
        if num_of_orders_for_address[x] == 0:
            num_of_orders_for_address[x] = 1 
        x = x + 1


# In[ ]:


### Populating dictionary with tips for each order. 
def seperate_tips():
    for e in range(1,max_orders+1):
        x = 0
        for i in raw_tips:
            tips_dict['tip{0}'.format(e)].append(raw_tips[x][e])
            x = x + 1


# In[ ]:


### Populating dictionary with rip pay and order pay for each order. 
def split_tip_order_pay():
    for i in range(1,max_orders+1):
        x = tips_dict['tip{0}'.format(i)]
        for e in range(0,(len(tips_dict["tip1"]))):
            if x[e] == "":
                tips_pay_dict['tip{0}_tip_pay'.format(i)].append('')
                tips_order_pay_dict['tip{0}_order_pay'.format(i)].append('')
            else:
                x[e] = x[e].split("/")
                tips_pay_dict['tip{0}_tip_pay'.format(i)].append(x[e][0])
                tips_order_pay_dict['tip{0}_order_pay'.format(i)].append(x[e][1])


# In[ ]:


### Calculating percent tip for each order. 
def extract_tips_percent():
    for i in range(1,max_orders+1):
        x = tips_pay_dict['tip{0}_tip_pay'.format(i)]
        y = tips_order_pay_dict['tip{0}_order_pay'.format(i)]
        z = tips_pcent_dict['tip{0}_percent'.format(i)]
        for e in range(0,(len(tips_dict['tip1']))):
            if x[e] == '':
                z.append('') 
            else:
                z.append(round(int(x[e])/int(y[e]),3))


# In[ ]:


### Calculating the average percent tip for all orders at each address. 
def average_tip_by_address():
    global tmp_lst
    tmp_lst = []
    for e in range(0,len(tips_dict['tip1'])):
        for i in range(1,max_orders+1):
            if tips_pcent_dict['tip{0}_percent'.format(i)][e] == '':
                pass
            else:
                tmp_lst.append(tips_pcent_dict['tip{0}_percent'.format(i)][e])
           
    
        if len(tmp_lst) == 0:
            average_tip_by_address_percent.append(0)
        else:
            average_tip_by_address_percent.append(round(sum(tmp_lst)/len(tmp_lst),3))
        tmp_lst = []


# In[ ]:


### Create the Dataframe. 
def populate_df():
    df['Address'] = address
    df['Raw Tips'] = raw_tips
    df['Number of Orders'] = num_of_orders_for_address
    for i in range(1,max_orders+1):
        df['Tip{0}'.format(i)] = tips_dict['tip{0}'.format(i)]
        df['Tip{0} Tip'.format(i)] = tips_pay_dict['tip{0}_tip_pay'.format(i)]
        df['Tip{0} Order Pay'.format(i)] = tips_order_pay_dict['tip{0}_order_pay'.format(i)]
        df['Tip{0} Percent'.format(i)] = tips_pcent_dict['tip{0}_percent'.format(i)]
    df['Average Tip For Address'] = average_tip_by_address_percent


# In[ ]:


### Export the Dataframe. 
def export_df():
    t = input('What would you like to name the .csv?')
    df.to_csv(t)


# In[ ]:


import pandas as pd
import re
df = pd.DataFrame()
n = input('What is the path name for tip list?')
txt = open(n, 'r', encoding="utf-8")
txt_r = txt.read()
m = input("What is the path name for no tip list?")
no_tip_text = open(m, 'r', encoding="utf-8")
no_tip_txt = no_tip_text.read()
txt.close()
no_tip_text.close()
text = '\n' + txt_r
extracted_address_tip_list = []
working_notip_list = []
address = []
raw_tips = []
num_of_orders_for_address = []
no_tip_list1 = []
no_tip_list2 = []
all_address_with_tips = []
final_address_list = []
average_tip_by_address_percent = []

def main():
    regex_pat()
    address_tip_same_line()
    initialize_dicts()
    extract_split_sort_address_tip_list()
    handle_duplicates1()
    handle_duplicates2()
    organize_no_tip_list()
    combine_tip_no_tip()
    split_tips_sublist()
    create_address_raw_tip_lists()
    extract_num_of_orders_with_data()
    seperate_tips()
    split_tip_order_pay()
    extract_tips_percent()
    average_tip_by_address()
    populate_df()
    export_df()


# In[ ]:


main()


# In[ ]:




