# Local language model with Ollama

Docker Compose starts Ollama, FastAPI and a Streamlit client. The backend forwards prompts to the local model. Initial startup downloads llama3.2:1b. Open the client at http://localhost:8502.

## Run locally

```sh
docker compose up --build
```
