# from django.test import TestCase
#
# # Create your tests here.
# # id=1
# # name='Aashutosh Chaudhary'
# # phone='9990502220'
# # account_number='16701530002499'
# # ifsc='HDFC0001670'
# # email='ashugodia@gmail.com'
# # address='B 102 2nd Floor Sushant Lok 3'
# #
# # id=2
# # name='Aashutosh Chaudhary'
# # phone='9990502220'
# # account_number='00000031017243638'
# # ifsc='SBIN0007691'
# # email='ashugodia@gmail.com'
# # address='24 D Teachers Colony'
#
# from workers.models import *
# import payout
#
#
# class PayoutTestCase(TestCase):
#     fixtures = ['workers']
#
#     def setUp(self):
#         pass
#
#     def test_bank_account_validation(self):
#         worker = Worker.objects.first()
#         # self.assertEqual(payout.validate_bank_details(worker.name, '9990502220', worker.account.number,worker.account.ifscode.code),'Bank Account details verified successfully.')
#
