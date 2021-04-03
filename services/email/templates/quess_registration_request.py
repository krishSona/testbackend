
def message(*args):
    html = """
    <html>
    <head><title>Quess Registration Request</title></head>
    <body>
        <div style="text-align: center;">
            <h2>Quess Registration Request</h2>
            <p>Please initialize the registration process of this employee with the following details.:</p>
        </div>
        <div style="margin: 0% 20% 20% 20%;">
            <p>Name: """ + str(args[0][0]) + """</p>
            <p>Employee ID: """ + str(args[0][1]) + """</p>
            <p>Phone: """ + str(args[0][2]) + """</p>
            <p>Company Name: """ + str(args[0][3]) + """</p>
            <p>Net Monthly Salary: """ + str(args[0][4]) + """</p>
            <p>Bank Name: """ + str(args[0][5]) + """</p>
            <p>Account Name: """ + str(args[0][6]) + """</p>
            <p>Bank Account Number: """ + str(args[0][7]) + """</p>
            <p>IFSC Code: """ + str(args[0][8]) + """</p>
            <p>Salary Day: """ + str(args[0][9]) + """</p>
            <p>Company Email Id: """ + str(args[0][10]) + """</p>
            <p>UTM source: """ + str(args[0][11]) + """</p>
            <p>UTM medium: """ + str(args[0][12]) + """</p>
            <p>UTM campaign: """ + str(args[0][13]) + """</p>
        </div>
    </body>
    </html>
    """
    return html
