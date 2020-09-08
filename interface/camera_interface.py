# -*- coding: utf-8 -*-

"""
This file contains the Qudi Interface for a camera.


Qudi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Qudi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Qudi. If not, see <http://www.gnu.org/licenses/>.

Copyright (c) the Qudi Developers. See the COPYRIGHT.txt file at the
top-level directory of this distribution and at <https://github.com/Ulm-IQO/qudi/>
"""

from core.interface import abstract_interface_method
from core.meta import InterfaceMetaclass


class CameraInterface(metaclass=InterfaceMetaclass):
    """ This interface is used to manage and visualize a simple camera
    """

    @abstract_interface_method
    def get_name(self):
        """ Retrieve an identifier of the camera that the GUI can print

        @return string: name for the camera
        """
        pass

    @abstract_interface_method
    def get_size(self):
        """ Retrieve size of the image in pixel

        @return tuple: Size (width, height)
        """
        pass

    @abstract_interface_method
    def support_live_acquisition(self):
        """ Return whether or not the camera can take care of live acquisition

        @return bool: True if supported, False if not
        """
        pass

    @abstract_interface_method
    def start_live_acquisition(self):
        """ Start a continuous acquisition

        @return bool: Success ?
        """
        pass

    @abstract_interface_method
    def get_ready_state(self):
        """ Is the camera ready for an acquisition ?

        @return bool: ready ?
        """
        pass

    @abstract_interface_method
    def start_single_acquisition(self):
        """ Start a single acquisition

        @return bool: Success ?
        """
        pass

    @abstract_interface_method
    def stop_acquisition(self):
        """ Stop/abort live or single acquisition

        @return bool: Success ?
        """
        pass

    @abstract_interface_method
    def get_acquired_data(self):
        """ Return an array of last acquired image.

        @return numpy array: image data in format [[row],[row]...]

        Each pixel might be a float, integer or sub pixels
        """
        pass

    @abstract_interface_method
    def set_exposure(self, exposure):
        """ Set the exposure time in seconds

        @param float exposure: desired new exposure time

        @return float: setted new exposure time
        """
        pass

    @abstract_interface_method
    def get_exposure(self):
        """ Get the exposure time in seconds

        @return float exposure time
        """
        pass

    @abstract_interface_method
    def set_amplifiers(self, names):
        """ Set the amplifier

        @param list names: Set the amplifiers to be used.

        @return float:  bool success ?
        """
        pass

    @abstract_interface_method
    def get_amplifiers(self):
        """ Get the currently used amplifiers

        @return float: current gain
        """
        pass

    @abstract_interface_method
    def set_gains(self, gain_dict):
        """ Set the gains of selected amplifiers

        @param float gains: desired new gain {'preamp': 2}

        @return float: new gain
        """
        pass

    @abstract_interface_method
    def get_gains(self):
        """ Get the gain

        @return dictionary: Return a dictionary with amplifiers e.g. {'preamp': 2}
        """
        pass

    @abstract_interface_method
    def get_available_readout_speeds(self):
        """
        Readout speeds on the device
        @return: list of available readout speeds on the device
        """
        pass

    @abstract_interface_method
    def set_readout_speeds(self, speed_dict):
        """ Set the readout speed e.g. {'horizontal': 10e6, 'vertical':1e6} in Hz

        @return float: exposure gain
        """
        pass

    @abstract_interface_method
    def get_readout_speeds(self):
        """
        get the current readout speed e.g. {'horizontal': 1e6, 'vertical':3e6} in Hz
        @return:
        """
        pass

    @abstract_interface_method
    def set_up_sensor_area(self, settings):
        """
        Binning and extracting a certain part of the sensor e.g. {'binning': (2,2), 'crop' (128, 256)} takes 4 pixels
        together to 1 and takes from all the pixels and area of 128 by 256
        @return:
        """
        pass

    @abstract_interface_method
    def get_sensor_area_settings(self):
        """
        Return the current binning and crop settings of the sensor e.g. {'binning': (2,2), 'crop' (128, 256)}
        @return: dict of the sensor area settings
        """
        pass

    @abstract_interface_method
    def get_available_readout_modes(self):
        """
        Readout modes on the device
        @return: list of available readout modes
        """
        pass

    @abstract_interface_method
    def set_readout_mode(self, readout_mode):
        """
        Set the readout mode of the camera ('single acquisition', 'kinetic series')
        @param str readout_mode: readout mode to be set
        @return: Success ?
        """
        pass

    @abstract_interface_method
    def get_readout_mode(self):
        """
        Set the readout mode of the camera
        @return: Success ?
        """
        pass

    @abstract_interface_method
    def set_up_image_sequence(self, num_images, exposures):
        """
        Set up the camera for the acquisition of an image sequence.

        @param float num_images: number of images to be taken
        @param list exposures: list of length(num_images) containing the exposures to be used
        @return:
        """
        pass

    @abstract_interface_method
    def acquire_image_sequence(self):
        """
        Takes a sequence of images
        @return: numpy nd array of dimension (seq_length, px_x, px_y)  
        """
        pass

    @abstract_interface_method
    def get_available_trigger_modes(self):
        """
        Trigger modes on the device
        @return: list of available trigger modes
        """
        pass

    @abstract_interface_method
    def set_up_triggering(self, trigger_mode):
        """
        Set the trigger mode ('Internal', 'External' ... )
        @param str trigger_mode: Target trigger mode
        @return: Success ?
        """
        pass

    @abstract_interface_method
    def get_trigger_mode(self):
        """
        Get the currently used trigger mode
        @return: String of the set trigger mode
        """
        pass

    @abstract_interface_method
    def open_shutter(self):
        """
        Oen a shutter if the camera has a shutter
        @return: Success ?
        """
        pass

    @abstract_interface_method
    def close_shutter(self):
        """
        Close the shutter if the camera has a shutter
        @return: Success ?
        """
        pass

    @abstract_interface_method
    def set_temperature(self, temperature):
        """
        Sets the temperature of the camera
        @param float temperature: Target temperature of the camera
        @return: success?
        """
        pass

    @abstract_interface_method
    def get_temperature(self):
        """
        Gets the temperature of the camera
        @return: success?
        """
        pass



