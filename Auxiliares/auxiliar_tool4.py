class AuxiliarTool4:
    @staticmethod
    def calculate_percentage(part, whole):
        """Calcula el porcentaje."""
        if whole == 0:
            return 0
        return (part / whole) * 100
