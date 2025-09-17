#pragma once
#include <vector>
#include <array>
struct Vec3{double x,y,z;};
struct Mesh{std::vector<Vec3> vertices; std::vector<std::array<int,3>> faces;};
