from pydantic import BaseModel, Field

class ClassificationOutput(BaseModel):
    label: str = Field(..., description="Category label")
    confidence: float = Field(..., ge=0, le=1)
