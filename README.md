
## Installation
Install the requirements with pip3:
```
pip3 install -r requirements.txr
```

## Example

1. Start the flask app from the terminal:
```
python3 -m flask run
```
2. Add tasks to the queue by making requests to localhost, e.g.
```
curl http://localhost:5000/lights_on
curl http://localhost:5000/lights_off
```
3. A worker will take care of the tasks one by one.