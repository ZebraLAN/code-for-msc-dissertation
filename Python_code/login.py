#!/usr/bin/python

from PyKCS11 import *

lib = '/usr/lib/x86_64-linux-gnu/pkcs11-spy.so'
pkcs11 = PyKCS11Lib()
pkcs11.load(lib)

slot = pkcs11.getSlotList()[0]
session = pkcs11.openSession(slot, CKF_SERIAL_SESSION | CKF_RW_SESSION)

pin = '12345'
session.login(pin)
#session.logout()
