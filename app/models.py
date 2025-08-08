from app import db # Importe l'instance db depuis le __init__.py

class Site(db.Model):
    __tablename__ = 'site'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, index=True)
    address = db.Column(db.String(250), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    
    # Relation : un site peut avoir plusieurs scénarios de risque.
    # cascade="all, delete-orphan" signifie que si un site est supprimé,
    # tous ses scénarios de risque le sont aussi.
    risk_scenarios = db.relationship('RiskScenario', backref='site', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Site {self.name}>'

class RiskScenario(db.Model):
    __tablename__ = 'risk_scenario'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    # Type de danger pour la symbologie (ex: 'thermique', 'toxique', 'surpression')
    risk_type = db.Column(db.String(50), nullable=False) 
    # Le rayon en mètres de la zone d'effet
    radius_meters = db.Column(db.Integer, nullable=False)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=False)

    def __repr__(self):
        return f'<RiskScenario {self.description}>'