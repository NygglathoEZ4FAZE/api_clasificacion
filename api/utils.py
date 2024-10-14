import os
import joblib

def cargar_modelos():
    ruta_modelos = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'models')
    
    try:
        # Asegúrate de que los nombres de los archivos sean correctos
        modelo_cargado = joblib.load(os.path.join(ruta_modelos, 'modelo_svm_entrenado_pickle.pkl'))
        pipeline_cargado = joblib.load(os.path.join(ruta_modelos, 'pipeline_entrenado.pkl'))
        encoder_cargado = joblib.load(os.path.join(ruta_modelos, 'label_encoder.pkl'))
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise ValueError("Error: No se pudieron cargar todos los modelos necesarios.")
    
    return modelo_cargado, pipeline_cargado, encoder_cargado
