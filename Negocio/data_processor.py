class DataProcessor:
    @staticmethod
    def clean_data(data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}
        return data

    @staticmethod
    def validate_data(data, required_fields):
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Faltan campos requeridos: {', '.join(missing_fields)}")
        return True
