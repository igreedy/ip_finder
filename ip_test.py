#!/usr/bin/env python
# encoding: utf-8

from socket import inet_aton

import os
import struct
import torndb
import pandas as pd


class IPIP(object):
    def __init__(self):
        self.offset = 0
        self.index = 0
        self.binary = ""
        dat_path = os.path.join('./', '17monipdb.dat')
        self.load(dat_path)

    def _unpack_V(self, b):
        return struct.unpack("<L", b)

    def _unpack_N(self, b):
        return struct.unpack(">L", b)

    def _unpack_C(self, b):
        return struct.unpack("B", b)

    def load(self, file):
        try:
            path = os.path.abspath(file)
            with open(path, "rb") as f:
                self.binary = f.read()
                self.offset, = self._unpack_N(self.binary[:4])
                self.index = self.binary[4:self.offset]
        except Exception as e:
            print e

    def find(self, ip):
        if not ip:
            return "N/A"
        nip = inet_aton(ip)
        ipdot = ip.split('.')
        if int(ipdot[0]) < 0 or int(ipdot[0]) > 255 or len(ipdot) != 4:
            return "N/A"

        tmp_offset = int(ipdot[0]) * 4
        start, = self._unpack_V(self.index[tmp_offset:tmp_offset + 4])

        index_offset = index_length = 0
        max_comp_len = self.offset - 1028
        start = start * 8 + 1024
        while start < max_comp_len:
            if self.index[start:start + 4] >= nip:
                index_offset, = self._unpack_V(self.index[start + 4:start + 7] + chr(0).encode('utf-8'))
                index_length, = self._unpack_C(self.index[start + 7])
                break
            start += 8

        if index_offset == 0:
            return "N/A"

        res_offset = self.offset + index_offset - 1024
        result = self.binary[res_offset:res_offset + index_length].decode('utf-8')
        return result

if __name__ == '__main__':
    ipfinder = IPIP()
    ip_lists = ['125.224.237.90', '202.106.58.118', '219.137.150.255']

    for ip in ip_lists:
        name = ipfinder.find(ip)
        print ip, name