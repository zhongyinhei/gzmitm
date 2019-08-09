# -*- coding:utf-8 -*-
# from handle_data.tasks import
# print('hello')
from handle_data import celery_app


def handle_data(data_str):
    # res = chain(to_product.s(data_str), to_analysis.s(), to_consume.s())()

    # 插入一条pickle后的数据，返回记录的id res1
    to_create.apply_async(args=[data_str], retry=True, queue='to_create', immutable=True)
    # res = to_create(data_str)
    # print(res)


@celery_app.task(name='to_create')
def to_create(data):
    '''解析出所有的退回数据,将pickle的数据做解析'''
    pass
    # if data:
    #     order_number = str(random.random())
    #     REDIS_GZ.set(order_number, data, ex=3600)
    #     to_analysis.apply_async(args=[order_number], retry=True, queue='to_analysis', immutable=True)
