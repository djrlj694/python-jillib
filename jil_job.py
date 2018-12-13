#!/opt/cloudera/parcels/Anaconda/bin/python
# -*- coding: utf-8 -*-

'''
FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
jil_job.py

DECLARATION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
JILJob(self, insert_job, job_type, **kwargs)

DESCRIPTION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
This class models the JIL (Job Information Language) script
subcommand and attribute statements of Autosys jobs.

REFERENCES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1. https://docops.ca.com/ca-workload-automation-ae/11-4-2/en/scheduling/ae-scheduling/manage-your-jobs/common-optional-attributes
2. https://docops.ca.com/ca-workload-automation-ae/11-4-2/en/scheduling/ae-scheduling/manage-your-jobs/define-jobs
3. https://stackoverflow.com/questions/23862406/filter-items-in-a-python-dictionary-where-keys-contain-a-specific-string
'''


### Libraries ###

# 3rd-party

# Custom
from jil_statement import JILStatement


### Class Declaration ###

class JILJob(object):

    '''
    This class models the JIL (Job Information Language) script
    subcommand and attribute statements of Autosys jobs.

    Args:
        1. insert_job: str
        2. job_type: str
        3. kwargs: dict
    
    Returns:
        Instance of JILJob object
        
    '''

    # NOTE: Per Autosys Workload Automation AE documentation:
    # * All valid job definitions specify the job name ("insert_job") and the machine ("machine") on which the job runs;
    # * A job definition may include additional attributes, the optionality of which depends on the job type ("job_type"):
    def __init__(self, insert_job, job_type, **kwargs):

        job_types = [
            'BOX',
            'CMD',
            'FW'
        ]
        
        if not job_type in job_types:
            value_msg = 'The value of "job_type" must be one of the following'
            job_types_str = (', ').join(job_types)
            raise ValueError('{}: {}'.format(value_msg, job_types_str))

        # Required
        self.insert_job = JILStatement('insert_job', value=insert_job)
        self.job_type = JILStatement('job_type', value=job_type)
        
        # Optional
        self.alarm_if_fail = JILStatement('alarm_if_fail', **kwargs)
        self.owner = JILStatement('owner', **kwargs)
        self.permission = JILStatement('permission', **kwargs)
        self.max_run_alarm = JILStatement('max_run_alarm', **kwargs)
        self.send_notification = JILStatement('send_notification', **kwargs)

    def __str__(self):
        
        # Lists
        required = [
            self.insert_job,
            self.job_type
        ]
        optional = [
            self.alarm_if_fail,
            self.owner,
            self.permission,
            self.max_run_alarm,
            self.send_notification
        ]
        
        # Strings
        required_str = '\n'.join(required)
        optional_str = '\n'.join([x for x in optional if len(x) > 0])
        
        return required_str + '\n' + optional_str
        

if __name__ == '__main__':
    #pass
    
    print('')
    print('UNIT TESTS: PASS')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
    
    print('TEST P1:')
    pass1 = JILJob(insert_job="pass1_job", job_type="BOX", owner="user", permission="yes", send_notification="y")
    print(pass1)
    print('')
    #assert(pass1.max_run_alarm == None)

    print('TEST P2:')
    pass2 = JILJob(insert_job="pass2_job", job_type="CMD", owner="user", permission="yes", send_notification="y")
    print(pass2)
    print('')
    #assert(pass2.max_run_alarm == None)

    print('TEST P3:')
    pass3 = JILJob(insert_job="pass3_job", job_type="FW", owner="user", permission="yes", send_notification="y")
    print(pass3)
    print('')
    #assert(pass3.max_run_alarm == None)

    print('')
    print('UNIT TESTS: FAIL')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')

    print('TEST F1:')
    fail1 = JILJob(insert_job="fail1_job", job_type="test job", owner="user", permission="yes", send_notification="y")
    print(fail1)
    #assert(fail1.max_run_alarm == None)
