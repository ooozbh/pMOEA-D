function EAGMOEAD(Global)
% <algorithm> <A-G>
% An External Archive Guided Multiobjective Evolutionary Algorithm Based on
% Decomposition for Combinatorial Optimization
% LGs --- 8 --- The number of learning generations

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group. You are free to use the PlatEMO for
% research purposes. All publications which use this platform or any code
% in the platform should acknowledge the use of "PlatEMO" and reference "Ye
% Tian, Ran Cheng, Xingyi Zhang, and Yaochu Jin, PlatEMO: A MATLAB Platform
% for Evolutionary Multi-Objective Optimization [Educational Forum], IEEE
% Computational Intelligence Magazine, 2017, 12(4): 73-87".
%--------------------------------------------------------------------------

    %% Parameter setting
    LGs = Global.ParameterSet(8);

    %% Generate the weight vectors
    [W,Global.N] = UniformPoint(Global.N,Global.M);
    T = ceil(Global.N/10);

    %% Detect the neighbours of each solution
    B = pdist2(W,W);
    [~,B] = sort(B,2);
    B = B(:,1:T);
    
    %% Generate random population
    Population = Global.Initialization();
    Archive    = Population;            % External archive
    s          = zeros(Global.N,LGs);   % Number of successful solutions in last several generations

    %% Optimization
    while Global.NotTermination(Archive)
        [MatingPool,offspringLoc] = MatingSelection(B,s);
        Offspring  = Global.Variation(Population(MatingPool),Global.N);
        Population = UpdatePopulation(Population,Offspring,offspringLoc,W,B);
        [Archive,sucessful] = UpdateArchive(Archive,Offspring);
        % Update the number of successful solutions generated by each
        % subproblem in the last LGs generations
        if any(sucessful)
            s(:,mod(Global.gen,LGs)+1) = hist(offspringLoc(sucessful),1:Global.N)';
        end
    end
end