cmake_minimum_required(VERSION 3.10)
project(engine_bench CXX)
set(CMAKE_CXX_STANDARD 17)
add_executable(engine_bench src/benchmark.cpp src/mesh.cpp src/transforms.cpp)
