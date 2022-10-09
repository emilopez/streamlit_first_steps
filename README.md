# Learning streamlit


## Install

Create environment and install dependencies:

### Using conda

```
conda create --no-default-packages --name lst python=3.8.10
conda activate lst
conda install --yes --file requirements.txt
```

### Using venv

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

Run one of the py scripts, for example:

```streamlit run streamlit_test4.py```

## WebApp

Test the streamlit_test4.py:
- Go to https://emilopez-streamlit-first-steps-streamlit-test4-hdd9m9.streamlitapp.com/ 
- Use `datos/altura_estaciones.csv` as the input file
- Pick a valid date from the calendar (ie 2019-07-02)  
