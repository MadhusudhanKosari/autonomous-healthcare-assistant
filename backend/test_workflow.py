from app.agents.workflow import app_workflow

response = app_workflow.invoke({

    "query": "What does the report say about glucose?"

})

print(response["final_response"])