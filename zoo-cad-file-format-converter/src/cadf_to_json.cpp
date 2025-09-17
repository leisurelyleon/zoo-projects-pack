#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>
int main(int argc,char** argv){
    if(argc<2){std::cerr<<"usage: cadf_to_json <file>\n";return 1;}
    std::ifstream in(argv[1]); if(!in){std::cerr<<"open fail\n";return 1;}
    std::string header; std::getline(in,header); if(header!="CADF v1"){std::cerr<<"bad header\n";return 1;}
    std::vector<std::array<double,3>> V; std::vector<std::array<int,3>> F; std::string tag;
    while(in>>tag){ if(tag=="VERTEX"){double x,y,z;in>>x>>y>>z;V.push_back({x,y,z});} else if(tag=="FACE"){int i,j,k;in>>i>>j>>k;F.push_back({i,j,k});} }
    std::cout<<"{\n  \"vertices\":["; for(size_t i=0;i<V.size();++i){auto v=V[i]; std::cout<<"["<<v[0]<<","<<v[1]<<","<<v[2]<<"]"<<(i+1<V.size()?",":"");}
    std::cout<<"],\n  \"faces\":["; for(size_t i=0;i<F.size();++i){auto f=F[i]; std::cout<<"["<<f[0]<<","<<f[1]<<","<<f[2]<<"]"<<(i+1<F.size()?",":"");}
    std::cout<<"]\n}\n"; return 0;
}
