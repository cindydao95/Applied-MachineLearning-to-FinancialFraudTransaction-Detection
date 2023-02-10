import pickle5 as pickle
import json
import numpy as np

#write function to transform the input data from user 
def transform_text(text):
    text = text.upper()
    new_text = ''
    for i in text.split():
        new_text = new_text+i+'-'
    return new_text



def transform_input_data(raw_data, scalar):#list
    #input_data is dict type
    output_datas = {}
    for k in raw_data:
        value = raw_data[k]
        #category_value = transform_text(category_value)
        if 'Sender' in k:
            value = transform_text(value)
            transformed_value = value + 'sender'
        elif 'Bene' in k:
            value = transform_text(value)
            transformed_value = value + 'bene'
        elif k == 'USD_Amount':
            transformed_value = scalar.transform(np.array(value).reshape(1,-1))[0][0]
        else:
            transformed_value = transform_text(value).rstrip('-')
        output_datas[k] = transformed_value
    
    return output_datas #dict

#write function to encode the data



#user_data = transformed data result from transform_input_data
def encode_user_data(user_data,init_data):
    for k in user_data:
        if k == "Sender_Country":
            for k1 in init_data:
                if k1 in user_data.values():
                    init_data[k1] = 1
                else:
                    init_data['other-sender']=1

        elif k == "Bene_Country":
            for k1 in init_data:
                if k1 in user_data.values():
                    init_data[k1] = 1
                else:
                    init_data['other-bene'] = 1 

        else:
            for k1 in init_data:
                if k1 in user_data.values():
                    init_data[k1] = 1
                
    init_data['USD_amount'] = user_data["USD_Amount"]
    encoded_data = init_data
    return encoded_data



