#!/opt/cloudera/parcels/Anaconda/bin/python
# -*- coding: utf-8 -*-

'''
FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
jil_box_job.py

DECLARATION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
JILBoxJob(self, insert_job, **kwargs)

DESCRIPTION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
This subclass of "JILJob" models the JIL (Job Information Language) script
subcommand and attribute statements of Autosys "Box" jobs.

REFERENCES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1. https://docops.ca.com/ca-workload-automation-ae/11-4-2/en/scheduling/ae-scheduling/box-jobs-overview/define-a-box-job
'''


### Libraries ###

# 3rd-party

# Custom
from jil_job import JILJob


### Class Declaration ###

class JILBoxJob(JILJob):

    '''
    This subclass of "JILJob" models the JIL (Job Information Language) script
    subcommand and attribute statements of Autosys "Box" jobs.

    Args:
        1. insert_job: str
        2. kwargs: dict
    
    Returns:
        Instance of JILBoxJob object

    '''
    
    def __init__(self, insert_job, **kwargs):
        
        super(JILBoxJob, self).__init__(insert_job, 'BOX', **kwargs)



if __name__ == '__main__':
    #pass
    
    print('')
    print('UNIT TESTS: PASS')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
    
    print('TEST P1:')
    job1 = JILBoxJob(insert_job="test_job1", owner="user", permission="yes", max_run_alarm=15, alarm_if_fail="y", send_notification="y")
    print(job1)
    #assert(job1.max_run_alarm == None)

    print('')
    print('UNIT TESTS: FAIL')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
