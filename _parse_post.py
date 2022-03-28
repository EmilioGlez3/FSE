def _parse_post(self, json_obj):
	if not ’action’ in json_obj or not ’value’ in json_obj:
		return
	switcher = {
		’led’ : leds,
		’marquee’ : marquee,
		’numpad’ : bcd
	}
func = switcher.get(json_obj[’action’], None)
if func:
	print(’\tCall{}({})’.format(func, json_obj[’value’]))
	func(json_obj[’value’])