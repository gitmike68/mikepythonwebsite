def hello(environ, start_response):
    status="200 OK"
    headers=[("Content-Type","text/plain")]
    body=""
    if "QUERY_STRING" in environ:
        for param in environ["QUERY_STRING"].split("&"):
            body+=param
    start_response(status,headers)

    return [body]