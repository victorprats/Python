# https://stackoverflow.com/questions/6332577/send-outlook-email-via-python
import win32com.client as win32


outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'email@domain.com'
mail.Subject = 'Assumpte del missatge'
mail.Body = 'Aixó es una proba de correu'
# mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

# To attach a file to the email (optional):
attachment  = "\\Python_projects\\test.txt"
mail.Attachments.Add(attachment)

mail.Send()
