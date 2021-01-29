from importlib import import_module as _import_module
from importlib.util import find_spec as _find_spec

list_forms = ['simtk.unit', 'Pint', 'unyt']
forms_library = {'simtk.unit':'simtk.unit', 'Pint':'pint', 'unyt':'unyt'}
forms_exists = {ii: (_find_spec(jj) is not None) for ii,jj in forms_library.items()}
forms_apis_modules = {'simtk.unit':'api_simtk_unit', 'Pint':'api_pint', 'unyt':'api_unyt'}
forms_apis={}

base_package = __name__.replace('.base','')

for form in list_forms:
    if forms_exists[form]:
        forms_apis[form]=_import_module('.'+forms_apis_modules[form], base_package)

dict_is_form={}
dict_translate={}
dict_make_quantity={}
dict_make_unit={}
dict_get_value={}
dict_get_unit={}
dict_get_unit_name={}
dict_convert={}

for form, api in forms_apis.items():

    dict_is_form.update(api.is_form)

    dict_translate[form]={}
    for method in api.__dict__.keys():
        if method.startswith('to_'):
            out_form=method.replace('to_','').replace('_','.')
            dict_translate[form][out_form]= getattr(api, method)

    dict_make_quantity[form] = api.make_quantity
    dict_make_unit[form] = api.make_unit
    dict_get_value[form] = api.get_value
    dict_get_unit[form] = api.get_unit
    dict_get_unit_name[form] = api.get_unit_name
    dict_convert[form] = api.convert

del(base_package, forms_library, forms_apis_modules, forms_apis)
del(form, out_form, method, api)

