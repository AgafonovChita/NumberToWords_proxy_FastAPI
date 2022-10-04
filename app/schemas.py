from pydantic import BaseModel


class Number(BaseModel):
    ubi_num: int
