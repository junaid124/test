#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: OFDM 256QAM
# Author: Muhammad Junaid
# Description: NRTC Haripur pk
# Generated: Wed Jul  8 00:46:14 2015
##################################################

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import gr, digital, analog
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sys
import time

from distutils.version import StrictVersion
class GSM_OFDM_LTE_E300(gr.top_block, Qt.QWidget):

    def __init__(self, address="addr=192.168.10.2"):
        gr.top_block.__init__(self, "OFDM 256QAM")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("OFDM 256QAM")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "GSM_OFDM_LTE_E300")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.address = address

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e6
        self.samp_0 = samp_0 = 6.5e6
        self.CENTRAL_FREQEUNCY_USRP_Ch1 = CENTRAL_FREQEUNCY_USRP_Ch1 = 2145e6
        self.BW_USRP = BW_USRP = 50e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		args="scalar=1024",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_subdev_spec("B:0", 0)
        self.uhd_usrp_sink_0.set_samp_rate(5e6)
        self.uhd_usrp_sink_0.set_center_freq(CENTRAL_FREQEUNCY_USRP_Ch1, 0)
        self.uhd_usrp_sink_0.set_gain(27, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_bandwidth(BW_USRP, 0)
        self.digital_ofdm_mod_1 = grc_blks2.packet_mod_f(digital.ofdm_mod(
        		options=grc_blks2.options(
        			modulation="bpsk",
        			fft_length=1024,
        			occupied_tones=1000,
        			cp_length=0,
        			pad_for_usrp=True,
        			log=None,
        			verbose=None,
        		),
        	),
        	payload_length=0,
        )
        self.digital_cpmmod_bc_1 = digital.cpmmod_bc(analog.cpm.LREC, 2, 2, 2, 2)
        self.blocks_vector_source_x_1 = blocks.vector_source_f((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0,1, 1,0, 0, 1,0,1, 1, 1,0, 0, 1,0,1), True, 1, [])
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_f((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0,1, 1,0, 0, 1,0,1, 1, 1,0, 0, 1,0,1), True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_f((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0,1, 1,0, 0, 1,0,1, 1, 1,0, 0, 1,0,1), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_f((1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0,1, 1,0, 0, 1,0,1, 0, 1,0, 0, 1,0,1), True, 1, [])
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.digital_ofdm_mod_1, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.digital_cpmmod_bc_1, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_vector_source_x_1, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.digital_cpmmod_bc_1, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.digital_ofdm_mod_1, 0), (self.uhd_usrp_sink_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "GSM_OFDM_LTE_E300")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_samp_0(self):
        return self.samp_0

    def set_samp_0(self, samp_0):
        self.samp_0 = samp_0

    def get_CENTRAL_FREQEUNCY_USRP_Ch1(self):
        return self.CENTRAL_FREQEUNCY_USRP_Ch1

    def set_CENTRAL_FREQEUNCY_USRP_Ch1(self, CENTRAL_FREQEUNCY_USRP_Ch1):
        self.CENTRAL_FREQEUNCY_USRP_Ch1 = CENTRAL_FREQEUNCY_USRP_Ch1
        self.uhd_usrp_sink_0.set_center_freq(self.CENTRAL_FREQEUNCY_USRP_Ch1, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.CENTRAL_FREQEUNCY_USRP_Ch1, 1)

    def get_BW_USRP(self):
        return self.BW_USRP

    def set_BW_USRP(self, BW_USRP):
        self.BW_USRP = BW_USRP
        self.uhd_usrp_sink_0.set_bandwidth(self.BW_USRP, 0)
        self.uhd_usrp_sink_0.set_bandwidth(self.BW_USRP, 1)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-a", "--address", dest="address", type="string", default="addr=192.168.10.2",
        help="Set IP Address [default=%default]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = GSM_OFDM_LTE_E300(address=options.address)
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
