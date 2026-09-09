from dotenv import load_dotenv
import os
from sqlalchemy import text
from backend.utils.database import engine

load_dotenv()

print("DATABASE_URL loaded:", bool(os.getenv("DATABASE_URL")))
print("Engine URL:", engine.url.render_as_string(hide_password=True))

with engine.begin() as connection:
    print("Database:", connection.execute(text("SELECT current_database()")).scalar())
    print("Inserting equipment...")

    connection.execute(
        text("""
            INSERT INTO equipment
            (equipment_code, equipment_name, equipment_type, model, manufacturer)
            VALUES
            ('MOTOR-IM450', 'Industrial Induction Motor', 'Electric Motor', 'IM-450', 'MAINT-AI Demo'),
            ('PUMP-CP200', 'Centrifugal Process Pump', 'Centrifugal Pump', 'CP-200', 'MAINT-AI Demo'),
            ('COMP-AC300', 'Industrial Air Compressor', 'Air Compressor', 'AC-300', 'MAINT-AI Demo')
        """)
    )

print("3 equipment records inserted successfully!")