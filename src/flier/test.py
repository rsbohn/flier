import unittest
import flier
from os import environ

channel = environ.get("CHANNEL", "1001")

class EchoEndpoint(flier.Endpoint):
    eid = "37096"
    domain="surf"

    def do_echo(self, options):
        print options['message']

    def do_barn(self, attrs):
        print "barn:", attrs['action']
    do_suggestion = do_barn

def fixture():
    f = EchoEndpoint()
    f.channel=channel
    return f

class FirstFlight(unittest.TestCase):
    def setUp(self):
        self.ep = EchoEndpoint()
        self.ep.channel=channel

    def test_surf_up(self):
        self.ep.signal_event("up")
    
    def test_surf_down(self):
        self.ep.signal_event("down")
