from Bot import SmsBot
query = SmsBot.sms("username","password") # username is usually Mobile Number (Logging in)
my_message=input("Enter Your Message")
query.send("recipient",my_message) # recipient = receiver's number
query.Logout()
