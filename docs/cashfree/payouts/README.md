## Payouts API GUIDE

Please refer to the [Cashfree Docs](https://docs.cashfree.com/docs/)  for the complete API reference.

```diff
- All Optional Arguments Should Be Passed As An Keyword (Named) Arguments
```

#### Initializing Payouts Module

```python
from cashfree_sdk.payouts import Payouts
Payouts.init("<client_id>", "<client_secret>", "PROD")

```

| Option              | Default                       | Description                                                                           |
| ------------------- | ----------------------------- | ------------------------------------------------------------------------------------- |
| `env`        | `TEST`                        | Environment to be initialized. Can be set to `TEST` or `PROD` |
| `client_id` | ``                             | `client_id` which can be generated on cashfree dashboard.                  |
| `client_secret`         | ``                        | `client_secret` which can be found alongside generated `client_id`. |
| `public_key_path`         | `None`                        | `public_key_path` specify the path to your .pem public key file `. |
| `public_key`         | `None`                        | `public_key` Pass your Public Key to this parameter as an alternative to `public_key_path` . | 

### Beneficiary
Contains all APIs related to beneficiary.

##### Initializing Beneficiary
```python
    from cashfree_sdk.payouts.beneficiary import Beneficiary
```

- [Add Beneficiary](https://docs.cashfree.com/docs/payout/guide/#add-beneficiary)
    ##### Optional Arguments - group, bankAccount, ifsc, vpa, cardNo, address2, city, state, pincode
    ```python
    
    bene_add = Beneficiary.add("JOHN18012", "john doe", "johndoe@cashfree.com", "9876543210", "ABC Street", bankAccount="00001111222233", ifsc="HDFC0000001")
    // or
    bene_add = Beneficiary.add(beneId="JOHN18012", name="john doe", email="johndoe@cashfree.com", phone="9876543210", address1="ABC Street", bankAccount="00001111222233", ifsc="HDFC0000001")
    

    ```
- [Get Beneficiary Details](https://docs.cashfree.com/docs/payout/guide/#get-beneficiary-details)
    ```python
    bene_details = Beneficiary.get_bene_details("JOHN18011")
    ```
- [Get Beneficiary Id](https://docs.cashfree.com/docs/payout/guide/#fetch-beneficiary-id)
    ```python
   bene_id = Beneficiary.get_bene_id("00001111222233", "HDFC0000001")
    ```
- [Remove Beneficiary](https://docs.cashfree.com/docs/payout/guide/#fetch-beneficiary-id)
    ```python
   remove_bene = Beneficiary.remove_bene("JOHN18011")
    ```
    
### Transfers
Contains all APIs related to Transfers.
##### Initializing Transfers
#
```python
from cashfree_sdk.payouts.transfers import Transfers
```

- [Request Transfer](https://docs.cashfree.com/docs/payout/guide/#request-transfer)

    ##### Optional Arguments - transferMode, remarks

    ```python
    tnx_req = Transfers.request_transfer(beneId="JOHN18012", amount="100.1", transferId="DEC2017", transferMode="banktransfer", remarks="Test transfer")
    ```

- [Get Transfer Status](https://docs.cashfree.com/docs/payout/guide/#get-transfer-status)
    ```python
    tnx_stats = Transfers.get_transfer_status(referenceId="14057")
    //
    tnx_stats = Transfers.get_transfer_status(transferId="JUNOB2018")
    ```
    
- [Get Transfers](https://docs.cashfree.com/docs/payout/guide/#list-transfers)
    ##### Optional arguments : maxReturn, lastReturnId, date
    ```python
    tnx = Transfers.list_transfers(maxReturn=10)
    ``` 
- [Request Batch Transfer](https://docs.cashfree.com/docs/payout/guide/#batchtransfer-api)
    ##### Optional arguments : deleteBene
    ```python
    entries = [ {"transferId" : "PTM_00121241112", 
	    "amount" : "12",
	    "phone" : "9999999999",
	    "bankAccount" : "9999999999" , 
	    "ifsc" : "PYTM0_000001",
	    "email" : "bahrat@gocashfree.com", 
	    "name": "bharat"},
	    {"transferId" : "PTM_00052312126",
	    "amount" : "12",
	    "phone" : "9999999999", 
	    "bankAccount" : "9999999999" , 
	    "ifsc" : "PYTM0000001",
	    "email" : "bharat@gocashfree.com", 
	    "name": "bharat" },
	    {"transferId" : "PTM_0001321215",
	    "amount" : "12","phone" : "9999999999", 
	    "bankAccount" : "9999999999" , 
	    "ifsc" : "PYTM0000001",
	    "email" : "bahrat@gocashfree.com", "name": "bharat"} ]

    batch_tnx_create = Transfers.create_batch_transfer(batchTransferId="Test_Bank_Account_Format_45", batchFormat="BANK_ACCOUNT", batch=entries, deleteBene=1)
    ```

- [Get Batch Transfer Status](https://docs.cashfree.com/docs/payout/guide/#get-batch-transfer-status-request)
    ```python
    status = Transfers.get_batch_transfer_status(batchTransferId="Test_Bank_Account_Format_45")
    ```

### Validation
Contains all APIs related to Validation.

##### Initializing Validation
#
```python
//Initializing Validation
from cashfree_sdk.payouts.validations import Validations
```
- [Validate Bank Details](https://docs.cashfree.com/docs/payout/guide/#bank-details-validation)
    ```python
    v_det = Validations.bank_details_validation(name="JOHN", phone="9908712345", bankAccount="026291800001191",ifsc="YESB0000262")
    ```

- [Validate UPI Details](https://docs.cashfree.com/docs/payout/guide/#upi-validation)
    ```python
    upi_valid= Validations.upi_validation(name="Cashfree", vpa="success@upi")
    ```

- [Validate Bulk Bank Activation](https://docs.cashfree.com/docs/payout/guide/#bulk-bank-validation-api)
    ```python
    entry = [{ "name":"Sameera Cashfree", "bankAccount":"000890289871772", "ifsc":"SCBL0036078", "phone":"9015991882"},{ "name":"Cashfree Sameera", "bankAccount":"0001001289877623", "ifsc":"SBIN0008752", "phone":"9023991882"}]

    b_valid = Validations.bulk_bank_validation(bulkValidationId="int_test1", entries=entry)
    ```

- [Get Bulk Validation Status](https://docs.cashfree.com/docs/payout/guide/#get-bulkvalidate-status-request)
    ##### Optional : bankAccount, ifsc

    ```python
    status = Validations.get_bulk_bank_validation_status(bulkValidationId="int_test1", bankAccount=
    "0001001289877623", ifsc="SBIN0008752")
    ```

### Cashgram
Contains all APIs related to Cashgram.

##### Initializing Cashgram
#
```python

//Initializing Cashgram
from cashfree_sdk.payouts.cashgram import Cashgram
```

- [Create Cashgram](https://docs.cashfree.com/docs/payout/guide/#cashgram)
    ```python
    c = Cashgram.create_cashgram(cashgramId="JOHaN10", amount="1.1", name="john doe", email="johndoe@cashfree.com", phone="9876543210", 
    linkExpiry="2018/09/12", remarks="api", notifyCustomer=1)  
    ```
    
- [Get Cashgram Status](https://docs.cashfree.com/docs/payout/guide/#get-cashgram-status)
    ```python
   status = Cashgram.get_cashgram_status(cashgramId="JOHaN10")
    ```
    
- [Deactivate Cashgram](https://docs.cashfree.com/docs/payout/guide/#deactivate-cashgram)
    ```python
    d = Cashgram.deactivate_cashgram(cashgramId="JOHaN10")
    ```
    
### Common

- [Get Balance](https://docs.cashfree.com/docs/payout/guide/#get-balance)
    ```python
    b = Transfers.get_balance() 
    ```

- [Self Withdrawal](https://docs.cashfree.com/docs/payout/guide/#self-withdrawal)
    ```python
    withd = Transfers.self_withdrawal(withdrawalId="withdraw1", amount=1.1, remarks="withdrawal request")
    ```