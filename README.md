### Installation
#### Fixtures
##### Load all generic domains e.g gmail.com, rediffmail.com, hotmail.com etc to check email id is valid company email id

```
python3 manage.py createsuperuser
python3 manage.py loaddata core_setting
python3 manage.py loaddata core_domain
```


##### FAQs
> 1. Can we change salary of an employee after sign up.
> Yes we can change salary on sign up day only if customer has not made any withdraw request