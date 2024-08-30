import smtplib

server = "smtp.gmail.com"
port = 587  # connect to the server

sender = "nirjala.dhl55@gmail.com"
password = "rygh jjfz xxis rfwv"

receiver = input("Enter the email id of the receiver: ")
subject = input("Enter the subject: ")
message = input("Enter the message: ")

body = f"Subject: {subject}\n\n{message}"

connection = smtplib.SMTP(server, port)
connection.starttls()

try:
    connection.login(sender, password)
    connection.sendmail(sender, receiver, body)
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print(f"Failed to login. Error: {e}")
except smtplib.SMTPException as e:
    print(f"Failed to send email. Error: {e}")
finally:
    connection.quit()  # Use quit() instead of close() to properly terminate the session
