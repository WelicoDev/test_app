from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser


@receiver(post_save ,sender=CustomUser)
def send_welcome_email(sender , instance , created , **kwargs):
    if created:
        send_mail(
            "Welcome to Test App",
            f"Hi , {instance.email}. Welcome to Test App !",
            'xurramovotabek568@gmail.com',
            [instance.email])
