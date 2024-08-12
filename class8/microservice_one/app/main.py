# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from app import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select, Sequence
from fastapi import FastAPI, Depends
from typing import AsyncGenerator
from app.middleware import middleware
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import json

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)

class Order(SQLModel):
    id: Optional[int] = Field(default=None)
    username: str 
    productId: int
    productName: str
    productPrice: int

@asynccontextmanager
async def lifespan(app: FastAPI)-> AsyncGenerator[None, None]:
    print("Call kafka consumer..")
    # initial stage class call here
    yield


app = FastAPI(lifespan=lifespan, title="Product service with kafka", 
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])
middleware.setup_cors(app)


@app.get("/")
def read_product():
    return {"Hello": "PanaCloud"}

#Producer
# it sends the order to kafka bootsrape server
@app.post("/create-order")
async def buy_product(order: Order):
    producer=AIOKafkaProducer(bootstrap_servers=settings.BOOTSTRAP_SERVER)
    await producer.start()
    orderJSON= json.dumps(order.__dict__).encode("utf-8")
    print("orderJSON")
    print(orderJSON)
    
    try:
        await producer.send_and_wait(settings.KAFKA_TOPIC, orderJSON)
    finally:
        await producer.stop()
    return orderJSON



#Consumer
# it gets the order to kafka bootsrape server
@app.get("/read-orders")
async def read_orders():
    consumer=AIOKafkaConsumer("order", 
                              bootstrap_servers=settings.BOOTSTRAP_SERVER,
                              group_id=settings.KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT)
    await consumer.start()
    
    
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp) 
    finally:
        await consumer.stop()
    return {"data": consumer}




