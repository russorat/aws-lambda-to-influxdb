import json, os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.domain.write_precision import WritePrecision

def lambda_handler(event, context):
    # make sure the bucket you set here is already created in your InfluxDB instance
    bucket = "my-bucket"
    # This specifies the precision of your timestamp. For example, standard unix
    # timestamps have a precision of second (WritePrecision.S)
    # NanoSecond is the default for InfluxDB
    timestamp_precision = WritePrecision.NS

    # You can use this to build a data point from your event.
    # For more information about measurements, tags, and fields, check out
    # https://docs.influxdata.com/influxdb/cloud/reference/key-concepts/data-elements/
    point = {
        "measurement" : "",
        "tags" : {},
        "fields" : {},
        "timestamp" : 0
    }

    record = Point.from_dict(point, write_precision=timestamp_precision)
    records_to_send = [record]

    write_api = _get_write_api()
    results = write_api.write(bucket=bucket, record=records_to_send)
    
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }

def _get_write_api():
    url = os.environ['INFLUXDB_HOST']
    token = os.environ['INFLUXDB_TOKEN']
    org = os.environ['INFLUXDB_ORG']
    
    return InfluxDBClient(url=url, token=token, org=org).write_api(write_options=SYNCHRONOUS)