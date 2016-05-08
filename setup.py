from setuptools import setup

setup(
    name='PyUpdater-s3-Plugin',
    version='2.5',

    description='Amazon S3 plugin for PyUpdater',

    author='JohnyMoSwag',
    author_email='johnymoswag@gmail.com',

    url='https://github.com/JohnyMoSwag/PyUpdater-s3-Plugin',

    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2.7',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=['pyupdater.plugins',
              ],

    install_requires=[
        'boto3',
        'jms-utils >= 0.6.2',
        ],

    py_modules=['s3_plugin'],

    include_package_data=True,

    entry_points={
        'pyupdater.plugins.uploaders': [
            's3 = s3_plugin:S3Uploader',
        ],
    },

    zip_safe=False,
)
