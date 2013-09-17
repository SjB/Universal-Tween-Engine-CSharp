#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2012 SjB <steve@nca.uwo.ca>. All Rights Reserved.

import os
from waflib import Options

APPNAME = 'TweenEngineAPI'
VERSION = '8.0.30703'

top = '.'
out = 'build'

def options(ctx):
    ctx.load('cs_extra', tooldir='waftools/sjb-waftools/extra')

    ctx.add_option('--debug', '-d',
                dest='debug',
                action='store_true',
                default=False,
                help='Enable debug build')

    ctx.add_option('--default-assembly-dir',
                dest='default_assembly_dir',
                type='string',
                default=False,
                help='Location of local assembly repository')


def configure(ctx):
    ctx.load('cs_extra', tooldir='waftools/sjb-waftools/extra')

    ctx.env.APPNAME = APPNAME
    ctx.define_cond('DEBUG', Options.options.debug)

    ctx.env.default_assembly_dir = Options.options.default_assembly_dir
    if not ctx.env.default_assembly_dir:
        ctx.env.default_assembly_dir = os.environ.get('DEFAULT_ASSEMBLY_DIR', './libs')

    ctx.env.default_app_install_path = '${PREFIX}/lib/%s' % APPNAME


def generate_path_list(path, module):
        return '{0} {0}/{1}'.format(path, module)

def build(ctx):

    ctx(features = 'subst',
        source = 'TweenEngineAPI.pc.in',
        target = 'TweenEngineAPI.pc',
        install_path = '${PREFIX}/pkg-config',
        APPNAME = APPNAME,
        VERSION = VERSION)

    ctx.recurse([
        'TweenEngineAPI'
    ])
