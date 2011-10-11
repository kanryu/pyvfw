# -*- coding: utf-8 -*-
"""
##################################################################################
# PyVFW v0.0.1
#
# Copyright (C) 2011 KATO Kanryu <k.kanryu@gmail.com>
##################################################################################
#  This file is distibuted under 3-BSD
#  See COPYING file attached.
##################################################################################
# a sample to direct call userdriver for VIDEO FOR WINDOWS 
"""

import sys
import ctypes
from ctypes import windll, c_int, c_char_p, c_uint, byref, c_void_p, Structure

def mmioFOURCC(*lst):
    result = 0
    for s in reversed(lst):
        result = ord(s) + result * 256
#        print result, s, ord(s)
    return result


# VFW codec constant values
DRVCNF_CANCEL      = 0x0000
DRVCNF_OK          = 0x0001
DRVCNF_RESTART     = 0x0002

DRV_CANCEL         = DRVCNF_CANCEL
DRV_OK             = DRVCNF_OK
DRV_RESTART        = DRVCNF_RESTART

DRV_LOAD           = 0x0001
DRV_ENABLE         = 0x0002
DRV_OPEN           = 0x0003
DRV_CLOSE          = 0x0004
DRV_DISABLE        = 0x0005
DRV_FREE           = 0x0006
DRV_CONFIGURE      = 0x0007
DRV_QUERYCONFIGURE = 0x0008
DRV_INSTALL        = 0x0009
DRV_REMOVE         = 0x000A
DRV_EXITSESSION    = 0x000B
DRV_POWER          = 0x000F
DRV_RESERVED       = 0x0800
DRV_USER           = 0x4000

ICM_USER          = (DRV_USER+0x0000)
ICM_RESERVED_LOW  = (DRV_USER+0x1000)
ICM_RESERVED_HIGH = (DRV_USER+0x2000)
ICM_RESERVED      = ICM_RESERVED_LOW
ICM_GETSTATE      = (ICM_RESERVED+0) 
ICM_SETSTATE      = (ICM_RESERVED+1) 
ICM_GETINFO       = (ICM_RESERVED+2) 
ICM_CONFIGURE     = (ICM_RESERVED+10)
ICM_ABOUT         = (ICM_RESERVED+11)
ICM_GETERRORTEXT  = (ICM_RESERVED+12)
ICM_GETFORMATNAME = (ICM_RESERVED+20)
ICM_ENUMFORMATS	  = (ICM_RESERVED+21)
ICM_GETDEFAULTQUALITY = (ICM_RESERVED+30)
ICM_GETQUALITY    = (ICM_RESERVED+31)
ICM_SETQUALITY    = (ICM_RESERVED+32)
ICM_SET			  = (ICM_RESERVED+40)
ICM_GET			  = (ICM_RESERVED+41)
ICM_FRAMERATE     = mmioFOURCC('F','r','m','R')
ICM_KEYFRAMERATE  = mmioFOURCC('K','e','y','R')
ICM_COMPRESS_GET_FORMAT    = (ICM_USER+4) 
ICM_COMPRESS_GET_SIZE      = (ICM_USER+5) 
ICM_COMPRESS_QUERY         = (ICM_USER+6) 
ICM_COMPRESS_BEGIN         = (ICM_USER+7) 
ICM_COMPRESS               = (ICM_USER+8) 
ICM_COMPRESS_END           = (ICM_USER+9) 
ICM_DECOMPRESS_GET_FORMAT  = (ICM_USER+10)
ICM_DECOMPRESS_QUERY       = (ICM_USER+11)
ICM_DECOMPRESS_BEGIN       = (ICM_USER+12)
ICM_DECOMPRESS             = (ICM_USER+13)
ICM_DECOMPRESS_END         = (ICM_USER+14)
ICM_DECOMPRESS_SET_PALETTE = (ICM_USER+29)
ICM_DECOMPRESS_GET_PALETTE = (ICM_USER+30)
ICM_DRAW_QUERY             = (ICM_USER+31)
ICM_DRAW_BEGIN             = (ICM_USER+15)
ICM_DRAW_GET_PALETTE       = (ICM_USER+16)
ICM_DRAW_UPDATE            = (ICM_USER+17)
ICM_DRAW_START             = (ICM_USER+18)
ICM_DRAW_STOP              = (ICM_USER+19)
ICM_DRAW_BITS              = (ICM_USER+20)
ICM_DRAW_END               = (ICM_USER+21)
ICM_DRAW_GETTIME           = (ICM_USER+32)
ICM_DRAW                   = (ICM_USER+33)
ICM_DRAW_WINDOW            = (ICM_USER+34)
ICM_DRAW_SETTIME           = (ICM_USER+35)
ICM_DRAW_REALIZE           = (ICM_USER+36)
ICM_DRAW_FLUSH	           = (ICM_USER+37)
ICM_DRAW_RENDERBUFFER      = (ICM_USER+38)
ICM_DRAW_START_PLAY        = (ICM_USER+39)
ICM_DRAW_STOP_PLAY         = (ICM_USER+40)
ICM_DRAW_SUGGESTFORMAT     = (ICM_USER+50)
ICM_DRAW_CHANGEPALETTE     = (ICM_USER+51)
ICM_DRAW_IDLE              = (ICM_USER+52)
ICM_GETBUFFERSWANTED       = (ICM_USER+41)
ICM_GETDEFAULTKEYFRAMERATE = (ICM_USER+42)
ICM_DECOMPRESSEX_BEGIN     = (ICM_USER+60)
ICM_DECOMPRESSEX_QUERY     = (ICM_USER+61)
ICM_DECOMPRESSEX           = (ICM_USER+62)
ICM_DECOMPRESSEX_END       = (ICM_USER+63)
ICM_COMPRESS_FRAMES_INFO   = (ICM_USER+70)
ICM_COMPRESS_FRAMES        = (ICM_USER+71)
ICM_SET_STATUS_PROC	       = (ICM_USER+72)


