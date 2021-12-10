%% Low frequency
im = imread('zy3.bmp');
im = im2double(rgb2gray(im));
wname='db20'
N=3
[L, Ch, Cv, Cd] = dwt2(im, wname,'mode', 'sp0');
m = mean(mean(L));
s = std(std(L));
T = s^2/(1*m);
nL = L.^2./m+T;
nim1 = idwt2(nL, Ch, Cv, Cd, wname);

%% High frequency
% N=1;
% [C,S] = wavedec2(nim,1,wname);
% [Ch,Cv,Cd] = detcoef2('all',C,S,1);
% A = appcoef2(C,S,wname,1)
% C=cat(3,Ch,Cv,Cd);
% % sigma=median(abs(C),3)/0.6745;
% % T = sigma*(2*log(N))^(1/2);
% % C=3*wthresh(C,'h',T);
% nim2 = idwt2(A,squeeze(C(:,:,1)),squeeze(C(:,:,2)),squeeze(C(:,:,3)),wname)
imshow(nim1)

%% HSI
k1 = pi    %1-2pi
k2 = pi     %0-2pi
mf = mean(mean(nim1)); 
I = nim1./(255+0.0157.*nim1.*(255-nim1));
S = (255-nim1)./(255+0.0157.*nim1.*(255-nim1));
H = (0.0157.*nim1.*(255-nim1))./(255+0.0157.*nim1.*(255-nim1));

I = 0.5/mf.*I;
H = k1.*H+k2;
V1 = S.*cos(H);
V2 = S.*sin(H);
R = I-0.204124*V1+0.612372*V2;
G = I-0.204124*V1+0.612372*V2;
B = I-0.204124*2*V1;
nim2=cat(3,R,G,B);
figure
imshow(nim2)

















