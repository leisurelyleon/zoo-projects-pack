#include "transforms.hpp"
#include <cmath>
#include <limits>
void translate(Mesh& m,double dx,double dy,double dz){for(auto& v:m.vertices){v.x+=dx;v.y+=dy;v.z+=dz;}}
void scale(Mesh& m,double sx,double sy,double sz){for(auto& v:m.vertices){v.x*=sx;v.y*=sy;v.z*=sz;}}
void rotateZ(Mesh& m,double r){double c=std::cos(r),s=std::sin(r);for(auto& v:m.vertices){double nx=c*v.x-s*v.y;double ny=s*v.x+c*v.y;v.x=nx;v.y=ny;}}
void aabb(const Mesh& m,Vec3& mn,Vec3& mx){mn={1e300,1e300,1e300};mx={-1e300,-1e300,-1e300};for(const auto& v:m.vertices){if(v.x<mn.x)mn.x=v.x;if(v.y<mn.y)mn.y=v.y;if(v.z<mn.z)mn.z=v.z;if(v.x>mx.x)mx.x=v.x;if(v.y>mx.y)mx.y=v.y;if(v.z>mx.z)mx.z=v.z;}}
