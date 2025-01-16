clc;clear;close all
load fisheriris.mat
species = categorical(species);
% [X,Y] = iris_dataset;
% 
NW =size(meas,1);

temp=randperm(NW);

% temp=1:nwhole;
train_ratio=0.8;
ntrain=round(NW*train_ratio);
ntest =NW-ntrain;

XTrain =meas(temp(1:ntrain),:);
YTrain=species(temp(1:ntrain),:);

XTest =meas(temp(ntrain+1:ntrain+ntest),:);
YTest =species(temp(ntrain+1:ntrain+ntest),:); 
classNames = unique(species)
classificationNeuralNetwork = fitcnet(...
    XTrain, ...
    YTrain, ...
    'LayerSizes', 100, ...
    'Activations', 'relu', ...
    'Lambda', 0, ...
    'IterationLimit', 1000, ...
    'Standardize', true, ...
    'ClassNames', classNames);

YPred = predict(classificationNeuralNetwork, XTest);
confusionchart(YTest,YPred)
[c_matrixp,Result,ReferenceResult]= confusion.getMatrix(grp2idx(YTest),grp2idx(YPred),0);
fprintf('Method \t Accuracy \t Sensitivity \t Specificity \t Precision \t F1 \t'),fprintf('\n')
fprintf('DL     \t %4.3f\t\t %4.3f\t\t\t %4.3f\t\t\t %4.3f\t\t %4.3f\t\t \n',...
    Result.Accuracy*100, Result.Sensitivity*100, Result.Specificity*100, Result.Precision*100,  Result.F1_score*100);

