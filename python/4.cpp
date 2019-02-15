#include <iostream>
#include <math.h>
#include <time.h>
using namespace std;
int main(){
  double t=clock();
  double x1=1.3;
  double y1=2.3;
  double x0=0;
  double y0=1;
  double C[4];
  for(int i=0;i<4;i++){
    C[i] = 0.5*log(pow((x1-x0),2)+pow((y1-y0),2))+0.5*log(pow((x1-x0),2)+pow((y1+y0),2));
    x1+=0.1;
    y1+=0.1;
  }

  for (int i=0;i<=4000;i++){
    double x,y;
    double h_i=i/1000;
    x=-2+h_i;
    for (int j=0;j<=4000;j++){
      double h_j=j/1000;
      y=0+h_j;
      double phi=0.5*log(pow((x-x0),2)+pow((y-y0),2))+0.5*log(pow((x-x0),2)+pow((y+y0),2));
      double a=fabs(phi-C[0])<0.003;
      double a1=fabs(phi-C[1])<0.003;
      double a2=fabs(phi-C[2])<0.003;
      double a3=fabs(phi-C[3])<0.003;
    }
  }
  double r=(clock()-t);
  cout<<(r/CLOCKS_PER_SEC)<<endl;
  return 0;
}