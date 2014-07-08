import webapp2

root = webapp2.WSGIApplication(
    [('/', "main.MainHandler")],
    debug=True
)
