import yaml

library_name="Test-UIBCDF-Library"

with open('../requirements.yaml') as fff:
    all_requirements = yaml.load(fff, Loader=yaml.FullLoader)

# Production
env_name=library_name
env_dict={}
env_dict["name"]=env_name
env_dict["channels"]=all_requirements["production"]["channels"]
env_dict["dependencies"]=all_requirements["production"]["dependencies"]
fff = open("production_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=False)
fff.close()

# Development
env_name=library_name+"_dev"
env_dict={}
env_dict["name"]=env_name
env_dict["channels"]=all_requirements["development"]["channels"]
env_dict["dependencies"]=all_requirements["development"]["dependencies"]
fff = open("development_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=False)
fff.close()

# Test
env_name=library_name+"_test"
env_dict={}
env_dict["name"]=env_name
env_dict["channels"]=all_requirements["test"]["channels"]
env_dict["dependencies"]=all_requirements["test"]["dependencies"]
fff = open("test_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=False)
fff.close()

# Docs
env_name=library_name+"_docs"
env_dict={}
env_dict["name"]=env_name
env_dict["channels"]=all_requirements["docs"]["channels"]
env_dict["dependencies"]=all_requirements["docs"]["dependencies"]
fff = open("docs_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=False)
fff.close()

# Setup
env_name=library_name+"_setup"
env_dict={}
env_dict["name"]=env_name
env_dict["channels"]=all_requirements["setup"]["channels"]
env_dict["dependencies"]=all_requirements["setup"]["dependencies"]
fff = open("setup_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=False)
fff.close()

# Build
env_name=library_name+"_build"
env_dict={}
env_dict["name"]=env_name
env_dict["channels"]=all_requirements["conda-build"]["channels"]
env_dict["dependencies"]=all_requirements["conda-build"]["dependencies"]
fff = open("build_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=False)
fff.close()


