rm upload-to-aws.zip
docker rm /lambdalayer
docker build -t lambdalayer:latest .
docker create --name lambdalayer lambdalayer:latest
docker cp lambdalayer:/install/python.zip ./upload-to-aws.zip
zip -g upload-to-aws.zip ../lambda_function.py
