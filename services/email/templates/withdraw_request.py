def message(*args):
    msg = """New Withdraw Request:
    """ + "\n" \
              "Name: " + str(args[0][0]) + "\n" +\
              "Amount: " + str(args[0][1]) + "\n" +\
              "Bank Name: " + str(args[0][2]) + "\n" +\
              "Bank Account Number: " + str(args[0][3]) + "\n" + \
              "IFSC Code: " + str(args[0][4]) + "\n" + \
              "ID: " + str(args[0][5])
    return msg
