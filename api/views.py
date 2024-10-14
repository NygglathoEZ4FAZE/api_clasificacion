from django.http import JsonResponse
from django.views import View
from .utils import cargar_modelos
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class ClasificarConsulta(View):
    modelo_cargado, pipeline_cargado, encoder_cargado = cargar_modelos()

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            consulta = data.get("consulta")

            if not consulta:
                return JsonResponse({"error": "Consulta no proporcionada."}, status=400)

            prediccion_codificada = self.modelo_cargado.predict([consulta])
            prediccion = self.encoder_cargado.inverse_transform(prediccion_codificada)
            return JsonResponse({"prediccion": prediccion[0]}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
