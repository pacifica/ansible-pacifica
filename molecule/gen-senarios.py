#!/usr/bin/python
import os
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from jinja2 import Template

def main():
    """Main method."""
    molecule_dir = os.path.dirname(__file__)
    platform_versions = {
        'centos': ['7'],
        'ubuntu': ['18.04']
    }
    scenario_list = [
        'archiveinterface',
        'core',
        'default',
        'in',
        'notify',
        'out'
    ]
    for scenario in scenario_list:
        molecule_tmplt = Template(open(os.path.join(molecule_dir, 'common', 'molecule.yml.j2'.format(scenario))).read())
        converge_tmplt = Template(open(os.path.join(molecule_dir, 'common', '{}-converge.yml.j2'.format(scenario))).read())
        for platform, version_list in platform_versions.items():
            for version in version_list:
                os.makedirs(os.path.join(molecule_dir, '{}-{}{}'.format(scenario, platform, version)), exist_ok=True)
                with open(os.path.join(molecule_dir, '{}-{}{}'.format(scenario, platform, version), 'molecule.yml'), 'w') as mole_fd:
                    mole_fd.write('{}\n'.format(molecule_tmplt.render(
                        platform=platform,
                        platform_version=version,
                        scenario=scenario,
                    )))
                with open(os.path.join(molecule_dir, '{}-{}{}'.format(scenario, platform, version), 'converge.yml'), 'w') as mole_fd:
                    mole_fd.write('{}\n'.format(converge_tmplt.render(
                        platform=platform,
                        platform_version=version,
                        scenario=scenario,
                    )))

if __name__ == '__main__':
    main()