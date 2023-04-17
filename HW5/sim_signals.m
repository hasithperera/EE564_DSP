
t = []
b = []
c = []
a = []
i = 0
j = 0
for i=0:15
    for j=0:15
        a = [a,0:15];
        b = [b,i*ones(1,16)];
        c = [c,j*ones(1,16)];
    end
end

plot(a)
hold on
plot(b)
plot(c)