# chdir to the directory that this script file lives in.
cd $(dirname $(readlink -f $0))

# load the pru excutable.
cp /opt/aproc/pru/pstrobe.out /lib/firmware/pru

echo "stop"
echo 'stop' > /sys/class/remoteproc/remoteproc1/state

echo "load"
echo 'pru/pstrobe.out' > /sys/class/remoteproc/remoteproc1/firmware

echo "start"
echo 'start' > /sys/class/remoteproc/remoteproc1/state

# Run the arm program.
my_program=/opt/aproc/bin/astrobe
echo $my_program
rlfe sudo $my_program $1


