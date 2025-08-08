from flask import render_template, request, redirect, url_for, flash, Blueprint, jsonify, Response
from app import db
from app.models import Site, RiskScenario
from app.services import geocode_address, generate_report_pdf
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    sites = Site.query.order_by(Site.name).all()
    return render_template('index.html', sites=sites)

@main.route('/site/new', methods=['GET', 'POST'])
def new_site():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        
        # Valider que les champs de base sont remplis
        if not name or not address:
            flash('Le nom du site et l\'adresse sont obligatoires.', 'danger')
            return redirect(url_for('main.new_site'))
        
        latitude, longitude = geocode_address(address)
        if latitude is None:
            flash(f"L'adresse '{address}' n'a pas pu être géocodée. Veuillez vérifier.", 'danger')
            return redirect(url_for('main.new_site'))
            
        new_site = Site(name=name, address=address, latitude=latitude, longitude=longitude)
        db.session.add(new_site)

        # Ajouter le scénario de risque initial
        risk_desc = request.form.get('risk_description')
        risk_type = request.form.get('risk_type')
        risk_radius = request.form.get('risk_radius')

        if risk_desc and risk_type and risk_radius:
            new_scenario = RiskScenario(
                description=risk_desc,
                risk_type=risk_type,
                radius_meters=int(risk_radius),
                site=new_site
            )
            db.session.add(new_scenario)
        
        db.session.commit()
        flash('Nouveau site créé avec succès !', 'success')
        return redirect(url_for('main.view_site', site_id=new_site.id))
        
    return render_template('site_form.html')

@main.route('/site/<int:site_id>')
def view_site(site_id):
    site = Site.query.get_or_404(site_id)
    
    # Préparer les données pour le JS de la carte
    scenarios_data = [{
        'description': s.description,
        'risk_type': s.risk_type,
        'radius_meters': s.radius_meters
    } for s in site.risk_scenarios]
    
    site_json_data = {
        'name': site.name,
        'address': site.address,
        'latitude': site.latitude,
        'longitude': site.longitude,
        'risk_scenarios': scenarios_data
    }

    return render_template('site_view.html', site=site, site_json=json.dumps(site_json_data))

@main.route('/site/<int:site_id>/delete', methods=['POST'])
def delete_site(site_id):
    site_to_delete = Site.query.get_or_404(site_id)
    db.session.delete(site_to_delete)
    db.session.commit()
    flash('Le site a été supprimé.', 'success')
    return redirect(url_for('main.index'))
    
@main.route('/site/<int:site_id>/report')
def download_report(site_id):
    site = Site.query.get_or_404(site_id)
    pdf_data = generate_report_pdf(site)
    
    return Response(pdf_data,
                    mimetype='application/pdf',
                    headers={'Content-Disposition': f'attachment;filename=rapport_risques_{site.id}.pdf'})