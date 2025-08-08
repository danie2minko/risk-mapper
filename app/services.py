from geopy.geocoders import Nominatim
from fpdf import FPDF

def geocode_address(address):
    """Convertit une adresse en coordonnées (latitude, longitude)."""
    try:
        # user_agent est requis par les conditions d'utilisation de Nominatim
        geolocator = Nominatim(user_agent="risk_mapper_prototype")
        location = geolocator.geocode(address, timeout=10)
        if location:
            return (location.latitude, location.longitude)
    except Exception as e:
        print(f"Erreur de géocodage: {e}")
    return (None, None)

def generate_report_pdf(site):
    """Génère un rapport PDF pour un site donné."""
    pdf = FPDF()
    pdf.add_page()
    
    # Titre
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f'Fiche de Synthèse de Risques', 0, 1, 'C')
    pdf.ln(10)

    # Informations du site
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'Site: {site.name}', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Adresse: {site.address}', 0, 1)
    pdf.cell(0, 10, f'Coordonnées: Lat {site.latitude:.4f}, Lon {site.longitude:.4f}', 0, 1)
    pdf.ln(10)

    # Tableau des scénarios de risques
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Scénarios de Risques Identifiés', 0, 1)
    
    # Entêtes du tableau
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(100, 10, 'Description du Phénomène Dangereux', 1)
    pdf.cell(40, 10, 'Type de Risque', 1)
    pdf.cell(40, 10, 'Zone d\'Effet (m)', 1)
    pdf.ln()

    # Contenu du tableau
    pdf.set_font('Arial', '', 10)
    for scenario in site.risk_scenarios:
        pdf.cell(100, 10, scenario.description, 1)
        pdf.cell(40, 10, scenario.risk_type.capitalize(), 1)
        pdf.cell(40, 10, str(scenario.radius_meters), 1)
        pdf.ln()
        
    return pdf.output(dest='S').encode('latin-1')