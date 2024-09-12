import random
import re
from models import Lead, db

# Função para validar e-mail usando regex
def is_valid_email(email):
    # Regex simples para verificar se o e-mail contém um formato básico "texto@texto.texto"
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False

# Função para validar telefone usando regex
def is_valid_telephone(telephone):
    # Regex simples para verificar os formatos (XX) XXXX-XXXX ou (XX) XXXXX-XXXX
    if re.match(r"^\(\d{2}\) \d{4,5}-\d{4}$", telephone):
        return True
    else:
        return False

# Função para verificar se o e-mail é único
def is_unique_email(email):
    return Lead.query.filter_by(email=email).first() is None

# Função para gerar leads fictícios com validações
def generate_leads():
    emails = ['emailaleotorio@gmail.com', 'jjashdjajsadhb@gmail.com', 'hhahahaha@gmail.com']
    names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
    interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']
    telephones = ['(51)99999-9999', '(51)88888-8888', '(51)77777-7777', '(51)66666-6666']

    for _ in range(100):
        name = random.choice(names)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        temperature = random.uniform(1, 5)
        interest = random.choice(interests)
        email = random.choice(emails)
        telephone = random.choice(telephones)

        # Validações
        
        lead = Lead(name, latitude, longitude, temperature, interest, email, telephone)
        db.session.add(lead)
        db.session.commit()
       

