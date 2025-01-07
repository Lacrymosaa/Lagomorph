import datetime

def greetings():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        time = "Bom dia mestre."
    elif hour >12 and hour<=18:
        time = "Boa tarde, mestre."

    else:
        time = "Boa noite, mestre."

    return time + " Como posso te ajudar?"