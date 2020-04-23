<p align="center">
  <img height="150" src="./assets/jolyu.svg">
</p>

# Jolyu webpage

Codebase for the webpage used in the elsys project Jolyu.

## Dash

The webpage is built upon the framework dash, and is used to display data from a bird counter station.'

## Install

```python
pip install -r requirements.txt
python3 app.py
```

This should install all that is needed for the project to run.

## Datagen

In the folder [data](data/) there two scrips for generating data. One generates for [csv](data/dataGenToCSV.py), and the other generates for [JSON](data/dataGenToDatabase.py) (this is most updated, and generates distorted sinuses).

