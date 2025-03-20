# communications/management/commands/send_test_email.py
from django.core.management.base import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Sends a test email'

    def handle(self, *args, **options):
        try:
            send_mail(
                subject='Test Email',
                message='This is a test email from Django.',
                from_email='tosh75910@gmail.com',
                recipient_list=['kiptootitus75@gmail.com'],
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS('Email sent successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error sending email: {e}'))