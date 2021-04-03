
def message(*args):
    body = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Daily Salary</title>
        <meta property="og:title" content="%%subject%%">
        <style>
          @media only screen and (min-width:1024px) {
            .template-section-note .template-section-note-p {
              margin: 0 2em
            }
            .h-1--md {
              font-size: 40px;
              line-height: 43px
            }
            .h-2--md {
              font-size: 32px;
              line-height: 40px
            }
            .h-3--md {
              font-size: 27px;
              line-height: 36px
            }
            .h-4--md {
              font-size: 24px;
              line-height: 32px
            }
            .h-5--md {
              font-size: 21px;
              line-height: 27px
            }
            .h-6--md {
              font-size: 18px;
              line-height: 27px
            }
            .h-7--md {
              font-size: 16px;
              line-height: 24px
            }
            .h-8--md {
              font-size: 14px;
              line-height: 20px
            }
            .h-9--md {
              font-size: 12px;
              line-height: 14px
            }
            .h-1--md {
              font-size: 40px;
              line-height: 43px
            }
            .h-2--md {
              font-size: 32px;
              line-height: 40px
            }
            .h-3--md {
              font-size: 27px;
              line-height: 36px
            }
            .h-4--md {
              font-size: 24px;
              line-height: 32px
            }
            .h-5--md {
              font-size: 21px;
              line-height: 27px
            }
            .h-6--md {
              font-size: 18px;
              line-height: 27px
            }
            .h-7--md {
              font-size: 16px;
              line-height: 24px
            }
            .h-8--md {
              font-size: 14px;
              line-height: 20px
            }
            .h-9--md {
              font-size: 12px;
              line-height: 14px
            }
          }
          @media only screen and (min-width:600px) {
            .h-1--sm {
              font-size: 40px;
              line-height: 43px
            }
            .h-2--sm {
              font-size: 32px;
              line-height: 40px
            }
            .h-3--sm {
              font-size: 27px;
              line-height: 36px
            }
            .h-4--sm {
              font-size: 24px;
              line-height: 32px
            }
            .h-5--sm {
              font-size: 21px;
              line-height: 27px
            }
            .h-6--sm {
              font-size: 18px;
              line-height: 27px
            }
            .h-7--sm {
              font-size: 16px;
              line-height: 24px
            }
            .h-8--sm {
              font-size: 14px;
              line-height: 20px
            }
            .h-9--sm {
              font-size: 12px;
              line-height: 14px
            }
            .h-1--sm {
              font-size: 40px;
              line-height: 43px
            }
            .h-2--sm {
              font-size: 32px;
              line-height: 40px
            }
            .h-3--sm {
              font-size: 27px;
              line-height: 36px
            }
            .h-4--sm {
              font-size: 24px;
              line-height: 32px
            }
            .h-5--sm {
              font-size: 21px;
              line-height: 27px
            }
            .h-6--sm {
              font-size: 18px;
              line-height: 27px
            }
            .h-7--sm {
              font-size: 16px;
              line-height: 24px
            }
            .h-8--sm {
              font-size: 14px;
              line-height: 20px
            }
            .h-9--sm {
              font-size: 12px;
              line-height: 14px
            }
          }
          @media only screen and (min-width:1440px) {
            .h-1--lg {
              font-size: 40px;
              line-height: 43px
            }
            .h-2--lg {
              font-size: 32px;
              line-height: 40px
            }
            .h-3--lg {
              font-size: 27px;
              line-height: 36px
            }
            .h-4--lg {
              font-size: 24px;
              line-height: 32px
            }
            .h-5--lg {
              font-size: 21px;
              line-height: 27px
            }
            .h-6--lg {
              font-size: 18px;
              line-height: 27px
            }
            .h-7--lg {
              font-size: 16px;
              line-height: 24px
            }
            .h-8--lg {
              font-size: 14px;
              line-height: 20px
            }
            .h-9--lg {
              font-size: 12px;
              line-height: 14px
            }
            .h-1--lg {
              font-size: 40px;
              line-height: 43px
            }
            .h-2--lg {
              font-size: 32px;
              line-height: 40px
            }
            .h-3--lg {
              font-size: 27px;
              line-height: 36px
            }
            .h-4--lg {
              font-size: 24px;
              line-height: 32px
            }
            .h-5--lg {
              font-size: 21px;
              line-height: 27px
            }
            .h-6--lg {
              font-size: 18px;
              line-height: 27px
            }
            .h-7--lg {
              font-size: 16px;
              line-height: 24px
            }
            .h-8--lg {
              font-size: 14px;
              line-height: 20px
            }
            .h-9--lg {
              font-size: 12px;
              line-height: 14px
            }
          }
          @media only screen and (min-width:1920px) {
            .h-1--xl {
              font-size: 40px;
              line-height: 43px
            }
            .h-2--xl {
              font-size: 32px;
              line-height: 40px
            }
            .h-3--xl {
              font-size: 27px;
              line-height: 36px
            }
            .h-4--xl {
              font-size: 24px;
              line-height: 32px
            }
            .h-5--xl {
              font-size: 21px;
              line-height: 27px
            }
            .h-6--xl {
              font-size: 18px;
              line-height: 27px
            }
            .h-7--xl {
              font-size: 16px;
              line-height: 24px
            }
            .h-8--xl {
              font-size: 14px;
              line-height: 20px
            }
            .h-9--xl {
              font-size: 12px;
              line-height: 14px
            }
            .h-1--xl {
              font-size: 40px;
              line-height: 43px
            }
            .h-2--xl {
              font-size: 32px;
              line-height: 40px
            }
            .h-3--xl {
              font-size: 27px;
              line-height: 36px
            }
            .h-4--xl {
              font-size: 24px;
              line-height: 32px
            }
            .h-5--xl {
              font-size: 21px;
              line-height: 27px
            }
            .h-6--xl {
              font-size: 18px;
              line-height: 27px
            }
            .h-7--xl {
              font-size: 16px;
              line-height: 24px
            }
            .h-8--xl {
              font-size: 14px;
              line-height: 20px
            }
            .h-9--xl {
              font-size: 12px;
              line-height: 14px
            }
          }
          @media only screen and (max-width:599px) {
            a {
              -webkit-text-size-adjust: none !important
            }
            blockquote {
              -webkit-text-size-adjust: none !important
            }
            body {
              -webkit-text-size-adjust: none !important
            }
            li {
              -webkit-text-size-adjust: none !important
            }
            p {
              -webkit-text-size-adjust: none !important
            }
            table {
              -webkit-text-size-adjust: none !important
            }
            td {
              -webkit-text-size-adjust: none !important
            }
            body {
              width: 100% !important;
              min-width: 100% !important
            }
            h1 {
              font-size: 20px !important
            }
            h1 {
              line-height: 135% !important
            }
            h2 {
              line-height: 135% !important
            }
            h2 {
              font-size: 18px !important
            }
            h3 {
              font-size: 16px !important
            }
            h3 {
              line-height: 135% !important
            }
            h4 {
              line-height: 135% !important
            }
            h4 {
              font-size: 14px !important
            }
            #bodyCell {
              padding: 10px !important
            }
            .circleIcon {
              max-width: 30px !important
            }
            .threeColumnLayout .templateColumnContainer {
              display: block !important;
              padding: 10px !important;
              width: 93% !important
            }
            .threeColumnLayout .templateColumnContainer .centerColumnContent {
              font-size: 16px !important;
              line-height: 135% !important
            }
            .threeColumnLayout .templateColumnContainer .leftColumnContent {
              font-size: 16px !important;
              line-height: 135% !important
            }
            .threeColumnLayout .templateColumnContainer .rightColumnContent {
              font-size: 16px !important;
              line-height: 125% !important
            }
            .threeColumnLayout .columnImage {
              height: auto !important;
              width: 135% !important
            }
            .footerContent {
              font-size: 14px !important;
              line-height: 115% !important;
              padding-left: 5px !important
            }
            .footerContent a {
              display: block !important
            }
            .socialContainer {
              min-width: 75px !important;
              padding-right: 15px !important
            }
            .noIndent {
              margin-left: 0 !important
            }
            img.hero-image {
              width: 100% !important
            }
            .template-footer-details {
              font-size: 9px !important
            }
            .template-footer-social {
              width: 25% !important
            }
            .mobile-br {
              display: block !important
            }
            .template-padding {
              padding-left: 15px !important;
              padding-right: 15px !important
            }
          }
        </style>
      </head>
      <body style="color: #525257; background-color: #fff; font-family: Arial; font-size: 1em; padding-top: 0; padding-right: 0; padding-bottom: 0; padding-left: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; margin-top: 0; margin-right: auto; margin-bottom: 0; margin-left: auto; position: relative; height: 100% !important; width: 100% !important;" bgcolor="#fff">
        <span class="preheader" style="color: transparent; display: none; height: 0; max-height: 0; max-width: 0; opacity: 0; overflow: hidden; mso-hide: all; visibility: hidden; width: 0;">
          </span>
        <table id="bodyTable" style="border-spacing: 20px; border-collapse: collapse; font-family: Arial; font-size: 16px; color: #525257; background-color: #fff; margin-top: 0; margin-right: 0; margin-bottom: 0; margin-left: 0; padding-top: 0; padding-right: 0; padding-bottom: 0; padding-left: 0; height: 100% !important; width: 100% !important;" bgcolor="#fbfafa" width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td align="center" valign="top" style="border-collapse: collapse; padding-top: 0; padding-right: 0; padding-bottom: 0; padding-left: 0;">
              <table class="template-section" style="border-spacing: 20px; border-collapse: collapse; width: 100%; max-width: 620px;" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td align="center" valign="top" class="template-section-container" style="border-collapse: collapse; padding-top: 0; padding-bottom: 0; padding-left: 10px; padding-right: 10px;">
                    <table id="templateHeaderLogo" style="border-spacing: 20px; width: 100%; border-collapse: collapse;" width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <div id="mail-text" style="text-align: left; margin-top: 30px; margin-bottom: 30px;">
                            <p>Hi """ + str(args[0][0]) + """,</p>
                            <p>Today's salary of <b><span style="font-family: DejaVu Sans;">&#x20b9;</span>""" + str(args[0][1]) + """</b> has been credited to your Salary Wallet.</p>
                            <p>You now have <b><span style="font-family: DejaVu Sans;">&#x20b9;</span>""" + str(args[0][2]) + """</b> in your Salary Wallet.</p>
                        </div>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td align="center" valign="top" style="border-collapse: collapse; padding-top: 0; padding-right: 0; padding-bottom: 0; padding-left: 0;">
              <table class="template-section" style="border-spacing: 20px; border-collapse: collapse; width: 100%; max-width: 620px;" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td align="center" valign="top" class="template-section-container" style="border-collapse: collapse; padding-top: 0; padding-bottom: 0; padding-left: 10px; padding-right: 10px;">
                    <table id="templateHeader" style="border-spacing: 20px; width: 100%; border-collapse: collapse;" width="100%" cellpadding="0" cellspacing="0" border="0">
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td align="center" valign="top" style="border-collapse: collapse; padding-top: 0; padding-right: 0; padding-bottom: 0; padding-left: 0;">
              <table class="template-section" style="border-spacing: 20px; border-collapse: collapse; width: 100%; max-width: 620px;" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td align="center" valign="top" class="template-section-container" style="border-collapse: collapse; padding-top: 0; padding-bottom: 0; padding-left: 10px; padding-right: 10px;">
                    <table id="templateBody" style="width: 100%; border-collapse: separate; border-spacing: 0;" width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td class="template-body-content" align="center" valign="top" style="box-shadow: 0px 10px 10px #e2e2e2; border-collapse: collapse; border-top-color: #dcdcdc; border-right-color: #dcdcdc; border-bottom-color: #dcdcdc; border-left-color: #dcdcdc; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-radius: 5px; overflow: hidden; background-color: #fff;" bgcolor="#fff">
                          <table style="border-spacing: 20px; width: 100%; border-collapse: collapse;" width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td class="template-header-logo-body" align="center" valign="top" style="border-collapse: collapse; padding-top: 20px; padding-right: 0; padding-bottom: 30px; padding-left: 0;">
                          <div style="font-size: 20px; font-weight: normal; color:#B8860B; padding-bottom: 20px;">DAILY <strong>SALARY</strong></div>
                          <img class="ob-header-img-sm" src="cid:auto_credited" style="max-width: 25%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; width: 150px; height: auto; display: block; margin-top: 0; margin-right: auto; margin-bottom: 0px; margin-left: auto;">
                        </td>
                      </tr>
                            <tr>
                              <td style="border-collapse: collapse; padding-top: 0; padding-right: 0; padding-bottom: 0; padding-left: 0;">
                                <div class="ob-template-header" style="margin-bottom: 0px; margin-top: 0px;">
                                  <div style="padding-top: 0; padding-right: 0; padding-bottom: 0; padding-left: 0; font-style: normal; font-weight: bold; letter-spacing: normal; color: #111; font-size: 20px; line-height: 24px; max-width: 360px; margin-top: 0px; margin-right: auto; margin-bottom: 10px; margin-left: auto; text-align: center;" align="center">SALARY WALLET</div>
                                </div>
                                <div class="ob-template-content text-center" style="max-width: 360px; margin-top: 0; margin-right: auto; margin-bottom: 0; margin-left: auto; padding-top: 0; padding-right: 0; padding-bottom: 40px; padding-left: 0; text-align: center !important;" align="center">
                                  <div style="font-size: 4px; font-weight: normal; margin-top: 0; line-height: 1; margin-right: 0; margin-bottom: 15px; margin-left: 0; color: #111;">
                                    <span style="font-family: DejaVu Sans;font-size: 40px;">&#x20b9;</span><b style="font-size: 60px; font-weight: bold;"> """ + str(args[0][2]) + """</b>
                                  </div>
                                  <div class="transfer_button_cont" style="text-align: center; margin: auto;">
                                  <a class="transfer_button" href="https://dailysalary.in/app/wallet" style="width: 70%; padding: 3%; border-radius: 100px; background: #B8860B; color: #fff; font-size: 15px; margin: auto; margin-top: 10px; margin-bottom: 15px; display: block; text-decoration: none;">Transfer Salary to Bank</a>
                                      <div style="font-size: 15px; font-weight: normal; line-height: 1.6em; margin-top: 0; margin-right: 0; margin-left: 0; margin-bottom: 0; padding-bottom: 0;">
                                        Use the Daily Salary app to transfer your salary<br>to your bank.
                                      </div>
                                  </div>
                                </div>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td align="center" valign="top" style="border-collapse: collapse; padding-top: 0; padding-right: 0; padding-bottom: 0; padding-left: 0;">
              <table class="template-section" style="border-spacing: 20px; border-collapse: collapse; width: 100%; max-width: 620px;" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td align="center" valign="top" class="template-section-container" style="border-collapse: collapse; padding-top: 0; padding-bottom: 0; padding-left: 15px; padding-right: 15px;">
                    <table id="newTemplateFooter" style="border-spacing: 20px; width: 100%; border-collapse: collapse;" width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td class="template-footer-content" align="center" valign="top" style="border-collapse: collapse; padding-right: 0; padding-left: 0; padding-top: 30px; padding-bottom: 35px;">
                          <div class="template-footer-gusto-header" style="font-weight: 400; line-height: 1.2em; font-size: 14px; margin-top: 0; margin-right: 0; margin-bottom: 5px; margin-left: 0; color: #1c1c1c;"><b>Daily Salary</b></div>                      
                          <p style="font-weight: 400; line-height: 1.6em; font-size: 14px; margin-top: 0; margin-right: 0; margin-bottom: 15px; margin-left: 0;"><small>© NSquared Systems Pvt. Ltd., InstaOffice, 301/302, 3rd Floor, Good Earth City Center, Sector 50, Gurugram, Haryana, India - 122002</small></p>
                          <p style="font-weight: 400; line-height: 1.6em; font-size: 14px; margin-bottom: 0; margin-top: 0; margin-right: 0; margin-left: 0;"><small>You received this email because you have registered on Daily Salary.</small></p>
                              <p style="font-family: Arial; text-align: center; font-size: 11px;">
                                <a href="https://dailysalary.in/unsubscribe/?unsubscribe_token=""" + str(args[0][3]) + """">Unsubscribe</a>
                            </p>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
        </body>
    </html>
    """
    return body
