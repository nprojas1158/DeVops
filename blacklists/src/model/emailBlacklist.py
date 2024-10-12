from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from marshmallow import Schema, fields
import uuid

Base = declarative_base()

class EmailBlacklist(Base):
    __tablename__ = 'email_blacklist'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable = False)
    appId = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable = False)
    reason = Column(String(255), nullable = True)
    dirIP = Column(String, nullable = False)
    dateHour = Column(DateTime, nullable = False)

    def __init__(
            self, id, email, appId, reason, dirIp, dateHour
    ):
        self.id = uuid.uuid4()
        self.email = email
        self.appId = appId
        self.reason = reason
        self.dirIP = dirIp
        self.dateHour = dateHour
    
    class EmailBlacklistSchema(Schema):
        id = fields.UUID()
        email = fields.Str()
        appId = fields.UUID()
        reason = fields.Str()
        dirIp = fields.Str()
        dateHour = fields.DateTime()