grafica29.py: grilla.dat
	python grafica29.py
grilla.dat: datos29.x
	./datos29.x 
	./datos29.x > grilla.dat
datos29.x : ejercicio29.cpp
	c++ ejercicio29.cpp -o datos29.x