import flier

flier.debug=True
class Detector(flier.Endpoint):
    domain = "alien"
    def perform(self, directive, options):
        print directive

def main():
    ad = Detector()
    ad.eid = 42
    print "Test Klingon detector:"
    ad.signal_event("detected", {
        "_rids":"a421x110",
        "race":"Klingon"})

    print "Test Wookie detector:"
    ad.signal_event("detected", {
        "_rids":"a421x110",
        "race":"Wookie"})

if __name__ == "__main__":
    main()
      
