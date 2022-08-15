import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .resolver import Query

from .model import models
from .session.sessions import engine

models.Base.metadata.create_all(bind=engine)


schema=strawberry.Schema(query=Query)

graphql_app=GraphQLRouter(schema)
app=FastAPI()
app.include_router(graphql_app, prefix="/graphql")
