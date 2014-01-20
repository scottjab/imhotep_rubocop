from setuptools import setup, find_packages

setup(
    name='imhotep_rubocop',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/scottjab/imhotep_rubocop',
    license='MIT',
    author='James Scott',
    author_email='scottjab@gmail.com',
    description='An imhotep plugin for ruby-lint validation',
    entry_points={
        'imhotep_linters': [
            '.py = imhotep_rubocop.plugin:RubyLintLinter'
        ],
    },
)
