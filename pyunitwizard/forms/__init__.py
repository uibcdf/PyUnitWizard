from importlib import import_module as _import_module

dict_is_form={}
dict_is_unit={}
dict_is_quantity={}
dict_get_value={}
dict_get_unit={}
dict_make_quantity={}
dict_translate={}
dict_convert={}
dict_string_to_quantity={}
dict_string_to_unit={}
dict_to_string={}
dict_dimensionality={}
dict_compatibility={}

_base_package = __name__.replace('.base','')
_forms_apis_modules = {'openmm.unit':'api_openmm_unit', 'pint':'api_pint', 'unyt':'api_unyt'}

def load_library(library):

    from pyunitwizard.kernel import loaded_libraries, loaded_parsers

    api = _import_module('.'+_forms_apis_modules[library], _base_package)

    dict_is_form.update(api.is_form)
    dict_is_unit[library]=api.is_unit
    dict_is_quantity[library]=api.is_quantity
    dict_get_value[library] = api.get_value
    dict_get_unit[library] = api.get_unit
    dict_make_quantity[library] = api.make_quantity
    dict_convert[library] = api.convert
    dict_translate[library]={}
    dict_string_to_quantity[library] = api.string_to_quantity
    dict_string_to_unit[library] = api.string_to_unit
    dict_dimensionality[library] = api.dimensionality
    dict_compatibility[library] = api.compatibility

    dict_translate[library]['string']=api.to_string
    api_string = _import_module('.api_string', _base_package)
    dict_translate['string'][library]= getattr(api_string, 'to_'+library.replace('.','_'))
    del(api_string)

    for method in api.__dict__.keys():
        if method.startswith('to_'):
            out_form=method.replace('to_','').replace('_','.')
            if out_form in loaded_libraries:
                dict_translate[library][out_form]= getattr(api, method)
    if api.parser:
        loaded_parsers.append(library)

    for library_loaded in loaded_libraries:
        api = _import_module('.'+_forms_apis_modules[library_loaded], _base_package)
        for method in api.__dict__.keys():
            if method.startswith('to_'):
                out_form=method.replace('to_','').replace('_','.')
                if out_form == library:
                    dict_translate[library_loaded][library]= getattr(api, method)
                    break

    loaded_libraries.append(library)
    del(api)

    pass

# load_string

api = _import_module('.api_string', _base_package)

dict_is_form.update(api.is_form)
dict_is_unit['string']=api.is_unit
dict_is_quantity['string']=api.is_quantity
dict_get_value['string'] = api.get_value
dict_get_unit['string'] = api.get_unit
dict_make_quantity['string'] = api.make_quantity
dict_convert['string'] = api.convert
dict_translate['string']={}
dict_string_to_quantity['string'] = api.string_to_quantity
dict_string_to_unit['string'] = api.string_to_unit
dict_dimensionality['string'] = api.dimensionality
dict_compatibility['string'] = api.compatibility

del(api)

