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
subcommand and attribute statements of Autosys "File Watcher" jobs.

REFERENCES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1. https://docops.ca.com/ca-workload-automation-ae/11-4-2/en/scheduling/ae-scheduling/file-watcher-jobs-overview/define-a-file-watcher-job
'''


### Libraries ###

# 3rd-party

# Custom
from jil_job import JILJob
from jil_statement import JILStatement


### Class Declaration ###

class JILFWJob(JILJob):

    '''
    This subclass of "JILJob" models the JIL (Job Information Language) script
    subcommand and attribute statements of Autosys "File Watcher" jobs.

    Args:
        1. insert_job: str
        2. machine: str
        3. watch_file: str
        4. kwargs: dict
    
    Returns:
        Instance of JILFWJob object 

    '''
    
    def __init__(self, insert_job, machine, watch_file, **kwargs):
        
        super(JILFWJob, self).__init__(insert_job, 'FW', **kwargs)
        
        # Required
        self.machine = JILStatement('machine', value=machine)
        self.watch_file = JILStatement('watch_file', value=watch_file)
        
        # Optional
        self.box_name = JILStatement('box_name', **kwargs)
        self.watch_file_min_size = JILStatement('watch_file_min_size', **kwargs)
        self.watch_interval = JILStatement('watch_interval', **kwargs)
        
    def __str__(self):
        
        # Lists
        required = [
            self.machine,
            self.watch_file
        ]
        optional = [
            self.box_name,
            self.watch_file_min_size,
            self.watch_interval
        ]
        
        # Strings
        super_str = super(JILFWJob, self).__str__()
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
    job1 = JILFWJob(insert_job="test_job1", machine="my_computer", watch_file="TBD", owner="user", permission="yes", max_run_alarm=15, alarm_if_fail="y", send_notification="y", box_name="my_box", watch_file_min_size=7, watch_interval=3)
    print(job1)
    #assert(job1.max_run_alarm == None)

    print('')
    print('UNIT TESTS: FAIL')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
