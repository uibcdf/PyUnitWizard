from os import listdir as _listdir
from os.path import dirname as _dirname
from importlib import import_module as _import_module

base_package = __name__.replace('.base','')

list_api_forms=[filename.split('.')[0] for filename in _listdir(_dirname(__file__)) if filename.startswith('api')]

list_forms=[]
dict_api_forms={}

for api_form in list_api_forms:
    module_api_form=_import_module('.'+api_form, base_package)
    form_name=module_api_form.form_name
    list_forms.append(form_name)
    dict_api_forms[form_name]=module_api_form

dict_translator={}


for form_name in list_forms:

    dict_translator[form_name]={}

    for method in dict_api_forms[form_name].__dict__.keys():
        if method.startswith('to_'):
            out_form_name=method.replace('to_','').replace('_','.')
            dict_translator[form_name][out_form_name]= getattr(dict_api_forms[form_name], method)

del(api_form, list_api_forms, form_name, module_api_form, base_package)

