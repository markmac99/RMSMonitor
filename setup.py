setup(
    name="RMSMonitor",
    version="1.0.0",
    description="Check status of some RMS cameras",
    #long_description=README,
    #long_description_content_type="text/markdown",
    #url="https://github.com/realpython/reader",
    author="Mark McIntyre",
    #author_email="info@realpython.com",
    license="BSD 3-Clause License",
    classifiers=[
        "License :: OSI Approved :: BSD 3-Clause License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["."],
    include_package_data=True,
    install_requires=[
        "tkinter", "requests", "configparser", "datetime"
    ],
    entry_points={"console_scripts": ["RMSMonitor=checkStatus.__main__:main"]},
)
