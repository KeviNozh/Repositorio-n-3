class AuxiliarTool6:
    @staticmethod
    def dict_to_json(data_dict):
        """Convierte un diccionario a formato JSON."""
        import json
        return json.dumps(data_dict, indent=4)

    @staticmethod
    def json_to_dict(json_str):
        """Convierte una cadena JSON a un diccionario."""
        import json
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            return None
