from apps.assessment_facade.schemas.main import AssessmentRequest, AssessmentResponse
from fastapi import APIRouter

router = APIRouter()


@router.post("/", response_model=AssessmentResponse)
async def assess_facade(request: AssessmentRequest):
    question = request.question
    correct_answer = request.correct_answer
    given_answer = request.given_answer

    print(correct_answer.answer_type)

    correctness_percentage = 0
    comment = ''

    correct_answer_type = correct_answer.answer_type
    given_answer_type = given_answer.answer_type
    correct_answer_text = correct_answer.text
    given_answer_text = given_answer.text

    if correct_answer_type == 'SmallAnswer':
        if correct_answer_text == given_answer_text:
            correctness_percentage = 100
            comment = 'بنازم!'
        else:
            comment = 'ای بابا :('
    if correct_answer_type == 'MultiChoiceAnswer':
        if correct_answer_text == given_answer_text:
            correctness_percentage = 100
            comment = 'بنازم!'
        else:
            comment = 'ای بابا :('
    else:
        pass
    return {'correctness_percentage': correctness_percentage, 'comment': comment}
