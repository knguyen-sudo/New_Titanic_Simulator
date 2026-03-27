import kaggle 
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_files('yasserh/titanic-dataset', path='.', unzip=True)

api.dataset_metadata('yasserh/titanic-dataset', path='.')

# try:
#     import kaggle
#     print("kAGGLE IS INSTALL")
# except ImportError:
#     print("kAGGLE IS NOT INSTALL")