def application(environ, start_response):
    response_body = b'Hello Word!'
    status = '200 OK'
    headers = [('Content-type', 'text/plain;charset=UTF-8')]
    start_response(status, headers)
    return [response_body]
