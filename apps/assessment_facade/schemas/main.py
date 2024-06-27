from pydantic import BaseModel


class Question(BaseModel):
    question_type: str


class Answer(BaseModel):
    answer_type: str
    string: str


class AssessmentRequest(BaseModel):
    question: Question
    correct_answer: Answer
    given_answer: Answer


class AssessmentResponse(BaseModel):
    correctness_percentage: float
    comment: str
