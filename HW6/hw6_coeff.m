
N = 16
m = 0:N-1;
w = exp(-2*pi*j*m /N);

t = linspace(0,5,16);

f = 2;
y = 128*(sin(2*pi*f.*t));

y_fft = fft(y);
% plot(t,y,'o:')
plot(abs(y_fft),'o')

w_r = real(w)
w_c = imag(w)

%%
