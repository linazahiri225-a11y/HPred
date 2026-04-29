"""
Module de prédiction immobilière.
Charge le modèle entraîné et effectue des prédictions.
"""

import joblib
import numpy as np
import os


class RealEstatePredictor:
    """Classe pour charger le modèle et prédire les prix immobiliers."""

    # Ordre des caractéristiques attendu par le modèle
    FEATURE_NAMES = [
        "area", "bedrooms", "bathrooms", "stories",
        "mainroad", "guestroom", "basement",
        "hotwaterheating", "airconditioning", "parking",
        "prefarea", "furnishingstatus"
    ]

    def __init__(self, model_type="accurate", model_path=None):

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # 🎯 Choix automatique du modèle
        if model_path is None:
            if model_type == "fast":
                model_path = os.path.join(base_dir, "fast_model.pkl")
            else:
                model_path = os.path.join(base_dir, "gradient_boosting_model.pkl")

        if not os.path.exists(model_path):
            raise FileNotFoundError(
            f"Modèle introuvable : {model_path}\n"
            "Veuillez placer le fichier .pkl dans le dossier du projet."
        )

        self.model = joblib.load(model_path)
        if isinstance(self.model, dict):
    
            self.model = self.model.get('model', self.model) 
    
        self.model_path = model_path
        self.model_type = model_type

    def predict(self, area, bedrooms, bathrooms, stories,
                mainroad, guestroom, basement, hotwaterheating,
                airconditioning, parking, prefarea, furnishingstatus):
        """
        Prédit le prix d'un bien immobilier.
        
        Args:
            area: Surface en m²
            bedrooms: Nombre de chambres
            bathrooms: Nombre de salles de bain
            stories: Nombre d'étages
            mainroad: Accès route principale (0/1)
            guestroom: Chambre d'amis (0/1)
            basement: Sous-sol (0/1)
            hotwaterheating: Chauffage eau chaude (0/1)
            airconditioning: Climatisation (0/1)
            parking: Nombre de places de parking
            prefarea: Zone préférentielle (0/1)
            furnishingstatus: État d'ameublement (0=non meublé, 1=semi-meublé, 2=meublé)
            
        Returns:
            float: Prix estimé du bien
        """
        features = np.array([[
            area, bedrooms, bathrooms, stories,
            mainroad, guestroom, basement,
            hotwaterheating, airconditioning, parking,
            prefarea, furnishingstatus
        ]])

        prediction = self.model.predict(features)
        return float(prediction[0])

    def validate_inputs(self, area, bedrooms, bathrooms, stories, parking):
        """
        Valide les entrées utilisateur.
        
        Returns:
            tuple: (is_valid, error_message)
        """
        errors = []

        if area is None or area <= 0:
            errors.append("La surface doit être supérieure à 0 m².")
        if area and area > 100000:
            errors.append("La surface semble trop grande (max 100 000 m²).")

        if bedrooms is None or bedrooms < 0:
            errors.append("Le nombre de chambres doit être positif.")
        if bedrooms and bedrooms > 20:
            errors.append("Le nombre de chambres semble trop élevé.")

        if bathrooms is None or bathrooms < 0:
            errors.append("Le nombre de salles de bain doit être positif.")
        if bathrooms and bathrooms > 10:
            errors.append("Le nombre de salles de bain semble trop élevé.")

        if stories is None or stories < 1:
            errors.append("Le nombre d'étages doit être au minimum 1.")
        if stories and stories > 10:
            errors.append("Le nombre d'étages semble trop élevé.")

        if parking is None or parking < 0:
            errors.append("Le nombre de parkings doit être positif.")
        if parking and parking > 10:
            errors.append("Le nombre de parkings semble trop élevé.")

        if errors:
            return False, "\n".join(errors)
        return True, ""
