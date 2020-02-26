% -------------------------------------------------------------------------
% Carter Mak
% Sounding Rocket Laboratory
% University of Colorado, Boulder
% February, 2020
% -------------------------------------------------------------------------
% Script to read and plot temperatures from all .dat files from DAQ v2.0
% -------------------------------------------------------------------------

%% Clear Out
clear;close all;clc;

fileList = dir('*.dat');

lgdCell = cell(length(fileList),1);

for i = 1:length(fileList)
	
	filename = fileList(i).name;
	
	data = readtable(filename);

	hold on
	plot(data.TIME,data.TEMP0)
	plot(data.TIME,data.TEMP1)
	plot(data.TIME,data.TEMP2)
	hold off
	
	fileLgd = {[filename,'_TEMP0'],[filename,'_TEMP1'],[filename,'_TEMP2']};
	
	lgdCell{i} = fileLgd;
	
end

lgdCell = horzcat(lgdCell{:});

legend(lgdCell,'location','best','interpreter','none')
xlabel('Time [ms]')
ylabel('Temperature [K]')
grid minor