import random
from models import Lead, db

# Função para gerar leads fictícios
def generate_leads():
    email = ['emailaleotorio@gmail.com', 'jjashdjajsadhb@gmail.com', 'hhahahaha@gmail.com']
    names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
    interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']
    telephone = ['(51)99999-9999', '(51)88888-8888','(51)77777-7777','(51)66666-6666']

    for _ in range(100):
        name = random.choice(names)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        temperature = random.uniform(10, 40)
        interest = random.choice(interests)
        email = random.choice(email)
        telephone = random.choice(telephone)

        lead = Lead(name, latitude, longitude, temperature, interest, email, telephone)
        db.session.add(lead)
        db.session.commit()

