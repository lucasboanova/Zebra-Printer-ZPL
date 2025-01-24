from pydantic import BaseModel

class ZplModel(BaseModel):
    turn: str
    typeTonner: str
    branch: str
    ramp: str