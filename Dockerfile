FROM ghcr.io/astral-sh/uv:0.12.3-python3.14-trixie-slim
WORKDIR /app
ENV UV_LINK_MODE=copy
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked
COPY . .
ENTRYPOINT ["uv", "run", "--locked"]
