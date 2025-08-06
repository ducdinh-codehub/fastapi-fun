from fastapi import APIRouter, Depends, status

from .models import SendingEmailRequest
from .services import sendEmail as sv_send_mail

routers = APIRouter()

@routers.post("/send-email/")
async def send_email(data: SendingEmailRequest):
    reponse = sv_send_mail(data)
    return reponse