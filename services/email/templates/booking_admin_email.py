def message(*args):
    html = """
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
                            <p>Hi admin,</p>
                            <p>Please check """ + str(args[0][0]) + """ has registered on our Daily Salary portal.</p>
                            <p>Details are i.e. : </p>
                            <p>Company Name: """ + str(args[0][1]) + """</p>
                            <p>Email: """ + str(args[0][2]) + """</p>
                            <p>Mobile No: """ + str(args[0][3]) + """</p>
                            <p>Please contact as soon as possible!</p>
                        </div>
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
    return html
