class AuxiliarTool3:
    @staticmethod
    def is_valid_email(email):
        """Valida si el formato del correo electrónico es válido."""
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))
