import socket

from twisted.words.xish import domish
from wokkel.xmppim import MessageProtocol, AvailablePresence

import mpdclient

class StereoBotProtocol(MessageProtocol):
    def __init__(self):
        MessageProtocol.__init__(self)
        self.mpdclient = mpdclient.MpdClient()
        self.mpdclient.connect()

    def connectionMade(self):
        print "Connected!"

        # send initial presence
        self.send(AvailablePresence())

    def connectionLost(self, reason):
        print "Disconnected!"

    def onMessage(self, msg):
        print str(msg)

        if msg["type"] == 'chat' and hasattr(msg, "body") and msg.body != None:
            response = self.mpdclient.send(str(msg.body))
            
            reply = domish.Element((None, "message"))
            reply["to"] = msg["from"]
            reply["from"] = msg["to"]
            reply["type"] = 'chat'
            
            reply.addElement("body", content=str(response))

            self.send(reply)
