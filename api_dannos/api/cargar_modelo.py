import tensorflow as tf
from tensorflow.keras import applications
import numpy as np
import os

class DamagePredictor:
    def __init__(self, model_path):
        """Carga el modelo y los diccionarios de etiquetas"""
        self.model = tf.keras.models.load_model(model_path)
        self.label_to_cls_piezas = {
            1: "Antiniebla delantero derecho",
            2: "Antiniebla delantero izquierdo",
            3: "Capó",
            4: "Cerradura capo",
            5: "Cerradura maletero",
            6: "Cerradura puerta",
            7: "Espejo lateral derecho",
            8: "Espejo lateral izquierdo",
            9: "Faros derecho",
            10: "Faros izquierdo",
            11: "Guardabarros delantero derecho",
            12: "Guardabarros delantero izquierdo",
            13: "Guardabarros trasero derecho",
            14: "Guardabarros trasero izquierdo",
            15: "Luz indicadora delantera derecha",
            16: "Luz indicadora delantera izquierda",
            17: "Luz indicadora trasera derecha",
            18: "Luz indicadora trasera izquierda",
            19: "Luz trasera derecho",
            20: "Luz trasera izquierdo",
            21: "Maletero",
            22: "Manija derecha",
            23: "Manija izquierda",
            24: "Marco de la ventana",
            25: "Marco de las puertas",
            26: "Moldura capó",
            27: "Moldura puerta delantera derecha",
            28: "Moldura puerta delantera izquierda",
            29: "Moldura puerta trasera derecha",
            30: "Moldura puerta trasera izquierda",
            31: "Parabrisas delantero",
            32: "Parabrisas trasero",
            33: "Parachoques delantero",
            34: "Parachoques trasero",
            35: "Puerta delantera derecha",
            36: "Puerta delantera izquierda",
            37: "Puerta trasera derecha",
            38: "Puerta trasera izquierda",
            39: "Rejilla, parrilla",
            40: "Rueda",
            41: "Tapa de combustible",
            42: "Tapa de rueda",
            43: "Techo",
            44: "Techo corredizo",
            45: "Ventana delantera derecha",
            46: "Ventana delantera izquierda",
            47: "Ventana trasera derecha",
            48: "Ventana trasera izquierda",
            49: "Ventanilla delantera derecha",
            50: "Ventanilla delantera izquierda",
            51: "Ventanilla trasera derecha",
            52: "Ventanilla trasera izquierda"
        }
        self.label_to_cls_danos = {
            1: "Abolladura",
            2: "Deformación",
            3: "Desprendimiento",
            4: "Fractura",
            5: "Rayón",
            6: "Rotura"
        }
        self.label_to_cls_sugerencias = {
            1: "Reparar",
            2: "Reemplazar"
        }

    def preprocess_image(self, image_path, img_size=(224, 224)):
        """Preprocesa la imagen para el modelo"""
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=img_size)
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = applications.efficientnet.preprocess_input(img_array)
        return np.expand_dims(img_array, axis=0)

    def predict(self, image_path):
        """Realiza la predicción sobre una imagen"""
        # Preprocesar imagen
        img_array = self.preprocess_image(image_path)
        
        # Hacer predicción
        predictions = self.model.predict(img_array)
        
        # Procesar resultados
        def get_top_predictions(classes, probs, label_dict, top_n=3):
            top_items = sorted(zip(classes, probs[0]), key=lambda x: x[1], reverse=True)[:top_n]
            return [{"label": label_dict.get(int(cls), f"Clase_{int(cls)}"), "probability": float(prob)} for cls, prob in top_items]
        
        return {
            "partes": get_top_predictions(range(len(self.label_to_cls_piezas)), predictions[0], self.label_to_cls_piezas),
            "dannos": get_top_predictions(range(len(self.label_to_cls_danos)), predictions[1], self.label_to_cls_danos),
            "sugerencias": get_top_predictions(range(len(self.label_to_cls_sugerencias)), predictions[2], self.label_to_cls_sugerencias)
        }