import smtplib

# Get email details
email = input("Sender Email: ")
receiver_email = input("Receiver Email: ")
subject = input("Subject: ")
message = input("Message: ")

# Create the email content
text = f"Subject: {subject}\n\n{message}"

# Connect to the Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  # Start TLS encryption

try:
    # Log in to the email account
    server.login(email, "rygh jjfz xxis rfwv")  # Use your actual app password here
    # Send the email
    server.sendmail(email, receiver_email, text)
    print("The email has been sent to " + receiver_email)
except smtplib.SMTPException as e:
    print(f"Failed to send email: {e}")
finally:
    # Close the connection
    server.quit()
