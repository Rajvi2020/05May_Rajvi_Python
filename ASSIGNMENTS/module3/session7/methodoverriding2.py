class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):      
        print("Sending email notification")


class SMSNotification(Notification):
    def send(self):      
        print("Sending SMS notification")

email = EmailNotification()
sms = SMSNotification()
email.send()
sms.send()

#Method overriding allows a child class to redefine a method of the parent class with the same name, so each child class provides its own implementation.
