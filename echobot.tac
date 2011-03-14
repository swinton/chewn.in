from twisted.application import service
from twisted.words.protocols.jabber import jid
from wokkel.client import XMPPClient

from echobot import EchoBotProtocol

application = service.Application("echobot")

xmppclient = XMPPClient(jid.internJID("nmstereo@chief-chirpas-macbook-pro.local/echobot"), "welcome")
xmppclient.logTraffic = False
echobot = EchoBotProtocol()
echobot.setHandlerParent(xmppclient)
xmppclient.setServiceParent(application)
