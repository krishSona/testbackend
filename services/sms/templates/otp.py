def login(*args):
    return 'Hello! Your OTP for login is ' + str(args[0][0]) + '. And this OTP is valid for 2 minutes only.'


def statement(*args):
    return 'Hello! Your OTP for withdrawal is ' + str(args[0][0]) + '. And this OTP is valid for 2 minutes only.'


def play_store_link(*args):
    return 'Hi ' + str(args[0][0]) + '! Your Daily Salary Wallet has been activated.' \
              ' Click this link to install your Salary Wallet. ' + str(args[0][1]) + ' Customer Care: +91 8826333239'

