from pydantic import BaseModel
from typing import Optional


class Question(BaseModel):
    question_type: str


class Answer(BaseModel):
    answer_type: str
    text: str


class AssessmentRequest(BaseModel):
    question: Question
    correct_answer: Answer
    given_answer: Answer


class AssessmentResponse(BaseModel):
    correctness_percentage: float
    comment: str
