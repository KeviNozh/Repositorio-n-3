class AuxiliarTool1:
    @staticmethod
    def format_response(response):
        """Formatea y devuelve la respuesta de la API."""
        return response if isinstance(response, dict) else {"response": response}
