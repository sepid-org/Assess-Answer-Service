from fastapi import FastAPI
from apps.assess_Github_repository.api.api_v1 import api_router as assess_Github_repository_api_router
from apps.assessment_facade.api.api_v1 import api_router as assessment_facade_api_router

app = FastAPI()

app.include_router(assess_Github_repository_api_router, prefix="/assess-github-repository/v1")
app.include_router(assessment_facade_api_router, prefix="/facade/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
