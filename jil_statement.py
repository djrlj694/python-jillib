#!/opt/cloudera/parcels/Anaconda/bin/python
# -*- coding: utf-8 -*-

'''
FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
jil_statement.py

DECLARATION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
JILStatement(self, key, **kwargs)

DESCRIPTION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
This class generates strings that conform to the syntax of JIL (Job
Information Language) script subcommand and arguments statements,
both of which can be expressed as colon-separated key/value pairs
(i.e., <KEY>:<VALUE>).

REFERENCES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1. https://docops.ca.com/ca-workload-automation-ae/11-4-2/en/scheduling/ae-scheduling/manage-jil/jil-syntax-rules
'''


### Class Declaration ###

class JILStatement(str):

    '''
    This class generates strings that conform to the syntax of JIL (Job
    Information Language) script subcommand and arguments statements,
    both of which can be expressed as colon-separated key/value pairs
    (i.e., <KEY>:<VALUE>).

    Args:
        1. key: str
        2. **kwargs: dict
    
    Returns:
        Instance of JILStatement object 

    '''

    # This constructor follows the following JIL syntax rules:
    # 1: Each subcommand uses the following form:
    #    sub_command:object_name
    # 2: The attribute statements have the following form:
    #    attribute_keyword:value
    def __new__(self, key, **kwargs):
        
        if not isinstance(key, str):
            raise TypeError('Argument "key" must be of type "str".')
            
        if len(kwargs) == 0:
            raise ValueError('At least one keyword argument must exist.')
        
        value = kwargs.get('value', None) or kwargs.get(key, None)
        
        return '' if not value else key + ': ' + str(value)
            
            
if __name__ == '__main__':
    #pass
    
    print('')
    print('UNIT TESTS: PASS')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
    
    insert_job = 'job1_name'
    pass_dict = {'test_key1': 'test_value1', 'test_key2': 'test_value2'}
    
    print(type(pass_dict))
    
    print('TEST P1:')
    pass1 = JILStatement('insert_job', value=insert_job)
    print(pass1)
    print('')

    print('TEST P2:')
    pass2 = JILStatement('test_key1', **pass_dict)
    print(pass2)
    print('')

    print('TEST P3:')
    pass3 = JILStatement('insert_job', key1=insert_job, key2='foo')
    print(pass3)

    print('')
    print('UNIT TESTS: FAIL')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')

    print('TEST F1:')
    fail1 = JILStatement('insert_job')
    print(fail1)
    
    print('TEST F2:')
    fail1 = JILStatement('insert_job', 'foo')
    print(fail1)

