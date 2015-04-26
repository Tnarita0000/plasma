#!/usr/bin/env python3
#
# Reverse : Generate an indented asm code (pseudo-C) with colored syntax.
# Copyright (C) 2015    Joel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.    If not, see <http://www.gnu.org/licenses/>.
#


import lib.fileformat.binary


class Raw:
    def __init__(self, filename, bits):
        import capstone as CAPSTONE

        self.raw = open(filename, "rb").read()
        self.bits = bits
        self.arch_lookup = {
            32: CAPSTONE.CS_MODE_32,
            64: CAPSTONE.CS_MODE_64,
        }


    def load_static_sym(self):
        return


    def load_dyn_sym(self):
        return


    def load_data_sections(self):
        return


    def is_address(self, imm):
        return None, False


    def get_section(self, addr):
        flags = {
            "exec": True
        }
        return (self.raw, 0, flags)


    def get_string(self, addr):
        return ""


    def get_arch(self):
        import capstone as CAPSTONE
        return CAPSTONE.CS_ARCH_X86, self.arch_lookup[self.bits]


    def get_arch_string(self):
        return ""


    def get_entry_point(self):
        return 0


    def iter_sections(self):
        return []
