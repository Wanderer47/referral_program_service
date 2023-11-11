from datetime import datetime

from sqlalchemy import  MetaData, Table, Column, Integer, String, TIMESTAMP

metadata_obj = MetaData()

contact = Table(
        "contact",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("full_name", String(60), nullable=False),
        Column("phone_num", String(12), nullable=False),
        Column("registred_at", TIMESTAMP, default=datetime.utcnow),
        )
