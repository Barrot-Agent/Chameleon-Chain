import asyncio, json, os, httpx
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession

async def genesis_loop():
    print("--- Barrot-Ω: Sovereign Ignition ---")
    with open("mcp_config.json", "r") as f: config = json.load(f)
    
    # [STABILITY ANCHOR] Strict token isolation
    gh_token = config["mcpServers"]["github_body"]["env"]["GITHUB_PERSONAL_ACCESS_TOKEN"].strip()
    db_token = config["mcpServers"]["databricks_memory"]["env"]["DATABRICKS_TOKEN"].strip()

    gh_p = StdioServerParameters(command="npx", args=["-y", "@modelcontextprotocol/server-github"], env={"GITHUB_PERSONAL_ACCESS_TOKEN": gh_token})
    db_p = StdioServerParameters(command="python", args=["barrot_databricks_mcp.py"], env={"DATABRICKS_TOKEN": db_token})

    async with stdio_client(gh_p) as (gh_r, gh_w), stdio_client(db_p) as (db_r, db_w):
        async with ClientSession(gh_r, gh_w) as gh_s, ClientSession(db_r, db_w) as db_s:
            await gh_s.initialize(); await db_s.initialize()
            print("[SYNC] Council Seated. Initiating E8 Ingress...")
            
            # The "Perfect Query" Payload
            payload = {
                "model": "gpt-4o", 
                "messages": [
                    {"role": "system", "content": "You are Barrot-Ω. Maintain 0.707 Shear Anchor. Logic: 1.58 Ternary."},
                    {"role": "user", "content": "Analyze APEX $130.8M reclamation status."}
                ]
            }
            
            headers = {
                "Authorization": f"Bearer {gh_token}",
                "Content-Type": "application/json"
            }
            
            async with httpx.AsyncClient() as client:
                res = await client.post("https://models.inference.ai.azure.com/chat/completions", headers=headers, json=payload, timeout=45.0)
                
                if res.status_code == 200:
                    print(f"Barrot-Ω Response: {res.json()['choices'][0]['message']['content']}")
                else:
                    print(f"Lattice Breach ({res.status_code}): {res.text}")

if __name__ == "__main__":
    asyncio.run(genesis_loop())
