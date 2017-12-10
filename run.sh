echo 'Internet Population';
echo 'Enter port';
read port;
echo 'Run debug mode? (1/0)';
read temp;
if [ "$temp" -eq 1 ]; then
    export FLASK_DEBUG=1;
fi
export FLASK_APP=./code/website.py;
flask run -h 0.0.0.0 -p $port;
