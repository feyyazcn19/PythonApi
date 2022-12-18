import uvicorn
from main import app

uvicorn.run(
    app,
    host="python-api-rmik.onrender.com",
    port=8080,
    # ssl_keyfile="./localhost+4-key.pem",
    # ssl_certfile="./localhost+4.pem"
)
