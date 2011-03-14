from twisted.application import service
from twisted.words.protocols.jabber import jid
from wokkel.client import XMPPClient

from stereobot import StereoBotProtocol

application = service.Application("stereobot")

xmppclient = XMPPClient(jid.internJID("nmstereo@chief-chirpas-macbook-pro.local/stereobot"), "welcome")
xmppclient.logTraffic = False
stereobot = StereoBotProtocol()
stereobot.setHandlerParent(xmppclient)
xmppclient.setServiceParent(application)
