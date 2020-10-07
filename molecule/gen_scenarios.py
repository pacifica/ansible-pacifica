#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to generate the molecule scenarios."""
import os
from os.path import join
from jinja2 import Template

WARNING_MSG = """
#####################################################################
# DO NOT EDIT THIS FILE!!!!!!!!!!!!!!
#
# NOTICE: This file is generated from a jinja2 template located in
#         the `molecule/common` folder.
#####################################################################
"""


def main():
    """Main method."""
    molecule_dir = os.path.dirname(__file__)
    platform_versions = {
        'centos': ['8'],
        'ubuntu': ['1804', '2004']
    }
    scenario_list = [
        'archiveinterface',
        'core',
        'default',
        'in',
        'notify',
        'out',
        'allinone',
        'twoinone'
    ]
    for scenario in scenario_list:
        molecule_tmplt = Template(
            open(join(molecule_dir, 'common', 'molecule.yml.j2')).read())
        converge_tmplt = Template(open(join(
            molecule_dir, 'common', '{}-converge.yml.j2'.format(scenario))).read())
        for platform, version_list in platform_versions.items():
            for version in version_list:
                os.makedirs(join(
                    molecule_dir, '{}-{}{}'.format(scenario, platform, version)), exist_ok=True)
                with open(join(
                    molecule_dir, '{}-{}{}'.format(scenario,
                                                   platform, version), 'molecule.yml'
                ), 'w') as mole_fd:
                    mole_fd.write('{}\n'.format(molecule_tmplt.render(
                        warning_msg=WARNING_MSG,
                        platform=platform,
                        platform_version=version,
                        scenario=scenario,
                    )))
                with open(join(
                    molecule_dir, '{}-{}{}'.format(scenario,
                                                   platform, version), 'converge.yml'
                ), 'w') as mole_fd:
                    mole_fd.write('{}\n'.format(converge_tmplt.render(
                        warning_msg=WARNING_MSG,
                        platform=platform,
                        platform_version=version,
                        scenario=scenario,
                    )))


if __name__ == '__main__':
    main()
