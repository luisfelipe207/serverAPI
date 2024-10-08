from models import Lead

class LeadService:
    def __init__(self, db):
        self.db = db

    def get_paginated_leads(self, page, per_page):
        return Lead.query.paginate(page=page, per_page=per_page, error_out=False)


    def create_lead(self, name, latitude, longitude, temperature, interest, email, telephone):
        lead = Lead(
            name=name,
            latitude=latitude,
            longitude=longitude,
            temperature=temperature,
            interest=interest,
            email=email,
            telephone=telephone
        )
        self.db.session.add(lead)
        self.db.session.commit()

    def get_all_leads(self):
        return Lead.query.all()

    def get_lead_by_id(self, lead_id):
        return Lead.query.get_or_404(lead_id)

    def update_lead(self, lead_id, name, latitude, longitude, temperature, interest, email, telephone):
        lead = self.get_lead_by_id(lead_id)
        lead.name = name
        lead.latitude = latitude
        lead.longitude = longitude
        lead.temperature = temperature
        lead.interest = interest
        lead.email = email
        lead.telephone = telephone
        self.db.session.commit()

    def delete_lead(self, lead_id):
        lead = self.get_lead_by_id(lead_id)
        self.db.session.delete(lead)
        self.db.session.commit()
