## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip install -r requirements.txt
python -m swagger_server
```

and, for instance, open your browser to here:

```
http://localhost:8080/api/v1/recambios
```


## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```