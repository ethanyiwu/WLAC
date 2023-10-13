import pandas as pd
from tqdm import trange
input_path = './results/inference_en-de_5-shot.json'
output_path = './final_results/en-de_5-shot.json'
df = pd.read_json(input_path)
prediction = []
for i in trange(len(df)):
    generation = df['generation'][i]
    str_list = generation.split('Answer: ')
    if len(str_list)>1:
        str_list = str_list[1].split(' ')
    else:
        str_list = str_list[0].split(' ')
    correct_prediction = False
    for j in str_list:
        if j.lower().strip().startswith(df['typed_seq'][i].lower()) or j.lower().strip().startswith(('\''+df['typed_seq'][i]).lower()):
            correct_prediction = True
            prediction.append(j)
            break
    if correct_prediction == False:
        prediction.append(str_list[0])
if len(prediction) == len(df):
    df['prediction'] = prediction
    df = df.drop('generation',axis=1)
    df.to_json(output_path,indent=4,orient='records',force_ascii=False)
else:
    print('something wrong!')
#print(prediction[:100])
