# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;std_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lcsm;-lcalib_odom".split(';') if "-lcsm;-lcalib_odom" != "" else []
PROJECT_NAME = "calib_odom"
PROJECT_SPACE_DIR = "/home/jkzhang/lidar_slam/github_repo/lidar_slam/HW2/odom_ws/install"
PROJECT_VERSION = "0.0.0"
