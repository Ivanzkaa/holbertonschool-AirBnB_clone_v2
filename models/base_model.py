#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models"""

    if models.storage_type == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(
                DateTime, default=datetime.utcnow(), nullable=False)
        updated_at = Column(
                DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            if (not kwargs.get("id", 0)):
                self.id = str(uuid.uuid4())

            if (kwargs.get("created_at", 0)):
                kwargs["created_at"] = datetime.fromisoformat(
                    kwargs["created_at"])
            else:
                self.created_at = datetime.now()

            if (kwargs.get("updated_at", 0)):
                kwargs["updated_at"] = datetime.fromisoformat(
                    kwargs["updated_at"])
            else:
                self.updated_at = self.created_at

            if (kwargs.get("__class__", 0)):
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        try:
            del my_dict["_sa_instance_state"]
        except:
            pass
        return my_dict

    def delete(self):
        """delete the current instance from storage"""
        models.storage.delete(self)
