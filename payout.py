from cashfree_sdk.payouts import Payouts
from cashfree_sdk.payouts.validations import Validations
from cashfree_sdk.payouts.beneficiary import Beneficiary
from cashfree_sdk.payouts.transfers import Transfers
from cashfree_sdk.exceptions import exceptions
import json
import re


def initialize():
    try:
        Payouts.init('CF8596D2125MM8G66AQAY', '8eba07528682962556c6dd4f9c84b278664d4283', 'TEST')
        # Payouts.init("CF27870FMPD32Z3L7IQQ22",
        #              "7c27c6ebf9d31091bd9034a0f0887442792a9ad7", "PROD")
    except ConnectionError:
        return None


def get_balance():
    if not authenticated():
        return None
    try:
        response = _json(Transfers.get_balance())
        return response['data']['balance']
    except ConnectionError:
        return None


def validate_bank_details(name, phone, account_number, ifsc):
    try:
        response = _json(
            Validations.bank_details_validation(name=name, phone=phone, bankAccount=account_number, ifsc=ifsc))
        if response['status'] == 'SUCCESS':
            _response = response['message']
    except exceptions.InputWrongFormatError:
        _response = 'Validation Not Enabled'
    except exceptions.UnknownErrorOccurredError as exception:
        # pdb.set_trace()
        _response = 'Service temporarily unavailable.Please try again later'
    return _response


# Beneficiaries
def add_beneficiary(beneficiary_id, name, email, phone, address, account_number, ifsc):
    try:
        response = _json(
            Beneficiary.add(beneId=beneficiary_id, name=name, email=email, phone=phone, address1=address,
                            bankAccount=account_number, ifsc=ifsc))
    except exceptions.AlreadyExistError:
        return 'Entered bank account already exist'
    return response['message']


def get_beneficiary_details(beneficiary_id):
    beneficiary_id = str(beneficiary_id)
    response = _json(Beneficiary.get_bene_details(beneficiary_id))
    if response['status'] == 'SUCCESS':
        _response = {'beneficiary_id': response['data']['beneId'], 'name': response['data']['name'],
                     'email': response['data']['email'], 'phone': response['data']['phone'],
                     'address': response['data']['address1'], 'account_number': response['data']['bankAccount'],
                     'ifsc': response['data']['ifsc']}
    return _response


def get_beneficiary_id(account_number, ifsc):
    response = _json(Beneficiary.get_bene_id(account_number, ifsc))
    if response['status'] == 'SUCCESS':
        _response = response['data']['beneId']
    return _response


def remove_beneficiary(beneficiary_id):
    beneficiary_id = str(beneficiary_id)
    response = _json(Beneficiary.remove_bene(beneficiary_id))
    if response['status'] == 'SUCCESS':
        _response = response['message']
    return _response


# Transfers
def request_transfer(beneficiary_id, amount, transfer_id, transfer_mode, remarks):
    try:
        _response = _json(Transfers.request_transfer(beneId=beneficiary_id, amount=amount, transferId=transfer_id,
                                                     transferMode=transfer_mode, remarks=remarks))
        if _response == 'Not enough available balance in the account':
            _response = {
                'message': 'Not enough available balance in the account'}
    except exceptions.InputWrongFormatError as e:
        # _response = 'Invalid bank account number or ifsc provided'
        _response = _exception(e)
    except exceptions.BadRequestError as e:
        _response = _exception(e)
    return _response


def get_transfer_status(transfer_id):
    try:
        _response = _json(
            Transfers.get_transfer_status(transferId=transfer_id))
    except:
        pass
    return _response


def _json(response):
    return json.loads(response._content.decode('utf-8'))


def _exception(e):
    search = re.search('^Reason = .*::', str(e))
    text = search.group()
    if text is not None:
        return text[9:-2]


def authenticated():
    return False


initialize()
