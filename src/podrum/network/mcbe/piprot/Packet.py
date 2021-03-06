"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

from podrum.utils.BinaryStream import BinaryStream

class Packet(BinaryStream):
    id = -1
    
    def getString(self):
        return self.get(self.getShort()).decode()
    
    def putString(self, value):
        self.putShort(len(value))
        self.put(value.encode())
        
    def getPosition(self):
        x = self.getFloat() - 128.0
        y = self.getFloat() - 64.0
        z = self.getFloat() - 128.0
        return [x, y, z]
    
    def putPosition(self, pos):
        x = pos[0] + 128.0
        y = pos[1] + 64.0
        z = pos[2] + 128.0
        self.putFloat(x)
        self.putFloat(y)
        self.putFloat(z)
    
    def decodePayload(self):
        pass
        
    def decode(self):
        self.getByte()
        self.decodePayload()
        
    def encodePayload(self):
        pass
        
    def encode(self):
        self.putByte(self.id)
        self.encodePayload()
