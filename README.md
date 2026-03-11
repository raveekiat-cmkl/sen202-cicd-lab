# Mini CI/CD Lab

This project demonstrates a simple CI/CD pipeline using GitHub Actions.

## Setup

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest

Run the application:

uvicorn app.main:app --reload

Open:

http://localhost:8000

## CI/CD

Every push to GitHub will automatically:

1. Checkout the repository
2. Install dependencies
3. Run tests

If tests fail, the CI pipeline fails.

## Lab Exercise

1. Clone the repository
2. Run tests locally
3. Push to GitHub
4. Observe CI pipeline

### Break the pipeline

Change the add function:

return {"result": a - b}

Push again.

CI should fail.

Fix it and push again.