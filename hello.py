
def test(environ, start_response):
	body = [str(i + '\n').encode('ascii') for i in environ['QUERY_STRING'].split('&')]
	start_response('200 OK', [('Content-Type', 'text/plain'),('Content-Length', str(len(body)))])
	return body
