# Loan Prediction App in Django

## Requirements :
To run this app locally 

``` git clone  https://github.com/debg48/loan-prediction-django.git ```

Install the packages in requirements.txt file

### API Hitpoint :

* Loan Prediction

```localhost:8000/predict/```

### Method :

```POST```

### Body :

``` 
{
    "no_of_dependents" : 2,
        "education" : 1 ,
        "self_employed" :1,
        "income_annum" : 1000,
        "loan_amount" : 10000,
        "loan_term" : 10 ,
        "cibil_score" : 22,
        "residential_assets_value" : 300,
        "commercial_assets_value" :200 ,
        "luxury_assets_value" : 500 ,
        "bank_asset_value" : 200 
}
```
