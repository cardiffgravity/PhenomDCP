

#
def generate_model_params(theta,eta,a1):

	'''
	Hola, soy un codigo escribido por "4b_document_fits.py". 
	~londonl@mit.edu/pilondon2@gmail.com 2020
	'''  

	# Import usefuls
	from numpy import cos

	# Preliminaries
	u = cos(theta)
	u2 = u*u
	u3 = u2*u
	u4 = u3*u
	eta2 = eta*eta
	eta3 = eta2*eta

	# mu1
	mu1 = -4.83550509e-01*(eta) + -5.70767870e-02*(a1) + 3.06285939e-02 + -3.87482129e-01*(u*u) + 2.45032352e+00*(eta*eta) + 8.94673544e-01*(eta*a1) + -1.52069695e-02*(u*eta*eta) + 7.08472166e-03*(u*eta*a1) + -3.70684346e+00*(eta2*eta) + -4.53303668e+00*(eta2*a1) + 5.04260174e-01*(u2*a1) + 7.43939662e+00*(u2*eta) + 2.67483437e-01*(u2*u) + -9.78802972e+00*(u2*eta*a1) + -4.49502247e+01*(u2*eta*eta) + 3.56490176e-02*(u3*u) + -5.22011346e+00*(u3*eta) + -3.48255282e-01*(u3*a1) + 7.24076668e+00*(eta3*a1) + 5.99138876e+01*(u2*eta2*a1) + 8.58106451e+01*(u2*eta2*eta) + 6.84404949e+00*(u3*eta*a1) + 3.11724703e+01*(u3*eta*eta) + -2.71419223e-02*(u2*u2*a1) + -5.78972876e+01*(u3*eta2*eta) + -4.03992866e+01*(u3*eta2*a1) + -4.95613713e+00*(u2*u2*eta*eta) + -1.15536449e+02*(u2*eta3*a1) + 7.38752770e+01*(u3*eta3*a1) + 1.81139915e+01*(u2*u2*eta2*eta) + 5.01826219e+00*(u2*u2*eta2*a1) + -1.92528671e+01*(u2*u2*eta3*a1)

	# mu2
	mu2 = -9.44875395e-02  +  2.38584951e-01 * (  2.51910055e+00*(u) + -1.97805683e+00*(u*u) + 4.38516765e-01*(u2*u) + 1.93992753e+00*(u2*a1) + -6.79547751e+01*(u*eta) + 2.06095905e+02*(u*eta*eta) + 4.20290904e+00*(u*eta*a1) + 6.57018609e+01*(eta) + -3.55729055e+02*(eta*eta) + 3.56157679e+02*(eta2*a1) + -6.10531555e+01*(eta*a1) + 4.08931887e-02 ) / ( 1.0 +  -2.53543647e+00*(u*u) + 6.22709511e-01*(u2*u) + -1.23669064e+01*(u2*eta) + 5.08876012e+00*(u2*a1) + -4.58250376e+00*(u*eta) + -4.73056676e-01*(u*a1) + 3.05218510e+01*(eta) + -5.67501010e+01*(eta2*a1) + -3.71044979e+00*(a1) )

	# mu3
	mu3 = 5.04921268e-02*(u) + 3.13247716e-01*(eta) + 6.45195951e-02*(a1) + -1.55054481e-02 + -4.93855705e-02*(u*a1) + 9.86989737e-02*(u*u) + -8.70183227e-01*(u*eta) + -1.75200467e+00*(eta*eta) + -1.18126698e+00*(eta*a1) + 4.99221250e+00*(u*eta*eta) + 7.42367124e-01*(u*eta*a1) + 2.98614792e+00*(eta2*eta) + 6.60469122e+00*(eta2*a1) + -3.85453818e-01*(u2*a1) + -1.39720642e+00*(u2*eta) + -7.03854714e-02*(u2*u) + -4.20936304e+00*(u*eta2*a1) + -9.27349236e+00*(u*eta2*eta) + 6.19188974e+00*(u2*eta*a1) + 6.07699563e+00*(u2*eta*eta) + -4.95915349e-02*(u3*u) + 1.14990338e+00*(u3*eta) + 2.17032815e-02*(u3*a1) + -1.16458975e+01*(eta3*a1) + -3.16325912e+01*(u2*eta2*a1) + -8.16295227e+00*(u2*eta2*eta) + -8.38007739e-02*(u3*eta*a1) + -6.33863766e+00*(u3*eta*eta) + 8.14796921e+00*(u*eta3*a1) + 4.35254244e-01*(u2*u2*eta) + 3.27516801e-01*(u2*u2*a1) + 1.16088210e+01*(u3*eta2*eta) + -4.88761726e+00*(u2*u2*eta*a1) + 5.20316551e+01*(u2*eta3*a1) + -3.93834811e+00*(u2*u2*eta2*eta) + 2.32212537e+01*(u2*u2*eta2*a1) + -3.52675541e+01*(u2*u2*eta3*a1)

	# mu4
	mu4 = -8.22472458e-04  +  1.36103742e-02 * (  6.14636541e-01*(u*u) + -4.38601237e+00*(u2*eta) + -6.37744636e+01*(u*eta) + 1.46976817e+02*(u*eta*eta) + 3.95988211e+01*(u*eta*a1) + -3.75291708e+00*(u*a1) + 3.30408962e+01*(eta) + -2.03021695e+02*(eta*eta) + 4.89740829e+01*(eta2*a1) + 1.98041963e+00 ) / ( 1.0 +  -6.43048586e+00*(u) + 3.80068886e+00*(u*u) + -3.99971307e+01*(u2*eta) + 5.92533416e+00*(u2*a1) + -2.61978372e+01*(u*eta) + 1.94289718e+02*(u*eta*eta) + 2.19803292e+00*(u*eta*a1) + 9.49196126e+01*(eta) + -2.51881508e+02*(eta*eta) + 1.58318387e+02*(eta2*a1) + -7.35549996e+01*(eta*a1) )

	# nu4
	nu4 = 5.51719008e+00*(u) + 2.18678678e+01*(eta) + 2.28629515e+00*(a1) + -6.80618656e-01 + -7.70491333e+00*(u*a1) + -1.15873321e+02*(u*eta) + -1.63512250e+00*(u*u) + -1.67614508e+02*(eta*eta) + -5.86237731e+01*(eta*a1) + 7.20411191e+02*(u*eta*eta) + 1.67813617e+02*(u*eta*a1) + 3.71117004e+02*(eta2*eta) + 4.32889004e+02*(eta2*a1) + 6.19614947e+00*(u2*eta) + -5.54678806e+00*(u2*u) + -1.04041396e+03*(u*eta2*a1) + -1.38468019e+03*(u*eta2*eta) + 4.75977227e+01*(u2*eta*a1) + 6.65553810e+01*(u2*eta*eta) + 1.85153536e+00*(u3*u) + 1.17222041e+02*(u3*eta) + 9.45887028e+00*(u3*a1) + -9.45713925e+02*(eta3*a1) + -4.90990830e+02*(u2*eta2*a1) + -2.53810687e+02*(u2*eta2*eta) + -2.06417940e+02*(u3*eta*a1) + -7.39291639e+02*(u3*eta*eta) + 1.96846191e+03*(u*eta3*a1) + -1.37542570e+01*(u2*u2*eta) + -2.62655571e+00*(u2*u2*a1) + 1.43485347e+03*(u3*eta2*eta) + 1.31054319e+03*(u3*eta2*a1) + 1.39143382e+01*(u2*u2*eta*a1) + 1.20398858e+03*(u2*eta3*a1) + -2.54546457e+03*(u3*eta3*a1) + 1.03772840e+02*(u2*u2*eta2*eta) + 4.76340540e+01*(u2*u2*eta2*a1) + -2.57784937e+02*(u2*u2*eta3*a1)

	# nu5
	nu5 = 2.88393711e-03  +  1.15379354e-02 * (  -1.64640469e+01*(u2*u2*a1) + -4.69178497e+02*(u3*eta*eta) + 1.40733777e+03*(u*eta3*a1) + -1.41383849e+02*(u*eta*a1) + 1.60965212e+01*(u*a1) + -7.51678976e+02*(eta3*a1) + 1.36828872e+01*(a1) + -1.75098134e+00 ) / ( 1.0 +  2.33090141e+01*(u) + 4.05445777e+01*(u2*u2*eta) + -8.79493193e+00*(u2*u2*a1) + 3.24763161e+01*(u2*eta*a1) + -2.00832844e+02*(u*eta) + 4.06600440e+02*(u*eta*eta) + 2.99037190e+02*(u*eta2*a1) + -1.78821180e+01*(u*a1) + 5.42060918e+02*(eta*eta) + -1.82130558e+03*(eta2*eta) + -5.42813762e+02*(eta3*a1) + 3.76473035e+00*(a1) )

	# nu6
	nu6 = 1.65194847e-01*(u) + 1.96529671e-01*(eta) + 8.89562681e-03 + -2.45536591e-01*(u*a1) + -3.39904493e+00*(u*eta) + -2.52412744e+00*(eta*eta) + -4.99260420e-01*(eta*a1) + 2.09636308e+01*(u*eta*eta) + 5.26414740e+00*(u*eta*a1) + 6.49768589e+00*(eta2*eta) + 5.40351281e+00*(eta2*a1) + 6.64017528e-02*(u2*a1) + -8.89643941e-01*(u2*eta) + -2.23573673e-01*(u2*u) + -3.27649022e+01*(u*eta2*a1) + -4.00643292e+01*(u*eta2*eta) + 3.84032195e-01*(u2*eta*a1) + 8.84025848e+00*(u2*eta*eta) + -1.37214125e+01*(eta3*a1) + -4.46926593e-02*(u3*u) + 4.46795244e+00*(u3*eta) + 4.06052368e-01*(u3*a1) + -9.63719114e+00*(u2*eta2*a1) + -2.09699403e+01*(u2*eta2*eta) + -8.35155054e+00*(u3*eta*a1) + -2.74679213e+01*(u3*eta*eta) + 6.24549604e+01*(u*eta3*a1) + 1.83589325e+00*(u2*u2*eta) + 5.26150227e+01*(u3*eta2*eta) + 5.20894001e+01*(u3*eta2*a1) + -1.46870655e+01*(u2*u2*eta*eta) + -1.67357011e+00*(u2*u2*eta*a1) + 2.82033377e+01*(u2*eta3*a1) + -1.00437247e+02*(u3*eta3*a1) + 3.21828994e+01*(u2*u2*eta2*eta) + 1.69468820e+01*(u2*u2*eta2*a1) + -4.09924669e+01*(u2*u2*eta3*a1)

	#
	return mu1,mu2,mu3,mu4,nu4,nu5,nu6
