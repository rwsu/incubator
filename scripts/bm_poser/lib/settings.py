#!/usr/bin/env python
#
# Copyright (c) 2012 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Local settings for """
import sys
import argparse
import libvirt

class settings(object):
    """Constants .. don't change this file unless you want to perm change the defaults"""
    
    # how many do you want to create (should be command line arg) 
    VMS = 1
    ARCH = "x86_64"
    ENGINE = "kvm"
    MAX_MEM = "524000"
    CPUS = "1" 
    BRIDGE = "br999"
    QEMU = "qemu:///system"
    BASE_NAME = 'bm_poser_'
    RUN_PATH = '/opt/stack/data/bm_poser/'
    TEMPLATE_DISK = 'template.qcow2'
    START_DELAY = 2
    TEMPLATE_XML = "template.xml"
    