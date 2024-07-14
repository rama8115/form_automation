from django.core.mail import EmailMessage
from django.shortcuts import render
import os

def send_submission_email(request):
    if request.method == 'POST':
        # Load the screenshot file
        screenshot_path = os.path.join(os.getcwd(), 'confirmation_screenshot.png')
        github_repo_link = 'https://github.com/rama8115/form_automation.git'
        document_path = os.path.join(os.getcwd(), 'documentation.docx')
    
        # Create email
        email_body = f"""
        
        GitHub Repository : {github_repo_link}
        
        """
        email = EmailMessage(
            subject='Python (Selenium) Assignment - Ramanand Kumar Gupt',
            body=email_body,
            from_email='babu.doctor.raman@gmail.com',
            to=['tech@themedius.a'],
            cc=['hr@themedius.ai'],
        )
        email.attach_file(document_path)
        email.attach_file(screenshot_path)

        # Send the email
        email.send()

        return render(request, 'submission/success.html')

    return render(request, 'submission/form.html')

