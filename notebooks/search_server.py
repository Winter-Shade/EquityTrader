from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS
from typing import Dict, Any

mcp = FastMCP("DuckDuckGo MCP Server")

@mcp.tool()
async def search(query: str, max_results: int = 5, region: str = "wt-wt") -> str:
    """Perform a DuckDuckGo web search.

    Args:
        query: The search query.
        max_results: Maximum number of results to return.
        region: Region code (e.g., "in-en", "us-en", "wt-wt" for global).
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, region=region, max_results=max_results))

        if not results:
            return "No results found."

        formatted = []
        for r in results:
            title = r.get("title", "No title")
            href = r.get("href", "No link")
            body = r.get("body", "")
            formatted.append(f"Title: {title}\nLink: {href}\nSnippet: {body}\n")

        return "\n".join(formatted)
    except Exception as e:
        return f"Error during DuckDuckGo search: {str(e)}"

if __name__ == "__main__":
    print("🚀 DuckDuckGo MCP Server running...")
    mcp.run()
