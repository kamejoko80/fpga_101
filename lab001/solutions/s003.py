from migen import *
from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform

#
# platform
#

_io = [
    ("user_led",  0, Pins("H17"), IOStandard("LVCMOS33")),
    ("user_led",  1, Pins("K15"), IOStandard("LVCMOS33")),
    ("user_led",  2, Pins("J13"), IOStandard("LVCMOS33")),
    ("user_led",  3, Pins("N14"), IOStandard("LVCMOS33")),
    ("user_led",  4, Pins("R18"), IOStandard("LVCMOS33")),
    ("user_led",  5, Pins("V17"), IOStandard("LVCMOS33")),
    ("user_led",  6, Pins("U17"), IOStandard("LVCMOS33")),
    ("user_led",  7, Pins("U16"), IOStandard("LVCMOS33")),
    ("user_led",  8, Pins("V16"), IOStandard("LVCMOS33")),
    ("user_led",  9, Pins("T15"), IOStandard("LVCMOS33")),
    ("user_led", 10, Pins("U14"), IOStandard("LVCMOS33")),
    ("user_led", 11, Pins("T16"), IOStandard("LVCMOS33")),
    ("user_led", 12, Pins("V15"), IOStandard("LVCMOS33")),
    ("user_led", 13, Pins("V14"), IOStandard("LVCMOS33")),
    ("user_led", 14, Pins("V12"), IOStandard("LVCMOS33")),
    ("user_led", 15, Pins("V11"), IOStandard("LVCMOS33")),

    ("user_sw",  0, Pins("J15"), IOStandard("LVCMOS33")),
    ("user_sw",  1, Pins("L16"), IOStandard("LVCMOS33")),
    ("user_sw",  2, Pins("M13"), IOStandard("LVCMOS33")),
    ("user_sw",  3, Pins("R15"), IOStandard("LVCMOS33")),
    ("user_sw",  4, Pins("R17"), IOStandard("LVCMOS33")),
    ("user_sw",  5, Pins("T18"), IOStandard("LVCMOS33")),
    ("user_sw",  6, Pins("U18"), IOStandard("LVCMOS33")),
    ("user_sw",  7, Pins("R13"), IOStandard("LVCMOS33")),
    ("user_sw",  8, Pins("T8"), IOStandard("LVCMOS33")),
    ("user_sw",  9, Pins("U8"), IOStandard("LVCMOS33")),
    ("user_sw", 10, Pins("R16"), IOStandard("LVCMOS33")),
    ("user_sw", 11, Pins("T13"), IOStandard("LVCMOS33")),
    ("user_sw", 12, Pins("H6"), IOStandard("LVCMOS33")),
    ("user_sw", 13, Pins("U12"), IOStandard("LVCMOS33")),
    ("user_sw", 14, Pins("U11"), IOStandard("LVCMOS33")),
    ("user_sw", 15, Pins("V10"), IOStandard("LVCMOS33")),

    ("user_btn", 0, Pins("N17"), IOStandard("LVCMOS33")),

    ("clk100", 0, Pins("E3"), IOStandard("LVCMOS33")),

    ("cpu_reset", 0, Pins("C12"), IOStandard("LVCMOS33")),
]


class Platform(XilinxPlatform):
    default_clk_name = "clk100"
    default_clk_period = 10.0

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a100t-CSG324-1", _io, toolchain="vivado")

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)

#
# design
#


# create our platform (fpga interface)
platform = Platform()

# create our module (fpga description)
class Switches(Module):
    def __init__(self, platform):     
        # synchronous assignments
        self.sync += []
        # combinatorial assignements
        for i in range(16):
            led = platform.request("user_led", i)
            sw = platform.request("user_sw", i)
            self.comb += led.eq(sw)

module = Switches(platform)

#
# build
#

platform.build(module)