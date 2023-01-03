from celery import shared_task
from celery import Celery
#from celery.schedules import crontab
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.utils import timezone
from django.db.models import Q
from django.apps import apps
from django.conf import settings

app = Celery()

@shared_task(name='notification_status')
def notification_status():
	print("iniciado")
	date_now = now = timezone.now()
	Iniciativa = apps.get_model('ppoa','Iniciativa')
	res_incumplido = Iniciativa.objects.filter(Q(porcentaje__isnull=True)|Q(porcentaje__lte=85),f_fin__year=date_now.year, f_fin__lte=date_now)
	for i in res_incumplido:
		if(i.unidadgestion.unidad.email_unidad):
			send_mail_internal(i.unidadgestion.unidad.email_unidad, i)

def send_mail_internal(email, iniciativa):
	return send_mail(
		'Mensaje de alerta de inicitaiva incumplida Sistema del POA de la USFA',
		f'Debe revisar las tareas que se deben cumplir { iniciativa.iniciativa } su fecha limite es { iniciativa.f_fin }.',
		settings.EMAIL_HOST_USER,
		[email],
		fail_silently=False
	)
