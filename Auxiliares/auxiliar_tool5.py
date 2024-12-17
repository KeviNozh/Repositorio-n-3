from datetime import datetime

class AuxiliarTool5:
    @staticmethod
    def get_current_date():
        """Obtiene la fecha actual en formato YYYY-MM-DD."""
        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def format_date(date_str, input_format, output_format):
        """Formatea una fecha de un formato a otro."""
        try:
            date_obj = datetime.strptime(date_str, input_format)
            return date_obj.strftime(output_format)
        except ValueError as e:
            print(f"Error formateando fecha: {e}")
            return None
