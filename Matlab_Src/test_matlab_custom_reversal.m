classdef test_matlab_custom_reversal < matlab.unittest.TestCase
    
    methods(Test)        
        function unimplementedTest(testCase)
            testCase.verifyEqual(matlab_custom_reversal('abc'), 'cba');
        end
    end
    
end