ICERR_OK           = 0x0
ICERR_UNSUPPORTED  = -1
ICERR_BADFORMAT    = -2
ICERR_MEMORY       = -3
ICERR_INTERNAL     = -4
ICERR_BADFLAGS     = -5
ICERR_BADPARAM     = -6
ICERR_BADSIZE      = -7
ICERR_BADHANDLE    = -8
ICERR_CANTUPDATE   = -9
ICERR_ABORT	       = -10
ICERR_ERROR        = -100
ICERR_BADBITDEPTH  = -200
ICERR_BADIMAGESIZE = -201

ICTYPE_VIDEO = mmioFOURCC('v', 'i', 'd', 'c')
ICTYPE_AUDIO = mmioFOURCC('a', 'u', 'd', 'c')

class ICOPEN(Structure):
    _fields_ = [
        ('dwSize', c_uint),
        ('fccType', c_uint),
        ('fccHandler', c_uint),
        ('dwVersion', c_uint),
        ('dwFlags', c_uint),
        ('dwError', c_uint),
        ('pV1Reserved', c_void_p),
        ('pV2Reserved', c_void_p),
        ('dnDevNode', c_uint),
    ]

class DriverVFW(object):
    def __init__(self, name):
        self.driver = ctypes.WinDLL(name)
        print self.driver
        self.proc = self.driver.DriverProc
        print self.proc

    def open(self):
        self.icopen = ICOPEN()
        self.icopen.dwSize = ctypes.sizeof(self.icopen)
        self.icopen.fccType = ICTYPE_VIDEO
        self.driver_id = self.proc(0, 0, DRV_OPEN, 0, byref(self.icopen))
        print self.driver_id

    def close(self):
        result = self.proc(self.driver_id, 0, DRV_CLOSE, 0, 0)
        print result

    def _call(self, message_id, lparam1, lparam2):
        result = self.proc(self.driver_id, 0, message_id, lparam1, lparam2)
        print result
        return result

    # state messages
    def get_state(self, lparam1, lparam2):
        return self._call(ICM_GETSTATE, byref(lparam1), lparam2)

    def set_state(self, lparam1, lparam2):
        return self._call(ICM_SETSTATE, byref(lparam1), lparam2)

    def get_info(self, icinfo, lparam2):
        return self._call(ICM_GETINFO, byref(lparam1), lparam2)

    def dialog_configure(self, hwnd=c_int(-1)):
        return self._call(ICM_CONFIGURE, byref(hwnd), 0)

    def dialog_about(self, hwnd=c_int(-1)):
        return self._call(ICM_ABOUT, byref(hwnd), 0)

    def get_defaultquality(self):
        lparam1 = c_int(0)
        self.proc(self.driver_id, 0, ICM_GETDEFAULTQUALITY, byref(lparam1), 0)
        return lparam1.value

    # compression messages
    def compress_query(self, bmin, bmout):
        return self._call(ICM_COMPRESS_QUERY, byref(bmin), byref(bmout))
        
    def compress_begin(self, bmin, bmout):
        return self._call(ICM_COMPRESS_BEGIN, byref(bmin), byref(bmout))
        
    def compress_get_format(self, bmin, bmout):
        return self._call(ICM_COMPRESS_GET_FORMAT, byref(bmin), byref(bmout))
        
    def compress_get_size(self, bmin, bmout):
        return self._call(ICM_COMPRESS_GET_SIZE, byref(bmin), byref(bmout))
        
    def compress(self, icomp, lparam2):
        return self._call(ICM_COMPRESS, byref(icomp), lparam2)
        
    def compress_end(self, bmin, bmout):
        return self._call(ICM_COMPRESS_END, 0, 0)
        
    # decompress messages
    def decompress_query(self, bmin, bmout):
        return self._call(ICM_DECOMPRESS_QUERY, byref(bmin), byref(bmout))
        
    def decompress_begin(self, bmin, bmout):
        return self._call(ICM_DECOMPRESS_BEGIN, byref(bmin), byref(bmout))
        
    def decompress_get_format(self, bmin, bmout):
        return self._call(ICM_DECOMPRESS_GET_FORMAT, byref(bmin), byref(bmout))
        
    def decompress_get_palette(self, bmin, bmout):
        return self._call(ICM_DECOMPRESS_GET_PALETTE, byref(bmin), byref(bmout))
        
    def decompress(self, icomp, lparam2):
        return self._call(ICM_DECOMPRESS, byref(icomp), lparam2)
        
    def decompress_end(self, bmin, bmout):
        return self._call(ICM_DECOMPRESS_END, 0, 0)
        

if __name__ == '__main__':
    drv = DriverVFW("Lagarith")
    drv.open()
    print drv.get_defaultquality()
    drv.close()
    sys.exit()

