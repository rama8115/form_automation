from django.core.mail import EmailMessage
from django.shortcuts import render
import os

def send_submission_email(request):
    if request.method == 'POST':
        # Load the screenshot file
        screenshot_path = os.path.join(os.getcwd(), 'confirmation_screenshot.png')

        
        email = EmailMessage(
            subject='Python (Selenium) Assignment - Ramanand Kumar Gupt',
            body='Please find attached the screenshot of the confirmation page.',
            from_email='babu.doctor.raman@gmail.com',
            to=['gupta.doctor.raman@gmail.com'],
            cc=['gupta.doctor.raman@gmail.com'],
        )
        email.attach()
        email.attach_file(screenshot_path)

        # Send the email
        email.send()

        return render(request, 'submission/success.html')

    return render(request, 'submission/form.html')

