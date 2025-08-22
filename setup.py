from setuptools import setup
import os
from glob import glob

package_name = 'boat_navigation'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('lib', package_name), glob('scripts/*.sh')),  # << añade los scripts
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Brayan Saldarriaga',
    maintainer_email='brayanjavsa@gmail.com',
    description='Bringup y navegación del bote.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={  # podés dejar vacío si no hay scripts Python
        'console_scripts': [],
    },
)
