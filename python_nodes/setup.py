from setuptools import find_packages, setup

package_name = 'python_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joush',
    maintainer_email='emmanuel.idiaquez@ucb.ecu.bo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node1=python_nodes.node1:main',
            'node2=python_nodes.node2:main',
            'odd_node=python_nodes.odd:main',
            'even_node=python_nodes.even:main',
            'calcule_eo=python_nodes.calculate_even_odd:main'
        ],
    },
)
