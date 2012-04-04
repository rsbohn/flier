import urllib2
from urllib import urlencode
import json

debug=False

def first_flight():
    print "Hello from Python."

sky = "http://cs.kobj.net"
class Endpoint(object):
    domain = 'flier'
    eid = 0
    channel = 1
    def signal_event(self, event_name, args={}):
        response = self.post(
            "/sky/event/{0}/{1}".format(self.channel, self.eid),
            event_name, args)
        if debug: print response
        directives = json.loads(response).get('directives')
        for d in directives:
            self.perform(d.get('name'), d.get('options'))

    def post(self, url, _type, args):
        if not args.get('_domain'):
            args['_domain'] = self.domain
        args['_type'] = _type

        if debug: print ">>", args
        req = urllib2.Request(
            sky+url,
            data=urlencode(args))
        f = urllib2.urlopen(req)
        response=[n for n in f.readlines() if not n.startswith("//")]
        return ''.join(response)

    def perform(self, directive, options):
        getattr(self, "do_"+directive)(options)

