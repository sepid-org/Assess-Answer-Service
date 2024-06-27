import json
from apps.assessment_facade.schemas.main import AssessmentRequest, AssessmentResponse
from fastapi import APIRouter

router = APIRouter()


@router.post("/", response_model=AssessmentResponse)
async def assess_facade(request: AssessmentRequest):
    question = request.question
    correct_answer = request.correct_answer
    given_answer = request.given_answer

    correctness_percentage = -1
    comment = 'not assessed'

    correct_answer_type = correct_answer.answer_type
    given_answer_type = given_answer.answer_type
    correct_answer_string = correct_answer.string
    given_answer_string = given_answer.string

    if correct_answer_type == 'SmallAnswer':
        if correct_answer_string == given_answer_string:
            correctness_percentage = 100
            comment = 'بنازم!'
        else:
            correctness_percentage = 0
            comment = 'ای بابا :('
    if correct_answer_type == 'MultiChoiceAnswer':
        given_choices = json.loads(given_answer_string)
        correct_choices = json.loads(correct_answer_string)
        if given_choices == correct_choices:
            correctness_percentage = 100
            comment = 'بنازم!'
        else:
            correctness_percentage = 0
            comment = 'ای بابا :('
    else:
        pass

    return {'correctness_percentage': correctness_percentage, 'comment': comment}
