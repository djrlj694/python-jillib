#!/opt/cloudera/parcels/Anaconda/bin/python
# -*- coding: utf-8 -*-

'''
FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
jil_fw_job.py

DECLARATION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
JILFWJob(self, insert_job, **kwargs)

DESCRIPTION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
This subclass of "JILJob" models the JIL (Job Information Language) script
subcommand and attribute statements of Autosys "Command" jobs.

REFERENCES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1. https://docops.ca.com/ca-workload-automation-ae/11-4-2/en/scheduling/ae-scheduling/command-jobs-overview/define-a-command-job
'''


### Libraries ###

# 3rd-party

# Custom
from jil_job import JILJob
from jil_statement import JILStatement


### Class Declaration ###

class JILCmdJob(JILJob):
    
    '''
    This subclass of "JILJob" models the JIL (Job Information Language) script
    subcommand and attribute statements of Autosys "Command" jobs.
    
    Args:
        1. insert_job: str
        2. machine: str
        3. condition: str
        4. kwrgs: dict
    
    Returns:
        Instance of JILCmdJob object 

    '''
    
    def __init__(self, insert_job, machine, command, **kwargs):
        
        super(JILCmdJob, self).__init__(insert_job, 'CMD', **kwargs)
        
        # Required
        self.machine = JILStatement('machine', value=machine)
        self.command = JILStatement('command', value=command)

        # Optional
        self.box_name = JILStatement('box_name', **kwargs)
        self.condition = JILStatement('condition', **kwargs)
        self.std_err_file = JILStatement('std_err_file', **kwargs)
        
    def __str__(self):
        
        # Lists
        required = [
            self.machine,
            self.command
        ]
        optional = [
            self.box_name,
            self.condition,
            self.std_err_file
        ]
        
        # Strings
        super_str = super(JILCmdJob, self).__str__()
        required_str = '\n'.join(required)
        optional_str = '\n'.join([x for x in optional if len(x) > 0])
        
        return '\n'.join([super_str, required_str, optional_str])
        

if __name__ == '__main__':
    #pass
    
    print('')
    print('UNIT TESTS: PASS')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
    
    print('TEST P1:')
    job1 = JILCmdJob(insert_job="test_job1", machine = "my_computer", command="my_cmd", owner="user", permission="yes", max_run_alarm=15, alarm_if_fail="y", send_notification="y", box_name="my_box", watch_file_min_size=7, watch_interval=3)
    print(job1)
    #assert(job1.max_run_alarm == None)

    print('')
    print('UNIT TESTS: FAIL')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
