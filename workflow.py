from kfp import dsl
from mlrun.platforms import auto_mount
import os
import sys
import mlrun

funcs = {}

# init func-1tions is used to configure func-1tion resources and local settings
def init_functions(functions: dict, project=None, secrets=None):
    for f in functions.values():
        f.apply(auto_mount())

@dsl.pipeline(
    name="NYC Taxi Demo",
    description="Convert ML script to MLRun"
)

def kfpipeline():

    # run the ingestion func-1tion with the new image and params
    step_1 = funcs['func-1'].as_step(params = {"x" : 0},outputs = ['return'])
    
    step_2 = funcs['func-1'].as_step(params = {"x" : step_1.outputs['return']},outputs = ['return'])
    
    step_3 = funcs['func-1'].as_step(params = {"x" : step_2.outputs['return']},outputs = ['return'])
    
    step_4 = funcs['func-1'].as_step(params = {"x" : step_3.outputs['return']},outputs = ['return'])
    
    step_5 = funcs['func-1'].as_step(params = {"x" : step_4.outputs['return']},outputs = ['return'])
    
    step_6 = funcs['func-1'].as_step(params = {"x" : step_5.outputs['return']},outputs = ['return'])
    
    step_7 = funcs['func-1'].as_step(params = {"x" : step_6.outputs['return']},outputs = ['return'])
    
    step_8 = funcs['func-1'].as_step(params = {"x" : step_7.outputs['return']},outputs = ['return'])
    
    step_1_1 = funcs['func-1'].as_step(params = {"x" : 0},outputs = ['return'])
    
    step_1_2 = funcs['func-1'].as_step(params = {"x" : step_1_1.outputs['return']},outputs = ['return'])
    
    step_1_3 = funcs['func-1'].as_step(params = {"x" : step_1_2.outputs['return']},outputs = ['return'])
    
    step_1_4 = funcs['func-1'].as_step(params = {"x" : step_1_3.outputs['return']},outputs = ['return'])

    step_1_5 = funcs['func-1'].as_step(params = {"x" : step_1_4.outputs['return']},outputs = ['return'])
    
    step_1_6 = funcs['func-1'].as_step(params = {"x" : step_1_5.outputs['return']},outputs = ['return'])
    
    step_1_7 = funcs['func-1'].as_step(params = {"x" : step_1_6.outputs['return']},outputs = ['return'])
    
    step_1_8 = funcs['func-1'].as_step(params = {"x" : step_1_7.outputs['return']},outputs = ['return'])
    
    step_2_1 = funcs['func-1'].as_step(params = {"x" : 0},outputs = ['return'])

    step_2_2 = funcs['func-1'].as_step(params = {"x" : step_2_1.outputs['return']},outputs = ['return'])

    step_2_3 = funcs['func-1'].as_step(params = {"x" : step_2_2.outputs['return']},outputs = ['return'])

    step_2_4 = funcs['func-1'].as_step(params = {"x" : step_2_3.outputs['return']},outputs = ['return'])

    step_2_5 = funcs['func-1'].as_step(params = {"x" : step_2_4.outputs['return']},outputs = ['return'])

    step_2_6 = funcs['func-1'].as_step(params = {"x" : step_2_5.outputs['return']},outputs = ['return'])

    step_2_7 = funcs['func-1'].as_step(params = {"x" : step_2_6.outputs['return']},outputs = ['return'])

    step_2_8 = funcs['func-1'].as_step(params = {"x" : step_2_7.outputs['return']},outputs = ['return'])

    step_3_1 = funcs['func-1'].as_step(params = {"x" : 0},outputs = ['return'])

    step_3_2 = funcs['func-1'].as_step(params = {"x" : step_3_1.outputs['return']},outputs = ['return'])

    step_3_3 = funcs['func-1'].as_step(params = {"x" : step_3_2.outputs['return']},outputs = ['return'])

    step_3_4 = funcs['func-1'].as_step(params = {"x" : step_3_3.outputs['return']},outputs = ['return'])

    step_3_5 = funcs['func-1'].as_step(params = {"x" : step_3_4.outputs['return']},outputs = ['return'])

    step_3_6 = funcs['func-1'].as_step(params = {"x" : step_3_5.outputs['return']},outputs = ['return'])

    step_3_7 = funcs['func-1'].as_step(params = {"x" : step_3_6.outputs['return']},outputs = ['return'])

    step_3_8 = funcs['func-1'].as_step(params = {"x" : step_3_7.outputs['return']},outputs = ['return'])

    step_4_1 = funcs['func-1'].as_step(params = {"x" : 0},outputs = ['return'])

    step_4_2 = funcs['func-1'].as_step(params = {"x" : step_4_1.outputs['return']},outputs = ['return'])

    step_4_3 = funcs['func-1'].as_step(params = {"x" : step_4_2.outputs['return']},outputs = ['return'])

    step_4_4 = funcs['func-1'].as_step(params = {"x" : step_4_3.outputs['return']},outputs = ['return'])

    step_4_5 = funcs['func-1'].as_step(params = {"x" : step_4_4.outputs['return']},outputs = ['return'])

    step_4_6 = funcs['func-1'].as_step(params = {"x" : step_4_5.outputs['return']},outputs = ['return'])

    step_4_7 = funcs['func-1'].as_step(params = {"x" : step_4_6.outputs['return']},outputs = ['return'])

    step_4_8 = funcs['func-1'].as_step(params = {"x" : step_4_7.outputs['return']},outputs = ['return'])
   
