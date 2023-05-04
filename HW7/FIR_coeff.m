N = 8
f_in = ones([1,N])./N;


t  = 1:.1:10;
t_in = 0:length(t)-1;
f0 = .5
A = 40;
x = A*(sin(2*pi*f0*t))

plot(t_in,x)

% salt and pepper noise
x1 = x;

snr = 15;
ns = fix((length(t)-1)*rand(1,snr))
ns_data = 80*(1-2*(rand(1,snr)> .5))
x1(ns)=ns_data;

hold on 
plot(t_in,x1)

% gaussian noise

snr = 40*.3
ns = snr*2*(rand(1,length(t_in))-.5)

x = x + ns;
plot(t_in,x2)

%% test cascade

t = 0:99;
x = zeros(1,100);

x(10)=80;

%% F64

f_64 = ones(1,64)/64;