### Introduction
Bank account verification is a sub-service of Cashfree payouts that allows a merchant to verify their end customer's bank details.
#### Usage
```python
from cashfree_sdk.payouts import Payouts
from cashfree_sdk.payouts.validations import Validations

clientId = "your_client_id"
clientSecret = "your_client_secret"
env = "TEST"

 Payouts.init(clientId, clientSecret, env)
```
```python
{"status":"SUCCESS", 
"message":"Token generated", 
"subCode":"200", 
"data": {"token":"eyJ0eXA...fWStg", "expiry":1564130052}
}
```
```python
bank_validation_result = Validations.bank_details_validation(
        name = "sameera",
        phone = "9000000000",
        bankAccount = "026291800001191",
        ifsc = "YESB0000262"
    )
```
```python
{ "status": "SUCCESS", 
"subCode": "200", 
"message": "Amount Deposited Successfully", 
"data": { "nameAtBank": "John Barnes Smith", "accountExists": "YES", "amountDeposited": "1.28", "refId": "5a7da061af50584d5992b2" } }
```
#### Responses
- Status
    1. Success
        * Name at Bank - [NA, UNREGISTERED]
        * Account No.
        * IFSC
        * Subcode - 200
        * Message
            1. Bank Account details verified successfully.
            2. Invalid account number or ifsc provided.
    2. Error
        * Name at Bank - NA
        * Account No.
        * IFSC
        * Subcode
        * Message
            1. 520 - Service temporarily unavailable.Please try again later.
            2. 520 - Could not verify bank account details.
            3. 520 - Validation attempt failed.
            4. 412 - Insufficient balance to process this request