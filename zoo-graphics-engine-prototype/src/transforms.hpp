#pragma once
#include "mesh.hpp"
void translate(Mesh&,double,double,double);
void scale(Mesh&,double,double,double);
void rotateZ(Mesh&,double);
void aabb(const Mesh&,Vec3&,Vec3&);
