# Import
import time
import usb.core
import usb.util
import threading

class RelayController:

    # Class Attribute
    CLOSE_RELAY_CMD = [0xA0, 0x01, 0x01, 0xA2]
    OPEN_RELAY_CMD = [0xA0, 0x01, 0x00, 0xA1]


    # Initializer / Instance Attributes
    def __init__(self, vendor_id, product_id, activation_time):
        self._ep = self._get_usb_endpoint(vendor_id, product_id)
        self._activation_time = activation_time

    def _get_usb_endpoint(self, vendor_id, product_id):
        # search for our device by product and vendor ID
        dev = usb.core.find(idVendor=vendor_id, idProduct=product_id)
        # raise error if device is not found
        if dev is None:
            raise ValueError("Device not found")
        # get interface 0, alternate setting 0
        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)
        cfg = dev.get_active_configuration()
        intf = cfg[(0, 0)]
        # find the first (and in this case only) OUT endpoint in our interface
        ep = usb.util.find_descriptor(
            intf,
            custom_match=lambda e:
            usb.util.endpoint_direction(e.bEndpointAddress) ==
            usb.util.ENDPOINT_OUT)
        assert ep is not None
        return ep

    def activate_relay(self, activation_time=None):
        if activation_time is None:
            activation_time = self._activation_time
        self._ep.write(self.CLOSE_RELAY_CMD)
        timer = threading.Timer(activation_time, self._deactivate_relay)
        timer.start() 
    
    def _deactivate_relay(self):
        self._ep.write(self.OPEN_RELAY_CMD)