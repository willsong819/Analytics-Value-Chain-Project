# Used_Car_Webapp
==============================

This web app predicts used car prices in Germany and Czech Republic markets


Deploy the app locally
------------
```
# Set up a new virtual environment
# Go to folder 'usedcar_webapp' and run
> source ./py/bin/activate
> conda create -n used_car_webapp python=3
> source activate used_car_webapp
> pip install -r requirements.txt

# Run the app
> cd src/models/
> python web_app.py
```


Project Organization
------------

    ├── LICENSE
    │
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    │
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   │
    │   ├── mymodel.p      <- a pickle file that stores the model object
    │   │
    │   ├── web_app.py     <- the main application python file    
    │   │     
    │   ├── static         <- CSS and JavaScript files
    │   │ 
    │   ├── templates      <- HTML file
    │   │   
    │   ├── models         <- Scripts to clean the data and train the model
    │       ├── initial_cleaning.py
    │       └── training_model.py
    │   
    │
    
   
Link to download the data
------------
https://www.kaggle.com/mirosval/personal-cars-classifieds/data


Link to Pivotal Tracker
------------


