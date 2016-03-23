from urlparse import parse_qs

def wsgi_application(environ, start_response):
	status = "200 OK"
	headers = [
		("Content-Type", "text/plain")
	]
	start_response(status, headers)

	resList = []
	for (key, values) in parse_qs(environ.get("QUERY_STRING"), keep_blank_values=True).items():
		for value in values:
			resList.append("%s=%s" %(key, value))

	return ['\n'.join(resList)]
