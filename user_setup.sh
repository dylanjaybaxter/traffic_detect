#!/bin/bash/

if [ $# -ne 0 ] ; then
    # Create local site package dir and download python dependencies
    python_dir=$1
    mkdir $python_dir
    python3 -c "import sys; sys.path.append(\"${python_dir}\")"
    export PYTHONPATH=$PYTHONPATH:${python_dir}
    check_python_package() {
        local package_name=$1
        python3 -c "import $package_name" &> /dev/null
        if [ $? -ne 0 ]; then
            echo "The package '$package_name' is not installed."
            python3 -m pip install --target=$python_dir $package_name
        else
            echo "The package '$package_name' is installed."
        fi
    }
    check_python_package "-r requirements.txt"
    export PATH=$PATH:${python_dir}bin/

else
    echo "Please enter a username in the form:"
    echo ". user_setup.sh [USERNAME]"
    echo "!!!!!THE DOT BEFORE THE SCRIPT NAME IS IMPORTANT!!!!"
fi