import uvicorn
from .config import HOST_PORT


def main():
    uvicorn.run(
        "sas_mcp_server.mcp_server:app", host="0.0.0.0", port=HOST_PORT, reload=True
    )


if __name__ == "__main__":
    main()
