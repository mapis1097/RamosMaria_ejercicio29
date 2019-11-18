#include <iostream>
//se llama el metodo
double ecuacion (double s, double d, float *actual, float *anterior, double Ctiempo, double Cespacio, double deltaT, double deltaX);

//ejecuta el codigo
int main (){
    //variables
    double phi_1 = 0.0;
    double phi_2 = 0.0;
    double deltaX = 2/30;
    double deltaT = 0.01;
    double tiempo = 1;
    double D = 1;
    double s = 1;
    double inicial = 0;
    double CTiempo = tiempo / deltaT;
    double CEspacio = 30;
    float anterior[30];
    float actual[30];
    ecuacion(s, D, actual, anterior, CTiempo, CEspacio, deltaT, deltaX);
    
 return 0;
}




//metodos
double ecuacion (double s, double d, float *actual, float *anterior, double Ctiempo, double Cespacio, double deltaT, double deltaX){
    for (int i = 0; i < Ctiempo; i ++){
        std::cout << "t: "<<deltaT*i <<"\n";
        for(int k = 0; k < Cespacio; k++){
            std::cout << *(anterior+k) << "\t"; 
        }
        std::cout<<std::endl;
        for (int j = 0; j < Cespacio; j ++)
        {
            if (i == 0){
                *(actual + j) = 0;
            }
            else if (j == 0 || j == Cespacio-1){
                *(actual + j) = 0;
            }
            else{
                *(actual +j ) = *(anterior +j) + ((d*deltaT)/(deltaX*deltaX))*(*(anterior + (j+1))- (2* (*(anterior + j)) + (*(anterior - j)))) + (deltaT*s);         
            }
            
        }
        for ( int l = 0; l < Cespacio; l++){
            *(anterior + l) = *(actual + l);
        }
    }
}
    
