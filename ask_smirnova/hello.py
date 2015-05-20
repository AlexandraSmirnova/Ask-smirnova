from pprint import pformat

def application(environ, start_response):
	# show the environment:
	
	output = ['<pre>']
	output.append('<font face="Times New Roman" size="4"><h1>Hello, world!</h1>')
	output.append('Your GET request (example: "localhost:8081?s=123") ')
	output.append(pformat(environ['QUERY_STRING']))
	output.append(' </font> </pre>')

	#create a simple form:
	output.append('<form method="post">')
	output.append('<input type="text" name="test">')
	output.append('<input type="submit">')
	output.append('</form>')
	if environ['REQUEST_METHOD'] == 'POST':
   		# show form data as received by POST:
   		output.append('<font face="Times New Roman" size="4">Your POST request ')
   		output.append(pformat(environ['wsgi.input'].read()))
		output.append('</font>')
	# send results
	output_len = sum(len(line) for line in output)
 	start_response('200 OK', [('Content-type', 'text/html'), ('Content-Length', str(output_len))])
	return output
	
