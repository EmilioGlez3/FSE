def _serve_file(self, rel_path):
	if not os.path.isfile(rel_path):
		self.send_error(404)
		return
	self.send_response(200)
	mime = magic.Magic(mime=True)
	self.send_header("Content-type", mime.from_file(rel_path))
	self.end_headers()
	with open(rel_path, ’rb’) as file:
		self.wfile.write(file.read())