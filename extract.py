import os
from kaggle.api.kaggle_api_extended import KaggleApi

def extract_data(user_name,user_key,dataset_owner,dataset_name, target_path):
 os.environ['KAGGLE_USERNAME'] = user_name
 os.environ['KAGGLE_KEY'] = user_key
 dataset = f"{dataset_owner}/{dataset_name}"
 api = KaggleApi()
 api.authenticate()
 api.dataset_download_files(dataset, path=target_path,unzip=True)
 
if __name__ == "__main__":
    user_name ='xiaonany'
    user_key = '8f63605740f5ba846b03681b1c444b23'
    dataset_owner = 'pavansubhasht'
    dataset_name = 'ibm-hr-analytics-attrition-dataset'
    target_path = "data"
    extract_data(user_name,user_key,dataset_owner,dataset_name, target_path)
