## Textlocal

#### Handling Receipts

1. **number** - The recipient's mobile phone number.
2. **status** - The delivery status of the message. This will either be: D, U, I, B or ?
3. **customID** - If applicable, the custom ID associated with the message. This can be set by using the custom parameter in send.
4. **datetime** - The datetime the Delivery Receipt was received from the operator. In MySQL datetime format.

#### Message Delivery Status

- **D** Message was delivered successfully.
- **U** The message was undelivered.
- **P** Message pending, the message is en route.
- **I** The number was invalid.
- **E** The message has expired.
- **?** Message pushed to networks, the message is en route.
- **B** Blocked, this number has been blocked by the DND.

#### Message Responses

1. {"errors":[{"code":7,"message":"Insufficient credits"}],"status":"failure"}
2. {"errors"=>[{"code"=>43, "message"=>"Invalid sender name"}], "status"=>"failure"}
3. {"warnings"=>[{"message"=>"Number is in DND", "numbers"=>"919990502220"}], "errors"=>[{"code"=>51, "message"=>"No valid numbers specified"}], "status"=>"failure"}
4. {"balance"=>9, "batch_id"=>856238493, "cost"=>1, "num_messages"=>1, "message"=>{"num_parts"=>1, "sender"=>"", "content"=>"Testing"}, "receipt_url"=>"", "custom"=>"", "messages"=>[{"id"=>"11147307804", "recipient"=>918882520015}], "status"=>"success"}
5. {"errors"=>[{"code"=>7, "message"=>"Insufficient credits"}], "status"=>"failure"}
6. {"errors"=>[{"code"=>204, "message"=>"Invalid message content"}], "status"=>"failure"}
7. {"status"=>"failure", "errors"=>"<html>\r\n<head><title>502 Bad Gateway</title></head>\r\n<body>\r\n<center><h1>502 Bad Gateway</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n"}

## Kaleyra

#### GET Send an SMS

```
curl --location --request POST 'https://api-alerts.kaleyra.com/v4/?api_key=A75bXXXXXXXXXXXXXX&method=sms&message=hello&to=974xxxx&sender=KALERA'
```

Response

```
{
  "status": "OK",
  "data": [
    {
      "id": "811436f5-0053-4ea6-8cac-b035880b8473:1",
      "customid": "1",
      "customid1": "11",
      "customid2": "22",
      "mobile": "95XXXXXXXXX",
      "status": "AWAITED-DLR"
    },
    {
      "id": "811436f5-0053-4ea6-8cac-b035880b8473:2",
      "customid": "2",
      "customid1": "1",
      "customid2": "2",
      "mobile": "97XXXXXXXX",
      "status": "AWAITED-DLR"
    }
  ],
  "message": "Campaign of 2 numbers Submitted successfully."
}
```
