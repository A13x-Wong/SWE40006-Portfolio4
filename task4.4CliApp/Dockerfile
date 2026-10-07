FROM python:3.14-slim

WORKDIR /app

COPY expense_manager.py .

ENV EXPENSE_DB=/data/expenses.db

VOLUME ["/data"]

ENTRYPOINT ["python", "expense_manager.py"]