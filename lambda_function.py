import json, os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.domain.write_precision import WritePrecision

def lambda_handler(event, context):
    bucket = "my-bucket"
    point = {
        "measurement" : "",
        "tags" : [],
        "fields" : [],
        "timestamp" : 0
    }

    write_api = _get_write_api()
    results = write_api.write(bucket=bucket, record=[Point.from_dict(point, write_precision=WritePrecision.NS)])
    
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }

def _get_write_api():
    url = os.environ['INFLUXDB_HOST']
    token = os.environ['INFLUXDB_TOKEN']
    org = os.environ['INFLUXDB_ORG']
    
    return InfluxDBClient(url=url, token=token, org=org).write_api(write_options=SYNCHRONOUS)