#!/usr/bin/env python

import sys, socket

class MpdClient():
    def connect(self, host="localhost", port=6600):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        sys.stderr.write(self.sock.recv(1024))
    
        return self.sock
    
    def send(self, cmd):
        self.sock.send(cmd.strip() + "\n")
        received = self.sock.recv(1024)
        return received

    def close(self):
        return self.sock.close()

mpdclient = MpdClient()

if __name__=="__main__":
    mpdclient.connect()
    print mpdclient.send(" ".join(sys.argv[1:]))
    mpdclient.close()
