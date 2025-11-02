"""
in readme file

This VM will be refactored using C++ in the future (for performance consideration), so this python version is only for prototyping and testing purpose.
"""

class InstructionSetArchitectureFileParser :
    def __init__(self, isa_path: str):
        if type(isa_path) is not str :
            raise TypeError("isa_path must be a string.")
        if not os.path.isfile(isa_path) :
            raise FileNotFoundError(f"ISA file not found: {isa_path}")
        
        with open(isa_path, 'r', encoding='utf-8') as f:
            self.isa_data = json.load(f)

        self.architecture                  = self.isa_data['architecture']

        self.modes                         = self.architecture['modes']
        self.registers                     = self.architecture['registers']
        self.flags                         = self.architecture['flags']

        self.bit_size                      = self.architecture['bit_size']
        self.endianness                    = self.architecture['endian']

        self.ISA_instructions              = self.isa_data['instructions']
        self.ISA_pseudoinstructions        = self.isa_data['pseudo_instructions']
        self.ISA_prefixes                  = self.isa_data['prefixes']
        self.ISA_interrupt_vectors         = self.isa_data['interrupt_vectors']

        self.assembler_encode_mnemonics    = self.isa_data['encode']

        # Build register table

        self.interger_registers                                          = self.registers['integer']
        self.interger_registers_minimum_privilege_level                  = self.interger_registers['minimum_privilege_level']

        self.single_precision_float_registers                            = self.registers['floating_point']['float']
        self.double_precision_float_registers                            = self.registers['floating_point']['double']
        self.float_registers_minimum_privilege_level                     = self.single_precision_float_registers['minimum_privilege_level']
        self.double_precision_float_registers_minimum_privilege_level    = self.double_precision_float_registers['minimum_privilege_level']

        self.control_registers                                           = self.registers['control']
        self.control_registers_minimum_privilege_level                   = self.control_registers['minimum_privilege_level']

        self.kernel_registers                                            = self.registers['kernel']
        self.kernel_registers_minimum_privilege_level                    = self.kernel_registers['minimum_privilege_level']

        # build flag table

        # self.flags                                                          = self.architecture['flags']

        # build instruction table

        # # Basic Instructions

        self.basic_instructions                          = self.ISA_instructions['basic']
        self.basic_control_instructions                  = self.basic_instructions['control']
        self.basic_data_transfer_instructions            = self.ISA_instructions['data_transfer']
        self.basic_arithmetic_instructions               = self.ISA_instructions['arithmetic']
        self.basic_logical_instructions                  = self.ISA_instructions['logic']
        self.basic_stack_operations_instructions         = self.ISA_instructions['stack_operations']
        self.basic_io_instructions                       = self.ISA_instructions['I/O']
        self.basic_load_store_instructions               = self.ISA_instructions['load_store']
        self.basic_branch_instructions                   = self.ISA_instructions['branch_or_jump']
        self.basic_floating_point_instructions           = self.ISA_instructions['floating_point']
        self.basic_coprocessor_instructions              = self.ISA_instructions['coprocessor']
        self.basic_system_call_instructions              = self.ISA_instructions['system_calls']

        # # Kernel Instructions

        self.kernel_instructions                         = self.ISA_instructions['kernel']
        self.kernel_interrupts_instructions              = self.kernel_instructions['interrupts']
        self.kernel_memory_management_instructions       = self.kernel_instructions['memory_management']
        self.kernel_context_switching_instructions       = self.kernel_instructions['context_switching']
        self.kernel_IO_management_instructions           = self.kernel_instructions['I/O_management']

        # # Hardware Instructions

        self.hardware_instructions                       = self.ISA_instructions['hardware']
        self.hardware_control_instructions               = self.hardware_instructions['control']
        self.hardware_device_management_instructions     = self.hardware_instructions['device_management']
        self.hardware_power_management_instructions      = self.hardware_instructions['power_management']

        # # Entended Instructions

        self.entended_instructions                       = self.ISA_instructions['entended']
        self.extended_XTU_instructions                   = self.entended_instructions['XTU_instructions']
        self.extended_BMU_instructions                   = self.entended_instructions['BMU_instructions']
        self.extended_MMU_instructions                   = self.entended_instructions['MMU_instructions']
        self.extended_CIU_instructions                   = self.entended_instructions['CIU_instructions']

        # TODO: Build hypervisor instructions table, virtualization instructions table, security instructions table.

        


    



import sys, os, re, time, numpy, math, random, multiprocessing, threading, json

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtCore import QThread, pyqtSignal, Qt

class ProgramAssembler :
    ...

class ProgramDisassembler :
    ...


class VitualMachineRuntimeExecutor :
    ...

class VirtualMachineRuntimeExceptions(Exception):
    ...


class VitualMachineMainUI_Window(QMainWindow):
    ...