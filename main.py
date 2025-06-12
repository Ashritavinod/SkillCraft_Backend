from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.concurrency import run_in_threadpool

from agent import SkillAgent, client
from prompts import system_prompt

app = FastAPI()

# Allow all origins during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = SkillAgent(client, system_prompt)

class SkillInput(BaseModel):
    current_skills: list[str]
    target_role: str

@app.get("/")
def root():
    return {"message": "API is live"}

@app.post("/generate")
async def generate_skill_tree(data: SkillInput):
    prompt = f"""
    Current Skills: {', '.join(data.current_skills)}
    Target Role: {data.target_role}
    """
    print("🔍 Generated Prompt for Agent:\n", prompt)

    try:
        result = await run_in_threadpool(agent, prompt)
        print("✅ Agent Response:\n", result)

        if not result:
            raise HTTPException(status_code=204, detail="Agent returned no data")

        return {"result": result}

    except Exception as e:
        print("❌ Error occurred:", e)
        raise HTTPException(status_code=500, detail=f"Something went wrong: {str(e)}")
