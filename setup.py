from setuptools import find_packages, setup

def get_requirements(requirement_file_path):
    required_modules = []
    with open(requirement_file_path, 'r') as f:
        for line in f:
            module = line.strip()
            if(module != '-e .'):
                required_modules.append(module)

    return required_modules


setup(
    name="ml_project",
    version="0.0.1",
    author="Mukul Jain",
    author_email="mukulj2018@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

