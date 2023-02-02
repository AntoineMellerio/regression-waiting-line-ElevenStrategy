# The Endless Line  -  with Eleven Strategy  
  
This project aims at predicting the waiting lines in a theme park and proposing use cases to reduce them.  
It is conducted along with Eleven Strategy.  
  
## Environment
The codes are executed under Python 3.8.16. Other versions may work but have not been tested.  
To make sure everything will work, you can create a conda environment running the following commands :  
`conda create --name eleven-env python=3.8.16`  
`conda activate eleven-env`  

## Packages  
Please run `pip install -r requirements.txt`.  
  
If a conda environment has been created, run the two following commands instead :  
`conda install pip`  
`path_to_env/bin/pip install -r requirements.txt`  
  
## Web app
We provide a dashboard showing the key take-outs of our analysis.  
To generate it, please run `streamlit run Home.py`.
