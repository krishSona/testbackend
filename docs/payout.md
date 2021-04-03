#### Payout
```python
import payout
```

##### Get Balance
```
payout.get_balance()

=> '20000'
```

##### Validate Bank Details
```
import payout

name='Aashutosh Chaudhary'
phone='9990502220'
account_number='00011020001772'
ifsc='HDFC0000001'

payout.validate_bank_details(name,phone,account_number,ifsc)

{'status': 'SUCCESS', 'subCode': '200', 'message': 'Bank Account details verified successfully.', 'data': {'nameAtBank': 'JOHN DOE', 'accountExists': 'YES', 'amountDeposited': '1', 'refId': '13504'}}
```
#### Beneficiaries
##### Add Beneficiary
```
id='1'
name='Aashutosh Chaudhary'
email='ashugodia@gmail.com'
phone='9990502220'
address='B 102 2nd Floor Sushant Lok 3'
account_number='16701530002499'
ifsc='HDFC0001670'

payout.add_beneficiary(id, name, email, phone, address, account_number, ifsc)

=> 'Beneficiary added successfully'

payout.add_beneficiary(id, name, email, phone, address, account_number, ifsc)

=> 'Entered bank account already exist'
```
##### Get Beneficiary Details
```
id='1'

payout.get_beneficiary_details(id)

=> {'id':'1','name':'Aashutosh Chaudhary','email':'ashugodia@gmail.com','phone':'9990502220','address':'B 102 2nd Floor Sushant Lok 3','account_number':'16701530002499','ifsc':'HDFC0001670'}
```
##### Get Beneficiary Id
```
account_number='16701530002499'
ifsc='HDFC0001670'

payout.get_beneficiary_id(account_number, ifsc)

=> '1'
```
##### Remove Beneficiary
```
id='1'

payout.remove_beneficiary(id)

=> 'Beneficiary removed'
```
##### Request Transfer
```python
{'status': 'SUCCESS', 'subCode': '200', 'message': 'Transfer completed successfully', 'data': {'referenceId': '110259', 'utr': '1387420160907000256942', 'acknowledged': 1}}
```

##### Get Transfer Status
```python
{'status': 'SUCCESS', 'subCode': '200', 'message': 'Details of transfer with referenceId 110259', 'data': {'transfer': {'transferId': '4', 'bankAccount': '026291800001191', 'ifsc': 'YESB0000262', 'beneId': '1', 'amount': '1', 'status': 'SUCCESS', 'utr': '1387420160907000256942', 'addedOn': '2020-05-09 16:27:27', 'processedOn': '2020-05-09 16:27:27', 'transferMode': 'FT', 'acknowledged': 1}}}
```