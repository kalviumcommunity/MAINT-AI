from sqlalchemy import text
from backend.utils.database import engine

documents = [
    ("industrial_motor_manual.pdf", "Maintenance Manual", "data/industrial_motor_manual.pdf", 1),
    ("centrifugal_pump_guide.pdf", "Maintenance Guide", "data/centrifugal_pump_guide.pdf", 2),
    ("air_compressor_guide.pdf", "Maintenance Guide", "data/air_compressor_guide.pdf", 3),
]

with engine.begin() as connection:
    for name, doc_type, path, equipment_id in documents:
        connection.execute(
            text("""
                INSERT INTO documents
                (document_name, document_type, file_path, equipment_id)
                VALUES (:name, :doc_type, :path, :equipment_id)
            """),
            {
                "name": name,
                "doc_type": doc_type,
                "path": path,
                "equipment_id": equipment_id
            }
        )

print("3 document records inserted successfully!")