#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os
import json
import pandas as pd


# In[22]:


listt=[{'2':'dd','3':'44'}]


# In[23]:


if listt[0]['2']!='NULL':
    print(listt)


# In[24]:


def counting(path):
    cnt = 0
    data_dir = path

    for path in os.listdir(data_dir):
        if os.path.isfile(os.path.join(data_dir, path)):
            cnt += 1

    print(f'데이터 개수 = {cnt}')
    return cnt


# In[25]:


target_path = '021.용도별 목적대화 데이터/01.데이터/1.Training/라벨링데이터/TL_2/'


# In[26]:


target_path_list = os.listdir(target_path)


# In[27]:


target_path_list


# In[28]:


os.getcwd()


# In[29]:


total_data = 0
for i in range(len(target_path_list)):
    cnt = counting(target_path+target_path_list[i])
    total_data += cnt
print(f'총 데이터 개수 = {total_data}')


# In[30]:


# 환불 반품 교환 a b구분용
''' 
purpose = []
an=[]
for i in range(len(target_path_list)):
    files = os.listdir(target_path+target_path_list[i])
    for k in range(len(files)):
        final_path = str(target_path)+str(target_path_list[i])+"/"+str(files[k])
        try:
            target_file = open(f"{final_path}", encoding="UTF-8")
            target_file = json.loads(target_file.read())
           
            for j in range(len(target_file['info'][0]['annotations']['lines'])):
                if j==0:
                    if target_file['info'][0]['annotations']['lines'][j]['norm_text'][0]=='A':
                        purpose.append(target_file['info'][0]['annotations']['lines'][j]['norm_text'][2:])
                    elif target_file['info'][0]['annotations']['lines'][j]['norm_text'][0]=='B':
                        a.append(target_file['info'][0]['annotations']['lines'][j]['norm_text'][2:])
                if target_file['info'][0]['annotations']['lines'][j-1]['norm_text'][0]=='A':
                    if target_file['info'][0]['annotations']['lines'][j]['norm_text'][0]=='A':
                        purpose[-1]=(purpose[-1]+' '+target_file['info'][0]['annotations']['lines'][j]['norm_text'][2:])
                    elif target_file['info'][0]['annotations']['lines'][j]['norm_text'][0]=='B':
                        an.append(target_file['info'][0]['annotations']['lines'][j]['norm_text'][2:])
                elif target_file['info'][0]['annotations']['lines'][j-1]['norm_text'][0]=='B':
                    if target_file['info'][0]['annotations']['lines'][j]['norm_text'][0]=='B':
                        an[-1]=an[-1]+' '+target_file['info'][0]['annotations']['lines'][j]['norm_text'][2:]
                    elif target_file['info'][0]['annotations']['lines'][j]['norm_text'][0]=='A':
                        purpose.append(target_file['info'][0]['annotations']['lines'][j]['norm_text'][2:])
        except:
            print(f"error! {final_path}")


# In[31]:


#대화 attention

purpose = []
an=[]
for i in range(len(target_path_list)):
    files = os.listdir(target_path+target_path_list[i])
    for k in range(len(files)):
        final_path = str(target_path)+str(target_path_list[i])+"/"+str(files[k])
        try:
            target_file = open(f"{final_path}", encoding="UTF-8")
            target_file = json.loads(target_file.read())
            for j in range(len(target_file['info'][0]['annotations']['lines'])):
                if target_file['info'][0]['annotations']['lines'][j]['norm_text'][0]!=target_file['info'][0]['annotations']['lines'][j+1]['norm_text'][0]:
                    purpose.append(target_file['info'][0]['annotations']['lines'][j]['norm_text'][2:])
                    an.append(target_file['info'][0]['annotations']['lines'][j+1]['norm_text'][2:])
        except:
            print(f"error! {final_path}")
            


# In[32]:


#왜 위와 같은 구조로 값을 뽑아 내었나?
'''이는 실제 대화내용을 기반으로 작성되었다. 그렇기에 화자가 둘이라고 가정한다면 A B가 있을 것이다
하지만 라벨링 되어 있는 구조기에 한 문장단위로 끊어 져있다 그렇기에 대화가 
ABAAABB와 같다고 할 때, 실질적인 질문과 답은 AB이거나 BA인 경우에 발생할 것이다.
즉, 답이 질문이 될 수도 있다. 그렇기에 다음과 같이 구현하였다
물론 AAB와 같이 AA의 모든 내용이 B라는 답을 구현 했을 수도 있다.
하지만 학습시키기에 양이 많아서, 필수 질문만 넣었다
'''


# In[ ]:





# In[33]:


len(purpose)


# In[34]:


len(an)


# In[35]:


q_df = pd.DataFrame({'q':purpose})


# In[36]:


q_df.tail()


# In[37]:


print(q_df)


# In[38]:


a_df = pd.DataFrame({'a':an})
a_df.tail()


# In[19]:


#a_df.to_csv("./refund_v2_a.csv", index=False)


# In[20]:


#q_df.to_csv("./refund_v2_q.csv", index=False)


# In[ ]:





# In[ ]:




