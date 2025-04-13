% W12AIR-SM0721P # P # Artificial Neural Networks - Projekt
% Autors: P.Ozga & P.Pramod 
% dateset by andrewmchen and mateiz from github link: https://github.com/mlflow/mlflow-example/blob/master/wine-quality.csv
% Toolbox: Statistics and Machine Learning Toolbox
% How to create ClassificationNeuralNetwork https://www.mathworks.com/help/stats/classificationneuralnetwork.html
close all;

opts = detectImportOptions('wine_quality_dataset.csv'); % import file
opts.VariableNamingRule = 'preserve';                   % save name of columns
data = readtable('wine_quality_dataset.csv', opts);     % read table
head(data);                                             % Check first data
class(data.quality)                                     % Check type of class
if ~isa(data.quality, 'double')                         % Check type 'double'
        data.quality = double(data.quality);            % Convert quality2double
end

% i need good predictor - alcohol
data.quality = categorical(data.quality ,[4,5,6,7,8,9]);      % classifitate on class

rng("default")                                          % about 
c = cvpartition(data.quality,"HoldOut",0.20);           % create object(data, two sets, witch 20% & 80% from data
trainingIndices = training(c);                          % Logical indices for the training set
testIndices = test(c);                                  % Logical indices for the test set 
%creditTrain = data(trainingIndices,:);                  % Select training samples
%creditTest = data(testIndices,:);                       % Select test samples
featureColumns = setdiff(data.Properties.VariableNames, {'quality'});

XTrain = data{trainingIndices, featureColumns}; % input (features)
YTrain = data.quality(trainingIndices);         % class laybel
XTest = data{testIndices, featureColumns};      % text data
YTest = data.quality(testIndices);              % text label

%Mdl = fitcnet(creditTrain,"quality");Mdl
Mdl = fitcnet(XTrain,YTrain);                   % Trening set

YTestPred = predict(Mdl, XTest);                % prediction laybel
testAccuracy = 1 - loss(Mdl, XTest, YTest, "LossFun", "classiferror"); 
%testAccuracy = 1-loss(Mdl,creditTest,"quality","LossFun","classiferror");

confusionchart(YTest, YTestPred);
%confusionchart(creditTest.quality,predict(Mdl,creditTest))

head(data); tail(data); % Check data
