### Example Lamdba Function to Write Data to InfluxDB

To build a zip file to upload to AWS, `cd` into the `docker` directory and run the `build-dependencies.sh` script. Upload the resulting file to AWS Lambda.

### Environment Variables

You will need to define the following environment variables in your Lambda project:

- `INFLUXDB_HOST` - the full base url of you InfluxDB instance (e.g. https://us-west-2-1.aws.cloud2.influxdata.com)
- `INFLUXDB_TOKEN` - A token with permissions to write to the specific bucket
- `INFLUXDB_ORG` - the name of the InfluxDB Org you would like to write to (e.g. my organization)
