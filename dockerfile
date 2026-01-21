FROM python:3.12-alpine
LABEL authors="PixelWelt"

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock /app/
RUN uv pip sync uv.lock --no-cache
COPY ./app /app

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
