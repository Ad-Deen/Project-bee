from setuptools import find_packages, setup
import os

package_name = 'bee'

def collect_files(directory):
    files = []
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            files.append(os.path.join(dirpath, f))
    return files

# Collect files from folders you want installed
launch_files = collect_files('launch') if os.path.exists('launch') else []
mesh_files = collect_files('meshes') if os.path.exists('meshes') else []
urdf_files = collect_files('urdf') if os.path.exists('urdf') else []
world_files = collect_files('worlds') if os.path.exists('worlds') else []
rviz_files = collect_files('rviz') if os.path.exists('rviz') else []
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    package_data={'': ['resource/bee']},
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', launch_files),
        ('share/' + package_name + '/meshes', mesh_files),
        ('share/' + package_name + '/urdf', urdf_files),
        ('share/' + package_name + '/worlds', world_files),
        ('share/' + package_name + '/rviz', rviz_files),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='deen',
    maintainer_email='deen@todo.todo',
    description='Drone perception and control package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control = bee.control.manual_control:main',
            'plotter = bee.control.gyro_plot_node:main',
            'cam1 = bee.perception.drone_camera1:main',
            'cam2 = bee.perception.drone_camera2:main',
            'logger = bee.perception.vid_log:main',
            'cam_filter = bee.perception.cam_filter:main',
            'vid_publisher = bee.perception.vid_publisher:main',
            'accumulator = bee.perception.keypoint_accumulator:main',
            'odometry = bee.perception.odometry:main',
            'pcd_generator = bee.perception.pcd_generator:main',
            'aligner_3D = bee.perception.aligner_3D:main',
            'sparse_map_builder = bee.perception.sparse_map_builder:main',
            'drift_detect = bee.perception.drift_detect:main',
        ],
    },
)
