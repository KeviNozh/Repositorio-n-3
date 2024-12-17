import hashlib

class Hashing:
    @staticmethod
    def generate_hash(data):
        return hashlib.sha256(data.encode()).hexdigest()

    @staticmethod
    def verify_hash(data, expected_hash):
        return Hashing.generate_hash(data) == expected_hash
