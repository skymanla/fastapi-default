from pydantic import BaseModel, Field
from typing import Union, Any, List


class RestResponse(BaseModel):
    code: str = Field(title="code value", default="0000")
    message: Union[str, None] = Field(title="메세지", default=None)
    data: Union[Any, None] = Field(title="data", default=None)


