## Author : Hasith Perera
## DSP HW 2 Q4
## Black body radiation 


k_b= 1.38e-23;
h = 6.6e-34;
j = 1
Temp = 0;
lamda = 0;
##for T=2:50:1e4
T =4000;
c=3e8;

black_body = @(T,v) (2*h.*v.^3)./(c^2*(exp((h.*v)/(k_b*T))-1));

  ## f = @(x) x.^2-4.*x - 5 ## test function for the algorithm
  f = @(v) ((v*h)/(k_b*T))*(1/(1-exp(-1*(h*v/(k_b*T)))))-3;

  dx = .1;
  err = 1e-4;

  root_n1 = 10000;
  root_n = root_n1+dx;
  k = 1;
  while abs(root_n1-root_n)>err

    df = (f(root_n1)-f(root_n))/(root_n1-root_n);
    root_n = root_n1;
    root_n1 = root_n-f(root_n)/df;
    k = k + 1;
  end

 fprintf("Peak f:%e\n",root_n1) 
 fprintf("Peak lamda:%3.2e\n",2.9e8/root_n1)
  
ff = 1e13:.1e14:1e15;
plot(ff,black_body(T,ff),'Linewidth',2)
hold on
plot(root_n1,black_body(T,root_n1),'o','Linewidth',2)
xlabel('freq (Hz)')

##  Temp(j) = T;
##  lamda(j) = 2.9e8/root_n1;
##  j = j + 1
##end
##plot(Temp,1./lamda,'o')
##xlabel('T (K)');
##ylabel('1/lamda (1/m)');
