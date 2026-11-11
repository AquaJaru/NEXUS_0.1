from fastapi import FastAPI

app = FastAPI(
    title="NEXUS API",
    description="AI-powered Data Intelligence Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to NEXUS",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }