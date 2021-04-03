def auto_credited_notification(*args):
    message = "Tap here to check Salary Wallet balance"
    return message


def transfer_to_bank(*args):
    message = "Rs." + str(args[0][0]) + " transferred to your bank account"
    return message


def month_end_notification(*args):
    message = "Your Salary Wallet balance will automatically " \
              "expire at month end. Tap here to withdraw money from your Wallet."
    return message
