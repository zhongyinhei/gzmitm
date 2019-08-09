/usr/local/bin/mitmdump --set block_global=false -s /code/start_script.py

BROKER_URL = 'amqp://cic_admin:JYcxys@3030@{}:{}/yct_gz'.format(RABBITMQ_HOST,RABBITMQ_PORT)

yct_gz/to_create

docker run --name gz_p_w -p 7777:8080 daocloud.io/zhongyinhei/mitm:master-5dd96d6