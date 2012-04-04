import urllib2
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
        _domain = args.get('_domain') or self.domain

        if debug: print args
        req = urllib2.Request(
            sky+url+"/"+_domain+"/"+_type, 
            headers={
                "Content-Type": "application/json"
                },
            data=json.dumps(args))
        f = urllib2.urlopen(req)
        response=[n for n in f.readlines() if not n.startswith("//")]
        return ''.join(response)

    def perform(self, directive, options):
        getattr(self, "do_"+directive)(options)

