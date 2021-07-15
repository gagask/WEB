
def test(environ, start_response):
	body = ['\r\n'.join(environ['QUERY_STRING'].split('&')).encode()]
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return body
