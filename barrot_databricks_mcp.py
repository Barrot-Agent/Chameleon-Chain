import asyncio, os, json, httpx
from mcp.server.stdio import stdio_server
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("barrot-databricks-bridge")
TOKEN = os.environ.get("DATABRICKS_TOKEN")
HOST = "https://adb-26479705.azuredatabricks.net"

@server.list_tools()
async def handle_list_tools():
    return [Tool(name="query_apex", description="Ternary Logic Ingress.", inputSchema={"type":"object","properties":{"sql":{"type":"string"}},"required":["sql"]})]

@server.call_tool()
async def handle_call_tool(name, arguments):
    if name == "query_apex":
        url = f"{HOST}/api/2.0/sql/statements"
        headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
        payload = {
            "warehouse_id": "4940f81d1844b6c6",
            "statement": arguments["sql"],
            "catalog": "hive_metastore",
            "schema": "barrot_omega"
        }
        async with httpx.AsyncClient(verify=False) as client:
            try:
                resp = await client.post(url, headers=headers, json=payload, timeout=30.0)
                return [TextContent(type="text", text=resp.text)]
            except Exception as e:
                return [TextContent(type="text", text=f"Lattice Breach: {str(e)}")]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
