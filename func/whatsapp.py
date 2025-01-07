import pywhatkit as kit
from datetime import datetime

def sendWhatsAppMessage(contato, message):
    now = datetime.now()
    time_hour = now.hour
    time_min = now.minute + 1
    
    if "best friend" in contato:
        kit.sendwhatmsg("+number", message, time_hour, time_min)
        
    if "baby" in contato:
        kit.sendwhatmsg("+number", message, time_hour, time_min)
        
        
    return "Mensagem enviada"