import json

f1 = json.loads(open('init_ddi.json', 'r').read())
f2 = json.loads(open('subset_info.json', 'r').read())

def msgt(m):
    dashes(); print(m); dashes();

def dashes():
    print ('-' * 40)

def compare_lists(f1_var, f2_var):

    f1_keys = f1_var.keys()
    f2_keys = f2_var.keys()

    not_f2 = ([x for x in f1_keys if x not in f2_keys])

    not_f1 = ([x for x in f2_keys if x not in f1_keys])

    if not_f2 != not_f1:
        print (not_f2)
        print (not_f1)

def compare_variables():

    f1_vars = f1['variables']
    f2_vars = f2['variables']

    for varname in f1_vars.keys():
        msgt('compare: %s' % varname)
        compare_lists(f1_vars[varname], f2_vars[varname])

def get_valid_vars(ddi_data):

    valid = []
    for var_key, var_info in ddi_data.get('variables', {}).items():
        if var_info['valid'] !=0:
            valid.append(var_key)
    print ('valid: ', valid)

if __name__ == '__main__':
    #compare_variables()
    get_valid_vars(f2)
