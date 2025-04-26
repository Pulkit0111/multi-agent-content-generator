from api_client import tavily_client

def web_Search_tool(query):
    """
    Search the web for the query
    """
    results = []
    response = tavily_client.search(
        query=query,
        max_results=6,
        include_answer="advanced"
    )
    
    # Add the main answer if available
    if "answer" in response:
        results.append(response["answer"])
    
    # Add content from each result
    for result in response["results"]:
        if "content" in result:
            results.append(result["content"])
    
    return "\n".join(results)


