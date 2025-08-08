document.addEventListener('DOMContentLoaded', (event) => {
    // Vérifie si l'élément 'map' et la variable 'siteData' existent
    // (le script est chargé sur toutes les pages, mais la carte n'est que sur la page de vue)
    const mapDiv = document.getElementById('map');
    if (mapDiv && typeof siteData !== 'undefined') {
        
        // 1. Initialiser la carte, centrée sur les coordonnées du site
        const map = L.map('map').setView([siteData.latitude, siteData.longitude], 13); // Zoom level 13

        // 2. Ajouter une couche de fond de carte (OpenStreetMap)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // 3. Ajouter un marqueur pour l'emplacement exact du site
        L.marker([siteData.latitude, siteData.longitude]).addTo(map)
            .bindPopup(`<b>${siteData.name}</b><br>${siteData.address}`)
            .openPopup();

        // 4. Boucler sur les scénarios de risque et dessiner les zones d'effets
        siteData.risk_scenarios.forEach(scenario => {
            let color = 'grey'; 
            if (scenario.risk_type === 'thermique') color = 'red';
            if (scenario.risk_type === 'toxique') color = 'green';
            if (scenario.risk_type === 'surpression') color = 'orange';
            
            // Dessiner un cercle sur la carte
            L.circle([siteData.latitude, siteData.longitude], {
                color: color,
                fillColor: color,
                fillOpacity: 0.3,
                radius: scenario.radius_meters // Le rayon est en mètres
            }).addTo(map).bindPopup(scenario.description);
        });
    }
});