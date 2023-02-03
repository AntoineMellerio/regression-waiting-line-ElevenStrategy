![Alt text](./images/banner_page2.jpeg?raw=true "Banner")

# The Endless Line  -  with Eleven Strategy  
  
This project aims at predicting the waiting lines in a theme park and proposing use cases to reduce them.  
It is conducted along with Eleven Strategy.  
  
## Environment
The codes are executed under Python 3.8.16. Other versions may work but have not been tested.  
To make sure everything will work, create a conda environment running the following commands :  
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
  
The app is composed of 4 pages :  
1. Homepage : presentation of the project and the team.  
2. Overview : global insights on the parks' performances (attendance and waiting times).  
3. Deep-diving : per attraction figures and predictions on the waiting times, at both daily and hourly granularities.   
4. Next steps : next steps to the predictive model and use-cases suggestions.  
